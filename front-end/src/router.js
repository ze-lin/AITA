import Vue from 'vue'
import Router from 'vue-router'
import Log from './views/Log.vue'
import Home from './views/Home.vue'
import Learn from './views/Learn.vue'
import Personal from './views/Personal.vue'
import CourseManagement from './views/CourseManagement.vue'
import Course from './views/Course.vue'
import Video from './components/Video.vue'
import Reading from './components/Reading.vue'
import Exam from './components/Exam.vue'
import StudentResult from './components/StudentResult.vue'
import TeacherResult from './components/TeacherResult'

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
      path: '/learn',
      name: 'learn',
      component: Learn,
      children: [
        {
          path: '/learn/video/:id',
          name: 'video',
          component: Video
        },
        {
          path: '/learn/reading/:id',
          name: 'reading',
          component: Reading
        },
        {
          path: '/learn/exam/:id',
          name: 'exam',
          component: Exam
        },
        {
          path: '/learn/result/:id',
          name: 'studentResult',
          component: StudentResult
        }
      ]
    },
    {
      path: '/course',
      name: 'course',
      component: Course
    },
    {
      path: '/result/:id',
      name: 'result',
      component: TeacherResult
    }
  ]
})
