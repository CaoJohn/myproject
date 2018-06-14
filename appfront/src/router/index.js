import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Hello from '@/components/Hello'
import Uikit_test from '@/components/Uikit_test'
import Workstation from '@/components/Workstation'
import Caseworkstation from '@/components/Caseworkstation'
import Test from '@/components/Test'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/hello',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/uikit_test',
      name: 'uikit_test',
      component: Uikit_test
    },
    {
      path: '/workstation',
      name: 'workstation',
      component: Workstation
    },
    {
      path: '/caseworkstation',
      name: 'caseworkstation',
      component: Caseworkstation
    },
    {
      path: '/test',
      name: 'test',
      component: Test
    }
  ]
})
