// vue.config.js
// For CORS policy
// https://medium.com/js-dojo/how-to-deal-with-cors-error-on-vue-cli-3-d78c024ce8d3
// https://cli.vuejs.org/config/#devserver-proxy
module.exports = {
  devServer: {
    proxy: 'http://localhost:5000/',
  }
}