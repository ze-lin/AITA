import Vue from 'vue'
import Router from 'vue-router'
import Log from './views/Log.vue'
import Home from './views/Home.vue'
//import Learn from './views/Learn.vue'
import Personal from './views/Personal.vue'
import CourseManagement from './views/CourseManagement.vue'
import Test from './views/test.vue'

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
      path: '/course-management',
      name: 'course-management',
      component: CourseManagement
    },
    {
      path: '/personal',
      name: 'personal',
      component: Personal
    },
    {
      path: '/test',
      name: 'test',
      component: Test
    }
  ]
})
