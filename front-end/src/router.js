import Vue from 'vue'
import Router from 'vue-router'
import Log from './views/Log.vue'
import Home from './views/Home.vue'
import Course from './views/Course.vue'
import Personal from './views/Personal.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'log',
      component: Log
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/course',
      name: 'course',
      component: Course
    },
    {
      path: '/personal',
      name: 'personal',
      component: Personal
    }
  ]
})
