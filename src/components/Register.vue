<template>
  <div id="register">
      <div id="login">
          <p v-if="registerError">{{ registerError }}</p>
          <div class="card">
              <form>
                  <div class="row">
                      <div class="input-field col s12">
                           <label for="user_name">Username</label>
                           <input id="user_name" v-model="registerForm.username" type="text" class="validate">
                      </div>

                      <div class="input-field col s12">
                           <label for="password">Password</label>
                          <input id="password" v-model="registerForm.password" type="text" class="validate">
                      </div>
                  </div>
                  <button class="btn" type="button" @click.prevent="register">Register</button>
              </form>
          </div>
      </div>
  </div>
</template>

<script>

class RegisterForm {
    constructor(){
        this.username = '';
        this.password = '';
    }

    clean(){
        this.username = '';
        this.password = '';
    }

    parse(){
        return {
            "username": this.username,
            "password": this.password,
        }
    }
}

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
                this.$http.post('auth/register/', this.registerForm.parse()).then((response) => {
                    this.registerForm.clean();
                    this.registerError = '';
                    this.$router.push('/login');
                }, (error) => {
                    this.registerError = 'Invalid request.'
                })
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
