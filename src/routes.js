import Vue from 'vue';
import VueRouter from 'vue-router'

import Login from './views/Login'
import Register from './views/Register'
import Characters from './views/Characters'
import CreateCharacter from './views/CreateCharacter'
import Dashboard from './views/Dashboard'
import Journal from './views/Journal'

Vue.use(VueRouter);

const routes = [
  { name: 'login', path: '/login', component: Login },
  { name: 'register', path: '/register', component: Register },
  { name: 'characters', path: '/characters', component: Characters },
  { name: 'create-character', path: '/characters/create', component: CreateCharacter },
  { name: 'dashboard', path: '/dashboard', component: Dashboard },
  { name: 'journal', path: '/journal', component: Journal },
]

export const router = new VueRouter({
    mode: 'history',
    routes // short for routes: routes
})
