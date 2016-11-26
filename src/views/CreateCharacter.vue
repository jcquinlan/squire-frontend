<template>
  <div id="register">
      <h4 class="view-title">Create New Character</h4>
      <p v-for="error of characterErrors">{{ error }}</p>
      <div class="card">
          <form>
              <div class="row">
                  <div class="input-field col m6">
                       <input id="first_name" v-model="characterForm.first_name" type="text" class="validate" placeholder="First Name">
                  </div>

                  <div class="input-field col m6">
                       <input id="last_name" v-model="characterForm.last_name" type="text" class="validate" placeholder="Last Name">
                  </div>
              </div>

              <div class="row">
                  <div class="input-field col s6">
                      <select id="class-select" v-model="characterForm.class_type">
                          <option v-for="classType of classes" :value="classType[0]">{{ classType[1] }}</option>
                      </select>
                  </div>

                  <div class="input-field col s6">
                      <select id="class-select" v-model="characterForm.race">
                          <option v-for="race of races" :value="race[0]">{{ race[1] }}</option>
                      </select>
                  </div>
              </div>

              <div class="row">
                  <div class="input-field col s12">
                      <input id="class" v-model="characterForm.background" type="text" class="validate" placeholder="Background">
                  </div>
              </div>

              <div class="row">
                  <div class="input-field col s6">
                      <input id="max_hitpoints" v-model="characterForm.max_hitpoints" type="text" class="validate" placeholder="Max Hitpoints">
                  </div>

                  <div class="input-field col s6">
                      <input id="armor_class" v-model="characterForm.armor_class" type="text" class="validate" placeholder="Armor Class">
                  </div>
              </div>

              <button class="btn" type="button" @click.prevent="createCharacter">Create Character</button>
          </form>
      </div>
  </div>
</template>

<script>
import { CreateCharacterForm } from '../forms/CreateCharacterForm';
import { resource } from '../resources';

export default {
    data () {
        return {
          characterForm: new CreateCharacterForm(),
          characterErrors: [],
          classes: '',
          races: '',
        }
    },
    created () {
        this.$http.get('api/classes/', { headers: resource.authorizationHeader() }).then(response => {
            this.classes = response.body;
        }, error => {
            if(error.status === 403){
                localStorage.removeItem('user-token');
                this.$store.commit('update_logged_in');
                this.$router.push('/login');
            }
        })

        this.$http.get('api/races/', { headers: resource.authorizationHeader() }).then(response => {
            this.races = response.body;
        }, error => {
            if(error.status === 403){
                localStorage.removeItem('user-token');
                this.$store.commit('update_logged_in');
                this.$router.push('/login');
            }
        })
    },
    methods: {
        createCharacter(){
            if(this.characterForm.is_valid()) {
                this.$store.commit('set_loading', true);
                this.$http.post('characters/', this.characterForm.parse(), { headers: resource.authorizationHeader() }).then((response) => {
                    this.$store.commit('set_loading', false);
                    this.$store.commit('set_selected_character', response.body);
                    this.$router.push('/dashboard');
                }, (error) => {
                    this.$store.commit('set_loading', false);
                    this.characterErrors = [];
                    for(let key of Object.keys(error.body)){
                        this.characterErrors.push(error.body[key][0])
                    }
                })
            } else {
                this.characterErrors = [];
                this.characterErrors.push('Please finish filling out the form.');
            }

        }
    }
}
</script>

<style lang="scss" scoped>

</style>
