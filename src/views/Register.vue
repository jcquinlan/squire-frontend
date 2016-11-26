<template>
  <div id="register">
      <h4 class="view-title">Register</h4>
      <p v-if="registerError">{{ registerError }}</p>
      <div class="card">
          <form>
              <div class="row">
                  <div class="input-field col m6">
                       <input id="user_name" v-model="registerForm.username" type="text" class="validate" placeholder="Username">
                  </div>

                  <div class="input-field col m6">
                       <input id="email" v-model="registerForm.email" type="email" class="validate" placeholder="Email">
                  </div>
              </div>

              <div class="row">
                  <div class="input-field col s12">
                      <input id="password" v-model="registerForm.password" type="password" class="validate" placeholder="Password">
                  </div>
              </div>

              <div class="row">
                  <div class="input-field col s12">
                      <input id="password" v-model="registerForm.confirm_password" type="password" class="validate" placeholder="Confirm password">
                  </div>
              </div>

              <button class="btn" type="button" @click.prevent="register">Register</button>
          </form>
      </div>
  </div>
</template>

<script>
import { RegisterForm } from '../forms/RegisterForm';

export default {
    data () {
        return {
          registerForm: new RegisterForm(),
          registerError: ''
        }
    },
    methods: {
        register(){
            if(this.registerForm.parse().username != '' && this.registerForm.parse().password != ''){
                if(this.registerForm.password == this.registerForm.confirm_password){
                    this.$http.post('users/', this.registerForm.parse()).then((response) => {
                        console.log('success');
                        this.registerForm.clean();
                        this.registerError = '';
                        this.$router.push('/login');
                    }, (error) => {
                        this.registerError = error.body.username[0] || 'Invalid request.'
                    })
                } else {
                    this.registerError = 'Your passwords do not match.';
                    this.registerForm.password = '';
                    this.registerForm.confirm_password = '';
                }
            }
            else {
                this.registerError = 'Please fill out registration form.'
            }
        }
    }
}
</script>

<style lang="scss" scoped>

</style>
