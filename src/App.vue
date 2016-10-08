<template>
    <div id="app">
        <nav>
            <div class="nav-wrapper">
              <a href="#" class="brand-logo">squire</a>
              <span v-if="loggedIn">{{ username }}</span>
              <ul id="nav-mobile" class="right hide-on-med-and-down">
                  <li v-if="!loggedIn"><router-link to="/login">Login</router-link></li>
                  <li v-if="!loggedIn"><router-link to="/register">Register</router-link></li>
              </ul>
            </div>
        </nav>

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

export default {
    store,
    computed: {
        loggedIn(){
            return store.state.logged_in;
        },

        username(){
            return store.state.user.username;
        }
    },
    methods: {},
    mounted: () => {
        let token = localStorage.getItem('user-token');
        if(token) {
            let requestOptions =  { headers: { "Authorization": `Token ${ token }`}}
            resource.users.me.get('auth/me/', requestOptions).then((response) => {
                store.commit('update_logged_in');
                store.commit('set_user', response.body);
                this.$router.push('/dashboard');
            },
            (error) => {
                localStorage.removeItem('user-token');
                this.$router.push('/login');
            });
        }
    }
}
</script>

<style src="../node_modules/materialize-css/dist/css/materialize.css"></style>
<style lang="scss">
    @import 'variables';

    html {
      height: 100%;
    }

    body {
      height: 100%;
      background-color: $light-grey;
    }

    nav {
        .nav-wrapper {
            padding: 0 20px;
            background-color: $primary-cool;
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
</style>
