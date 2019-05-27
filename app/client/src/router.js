import Vue from 'vue'
import Router from 'vue-router'
import Auth from './views/Auth.vue'
import Home from './views/Home.vue'
import Course from './views/Course.vue'
import PersonInfo from './views/PersonInfo.vue'
import CourseManage from './views/CourseManage.vue'
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
      name: 'home',
      component: Home
    },
    {
      path: '/auth',
      name: 'auth',
      component: Auth
    },
    {
      path: '/course-manage',
      name: 'course-manage',
      component: CourseManage
    },
    {
      path: '/person-info',
      name: 'person-info',
      component: PersonInfo
    },
    {
      path: '/course',
      name: 'course',
      component: Course,
      children: [
        {
          path: '/course/video/:id',
          name: 'video',
          component: Video
        },
        {
          path: '/course/reading/:id',
          name: 'reading',
          component: Reading
        },
        {
          path: '/course/exam/:id',
          name: 'exam',
          component: Exam
        },
        {
          path: '/course/result/:id',
          name: 'student-result',
          component: StudentResult
        }
      ]
    },
    {
      path: '/result/:id',
      name: 'result',
      component: TeacherResult
    }
  ]
})
