import Vue from 'vue';
import VueResource from 'vue-resource';

Vue.use(VueResource);
Vue.http.options.root = 'http://localhost:8000';

function createTokenHeader(){
    let token = localStorage.getItem('user-token');
    return { headers: { "Authorization": `Token ${ token }`}}
}

const login = Vue.resource('api-token-auth/');
const characters = Vue.resource('characters/');
const users = {
    "me": Vue.resource('auth/me/', {}, {}, createTokenHeader()),
}

export const resource = {
    login,
    characters,
    users,
}
