import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import router from './router'
import axios from 'axios'

Vue.config.productionTip = false
axios.defaults.withCredentials = true

const source = {
  usr: 'ludanxer',
  role: 'teacher',
  course_id: ''
}

new Vue({
  data: source,
  router,
  render: h => h(App)
}).$mount('#app')
