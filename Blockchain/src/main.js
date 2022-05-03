// import Vue from 'vue'
import Vue from 'vue/dist/vue.js';
import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
// import VueRouter from 'vue-router'
// import Register from './components/Register.vue'

Vue.config.productionTip = false
// Vue.use(VueRouter)

// const routes = [
//   { path: '/', component: App },
//   { path: '/register', component: Register }
// ]

// const router = new VueRouter({
//   routes // short for `routes: routes`
// })

new Vue({
  render: h => h(App),
}).$mount('#app')

// new Vue({
//   router
// }).$mount('#app')
