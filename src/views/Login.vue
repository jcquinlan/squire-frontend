<template>
  <div id="login">
      <h4 class="view-title">Login</h4>
      <p v-for="loginError of loginErrors">{{ loginError }}</p>
      <div class="card">
          <form>
              <div class="row">
                  <div class="input-field col s12">
                       <input id="user_name" v-model="loginForm.username" type="text" class="validate" placeholder="Username">
                  </div>

                  <div class="input-field col s12">
                      <input id="password" v-model="loginForm.password" type="text" class="validate" placeholder="Password">
                  </div>
              </div>
              <button class="btn" type="button" @click.prevent="login">Login</button>
          </form>
      </div>
  </div>
</template>

<script>
import Vue from 'vue';
import { resource } from '../resources';
import { LoginForm } from '../forms/LoginForm';


function parseJwt (token) {
            var base64Url = token.split('.')[1];
            var base64 = base64Url.replace('-', '+').replace('_', '/');
            return JSON.parse(window.atob(base64));
        };

export default {
    data () {
        return {
          loginForm: new LoginForm(),
          loginErrors: [],
        }
    },
    methods: {
        login(){
            if(this.loginForm.parse().username != '' && this.loginForm.parse().password != ''){
                this.$store.commit('setLoading', true);
                resource.login.save(this.loginForm.parse()).then((response) => {
                    this.$store.commit('setLoading', false);
                    localStorage.setItem('user-token', response.body.token)
                    this.$http.headers.common['Authorization'] = `JWT ${ localStorage.getItem('user-token')}`;
                    this.loginForm.clean();
                    this.loginError = '';
                    this.$store.commit('update_logged_in');
                    this.$store.commit('set_user', parseJwt(response.body.token));
                    this.$router.push('/characters');

                }, (error) => {
                    this.$store.commit('setLoading', false);
                    this.loginErrors = [];
                    for(let key of Object.keys(error.body)){
                        this.loginErrors.push(error.body[key][0])
                    }
                })
            }
            else {
                this.loginErrors = [];
                this.loginForm.clean();
                this.loginErrors.push('Please fill out login form.');
            }
        }
    }
}
</script>

<style lang="scss" scoped>

</style>
