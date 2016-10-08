import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        logged_in: false,
        user: null,
    },
    mutations: {
        update_logged_in(state){
            state.logged_in = !state.logged_in;
        },

        set_user(state, user){
            state.user = user;
        }
    }
})
