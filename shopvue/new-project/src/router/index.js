import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
  
      redirect(){return '/login'}
    },
    {
      path: '/login',
      name: '登录',
      component:()=>import('@/view/login.vue')
    },
    {
      path: '/index',
      name: '首页',
      component:()=>import('@/view/index.vue'),
      children:[
        {
          path: '/user',
          name: '登录',
          component:()=>import('@/view/user.vue')
        },
      ]
    }
  ]
})
