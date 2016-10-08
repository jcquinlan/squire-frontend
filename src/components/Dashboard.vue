<template>
  <div id="login">
      <p>{{ loginError }}</p>
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
              <button type="button" @click="loginForm.clean()" name="button">Clear</button>
          </form>
      </div>
  </div>
</template>

<script>

export default {
    data () {
        return {}
    },
    methods: {}
}
</script>

<style lang="scss" scoped>

</style>
