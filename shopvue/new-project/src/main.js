// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'   //导入store
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);
Vue.config.productionTip = false

router.beforeEach((to, from, next) => {

  let token = JSON.parse(localStorage.getItem("user"))
  if (to.path === '/login') {
    next();
  } else {
    let token = localStorage.getItem('user');
 
    if (token === null || token === '') {
      next('/login');
    } else {
      next();
    }
  }

})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
