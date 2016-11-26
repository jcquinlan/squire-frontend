<template>
    <div id="app">
        <nav>
            <div class="container">
                <div class="nav-wrapper">
                  <a href="#" class="brand-logo">squire</a>
                  <span v-if="loggedIn" class="username">hello, {{ username }}</span>
                  <ul id="nav-mobile" class="right">
                      <li v-if="!loggedIn"><router-link to="/login">Login</router-link></li>
                      <li v-if="!loggedIn"><router-link to="/register">Register</router-link></li>

                      <li v-if="loggedIn && selectedCharacter"><router-link to="/dashboard">Dashboard</router-link></li>
                      <li v-if="loggedIn"><router-link to="/characters">Characters</router-link></li>
                      <li v-if="loggedIn"><a @click.prevent="logout()">Logout</a></li>
                  </ul>
                </div>
            </div>
        </nav>

        <div v-if="loading" class="progress">
            <div class="indeterminate"></div>
        </div>

        <div id="content">
            <div class="container">
                <router-view></router-view>
            </div>
        </div>

        <footer class="page-footer">
          <div class="footer-copyright">
            <div class="container">
            © 2016 Squire
            </div>
          </div>
        </footer>

    </div>
</template>

<script>
import { store } from './store';
import { resource } from './resources';

function parseJwt (token) {
            var base64Url = token.split('.')[1];
            var base64 = base64Url.replace('-', '+').replace('_', '/');
            return JSON.parse(window.atob(base64));
        };

export default {
    store,
    computed: {
        loggedIn(){
            return store.state.logged_in;
        },

        username(){
            return store.state.user.username;
        },

        selectedCharacter(){
            return store.state.selected_character;
        },
        loading(){
            return store.state.loading;
        }
    },
    methods: {
        logout(){
            if(localStorage.getItem('user-token')) localStorage.removeItem('user-token');
            if(store.state.logged_in) store.commit('update_logged_in');
            if(store.state.user) store.commit('set_user', null);
            this.$router.push('/login');
        },
    },
    mounted(){
        let token = localStorage.getItem('user-token');
        if (!token){
            this.$router.push('login');
        } else {
            store.commit('set_user', parseJwt(token));
            store.commit('update_logged_in');
        }
    }
}
</script>

<style src="../node_modules/materialize-css/dist/css/materialize.css"></style>
<style lang="scss">
    @import 'variables';

    html {
      height: 100%;
      font-family: $primary-font;
      font-weight: 300;
    }

    body {
      height: 100%;
      background-color: $light-grey;

      select {
          display: block;
      }
    }

    nav {
        background-color: $primary-cool;
        .nav-wrapper {
            padding: 0 20px;
            background-color: $primary-cool;

            .username {
                float: right;
                margin-left: 20px;
            }
        }
    }

    .progress {
        margin: 0;
    }

    textarea {
        resize: none;
        border: none;

        &:active, &:focus {
            outline: none;
        }
    }

    #app {
        height: 100%;
        display: flex;
        flex-direction: column;

        #content {
            flex: 1 0 auto;
        }

        footer {
            flex: 0 0 auto;
            &.page-footer {
                background-color: $primary-cool;
            }
        }
    }

    .card {
        padding: 10px 20px;
    }

    .view-title {
        margin: 40px 0;
    }

    /* ----------------------------------------------------- Media Queries */
    @media only screen and (max-width: 992px){
        nav .brand-logo {
            left: 0;
            transform: none;
        }
    }
</style>
