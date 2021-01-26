import axios from 'axios';

export default {
  methods: {
    logButton: async function (message) {
      const api_request = require('axios')

      await api_request({
          method: 'post',
          url: this.appSettings.url_log_click,
          data: {
            logmessage: message
          }
      })
      .then(response => {
          if (response.status === 201) {
            // console.log('XXX')
          }
      })
      .catch( () => {
      })

    },  //logButton

    logAction: async function (message) {
      const api_request = require('axios')

      await api_request({
          method: 'post',
          url: this.appSettings.url_log_action,
          data: {
            logmessage: message
          }
      })
      .then(response => {
          if (response.status === 201) {
            // console.log('XXX')
          }
      })
      .catch( () => {
      })

    },  //logAction
  },
  computed: {
    appSettings () {
      return this.$store.state.appSettings
    },
  },
}

