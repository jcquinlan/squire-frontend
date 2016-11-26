import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        logged_in: false,
        user: '',
        selected_character: null,
        selected_journal: null,
        loading: false,
    },
    mutations: {
        update_logged_in(state){
            state.logged_in = !state.logged_in;
        },

        set_user(state, user){
            state.user = user;
        },

        set_selected_character(state, character){
            state.selected_character = character;
        },

        set_selected_journal(state, journal){
            state.selected_journal = journal;
        },

        set_loading(state, loadingBool) {
            state.loading = loadingBool;
        }
    }
})
