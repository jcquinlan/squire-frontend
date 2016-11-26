import Vue from 'vue';
import VueResource from 'vue-resource';

Vue.use(VueResource);
Vue.http.options.root = 'http://localhost:8000';

const login = Vue.resource('api-token-auth/');
const characters = Vue.resource('characters/');
const users = {
    "all": Vue.resource('users/'),
    "me": Vue.resource('users/{user_id}'),
}

function authorizationHeader(){
    return { Authorization: `JWT ${ localStorage.getItem('user-token')}` };
}

export const resource = {
    login,
    characters,
    users,
    authorizationHeader,
}
