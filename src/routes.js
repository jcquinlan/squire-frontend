import Vue from 'vue';
import VueRouter from 'vue-router'

import Login from './components/Login'
import Register from './components/Register'

Vue.use(VueRouter);

const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Register },
]

export const router = new VueRouter({
    mode: 'history',
    routes // short for routes: routes
})
