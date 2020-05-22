import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false


const vm = new Vue({
  router,
  store,
  render: h => h(App)
})
// mount the Vue after the interceptors, so that the interceptors
// can be used coming from request in the life hooks

// Original 
// new Vue({
//   router,
//   store,
//   render: h => h(App)
// }).$mount('#app')      



//////////////////////////////////////////////////////////////////////////////////
///////////////////  AXIOS settings and interceptors  ////////////////////////////
// 
// ** api_request , request interceptor when OK
// Add the access-token to the header
//
// ** api_request , response interceptor when NOT OK
// in case no code 401: retry the orignal request x times
// in case 401: refresh the token  and next retry 1 time
// 
//
// Store the access-token and refresh-token in the localStorage, so that these values 
// can be retreived before login so that maybe the user does not have to login again.


// Create instances of axios with different names, 
// so that different settings and interceptors can be used per axios instance

import axios from 'axios'               // used for temporary requests
import api_request from 'axios'         // For API requests to Django backend


// Default settings for instance axios
axios.defaults.baseURL = store.state.appSettings.url_api_base

// Default settings for instance api_request. The request  will use:  baseURL + url 
api_request.defaults.baseURL = store.state.appSettings.url_api_base 
// Get the updated access token in the request interceptor, to be sure it is the most recent access-token  
// api_request.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('access-token')


 /////////////////////////////////////////////////////////////////////////////////////
// Define a request function to be used within the interceptors
async function retry_attempt (config) {
  // Define an axios request instance with other name than the current interceptors.
  // so that this request will not be handled by the interceptors.
  // Async function, to wait for the result for the whole function
  //
  //  INPUT:  the error.config, which are the settings from a failed request
  //  OUTPUT: list with:
  //            * boolean for success
  //            * the response or error from this request

  // create a temporary axios instance to use in this function
  const api_call = axios.create()
  var success = false             // true when a response is received, false with error
  var output = ''                 // to contain the response or error

  await api_call(config)
      .then(response => {
        // JSON responses are automatically parsed.
        // console.log('retry-attempt-ok')
        // // console.log(response.status)
        success = true
        output = response
      })
      .catch(error => {
        // console.log('retry-attempt-not-ok')
        // // console.log(error)
        output = error
      })

      // result of this function
      return [success, output]

  }// END retry_attempt


/////////////////////////////////////////////////////////////////////////////////////
// Function to set a waiting time, like : await sleep(3000)
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}


 /////////////////////////////////////////////////////////////////////////////////////
// *** REQUEST interceptor
api_request.interceptors.request.use(
  
  function (config) {
    // Actions to do before the request is sent
    // // console.log('Interceptor request OK')
    // // console.log(config)

    // Update access token in every request
    const access_token = localStorage.getItem('access-token')
    if (access_token) {
      config.headers.Authorization = 'Bearer ' + access_token
      config.headers.Accept = 'application/json'
    }//END if

    // return the request settings with the new header
    if (config.headers.Authorization) {
        // // console.log('Access token before request: ', config.headers.Authorization)
        return config
    } else {
        // // console.log('Access token before request: ')
        return config
    }
  }, //END before request handling

  function (error) {
    // Actions to do with request error
    // console.log('Interceptor request Error')
    return Promise.reject(error);
  }//END error handling

)//END request interceptor


 /////////////////////////////////////////////////////////////////////////////////////
// *** RESPONSE interceptor
api_request.interceptors.response.use(
  function (response) {
    // Any status code that lie within the range of 2xx cause this function to trigger
    // Do something with response data
    // // console.log('Interceptor response OK')

    return response
  },
  async function (error) {
    // async function, so that await can be used so that every retry is handled sequentially
    // Any status codes that falls outside the range of 2xx cause this function to trigger
    // Do N_retry retries with the current access-token.
    // When this still fails, then to a refresh token request and
    // try again with the new access token.
    // When this also fails then remove all token and redirect to login page

    // The following can be retreived from the error
    // error.response
    // error.config   (settings of orginal request)

    // console.log('Interceptor response Not OK')
    // error.response
    // error.message   (like Network Error)
    
    if (error.message) {
      // console.log('Message: ', error.message)
    }

    // In case the error has no response part this will imply Network error
    // Directly signal the errror
    if (!error.response) {
      alert("Data kan niet verstuurd worden door netwerk problemen")
      return Promise.reject(error)

    } else if (error.response.status !== 401) {
    // In case there is a response check the status
    // Retry original request n times in case there was no authentication failure (!== 401)
    
      var success = false       // indicator for successful API call
      var n_retry = 1           // number of times the request must be repeated.
      var counter = 0           // this counts the number of retries
      const timeout = 1000      // waiting time before retry

      // Retry de original request n_retry times
      while (success === false && counter < n_retry) {
        await sleep(timeout)
        // // console.log(counter)
        counter = counter + 1
        var result = await retry_attempt(error.config)
        // // console.log('test', result)

        if (result[0] === true) {
          // // console.log(result[0])
          // success is true to exit the while loop
          success = true
        } else {
          // console.log(result[0])
        }
      } // end while loop

      // If request succeeded, than return the response
      if (success === true) {
        // return the response from the latest retry
        return result[1]
      } else {
        // alert("Verzoek niet afgehandeld door een fout")
        return Promise.reject(error)
      }

    } else {      // else for == 401, not authorized
      // Refresh the token and retry the original request

      const refresh_token = localStorage.getItem("refresh-token")
      var new_access_token = ''
      var refresh_ok = false        //Indicates that reqeust for new access-token has succeeded

      // Create a new axios instance with an other name 
      // this request will not be catched by the interceptors
      const api_refresh = axios.create()
    
      // User the refresh to get a new access token
      await api_refresh({
        method: 'post',
        url: store.state.appSettings.url_refresh_token,
        data: {
          refresh: refresh_token
        }
      })
          .then(response => {
            // JSON responses are automatically parsed.
            // console.log('refresh token ok')

            localStorage.setItem('access-token', response.data.access)

            // Get the user from localStore and store this in Vuex (store)
            var user = store.state.user
            user.usename = localStorage.getItem('username')
            user.user_is_logged_in = true
            // At main.js use store in stead of $store
            store.dispatch('updateUser', user)

            // // console.log('User is: ', store.state.user.username)

            new_access_token = response.data.access
            refresh_ok = true
          })
          .catch(() => {
            // this represents refresh_ok is not true (did not succeed)
            // console.log('refresh token not-ok')
            // console.log(error.message)
            // When refresh token failed it could be because the refresh token has expired
            // Set user to logged out and go tho Login page
            var user = store.state.user
            user.user_is_logged_in = false
            // At main.js use store in stead of $store
            store.dispatch('updateUser', user)
            router.push({ name: 'Login' }) 
          })
  

      // Do the original request with the new access token when the refresh succeeded
      if (refresh_ok === true) {
        const api_new_access = axios.create()
        var config = error.config
        config.headers.Authorization = 'Bearer ' + new_access_token

        // Need to return a resolved or rejected promise
        return new Promise((resolve, reject) => {
          api_new_access(config).then(response => {
            resolve(response);
          }).catch((error) => {
            alert("Data kan niet verstuurd worden door netwerk problemen")
            reject(error);
          })
        })// END promise

      }// end if refresh_ok
    
    } //END if-else 401

  }// End async error functions

)// End interceptor response


//////////////////////////////////////////////////////////////////////////////////
///////////////////  mount Vue after the interceptors ////////////////////////////
vm.$mount('#app');

// mount the Vue after the interceptors, so that the interceptors
// can be used coming from request in the life hooks

