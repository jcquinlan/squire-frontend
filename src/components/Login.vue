<template>
  <div id="login">
      <p v-if="loginError">{{ loginError }}</p>
      <div class="card">
          <form>
              <div class="row">
                  <div class="input-field col s12">
                       <label for="user_name">Username</label>
                       <input id="user_name" v-model="loginForm.username" type="text" class="validate">
                  </div>

                  <div class="input-field col s12">
                       <label for="password">Password</label>
                      <input id="password" v-model="loginForm.password" type="text" class="validate">
                  </div>
              </div>
              <button class="btn" type="button" @click.prevent="login">Login</button>
          </form>
      </div>
  </div>
</template>

<script>
import { resource } from '../resources';
import { LoginForm } from '../forms/LoginForm';

export default {
    data () {
        return {
          loginForm: new LoginForm(),
          loginError: ''
        }
    },
    methods: {
        login(){
            if(this.loginForm.parse().username != '' && this.loginForm.parse().password != ''){
                resource.login.save(this.loginForm.parse()).then((response) => {
                    localStorage.setItem('user-token', response.body.token)
                    this.loginForm.clean();
                    this.loginError = '';
                    this.$store.commit('update_logged_in');
                    this.$store.commit('set_user', response.body)
                    this.$router.push('/dashboard')

                }, (error) => {
                    this.loginError = 'Invalid login information provided.'
                })
            }
            else {
                this.loginForm.clean();
                this.loginError = 'Please fill out login form.'
            }
        }
    }
}
</script>

<style lang="scss" scoped>

</style>
