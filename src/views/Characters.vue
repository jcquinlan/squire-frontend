<template>
    <div id="characters">
        <h4 class="view-title">Characters</h4>

        <router-link to="/characters/create">
        <div class="col s12 character create-character">
            <div class="card horizontal">
                <div class="card-stacked">
                    <div class="card-content">
                        <p>New Character</p>
                    </div>
                </div>
            </div>
        </div>
        </router-link>

        <div v-for="character of characters" @click.prevent="selectCharacter(character)" class="col s12 character">
            <div class="card horizontal">
                <div class="card-stacked">
                    <div class="card-content">
                        <p>{{ character.first_name }} {{ character.last_name }}</p>
                        <p v-if="selectedCharacter == character">check!</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { resource } from '../resources';

export default {
    data () {
        return {
            characters: [],
        }
    },
    computed: {
        selectedCharacter(){
            return this.$store.state.selected_character;
        }
    },
    methods: {
        selectCharacter(character){
            this.$store.commit('set_selected_character', character);
            this.$router.push('/dashboard');
        }
    },
    created() {
        this.$store.commit('set_loading', true);
        this.$http.get('characters/', { headers: resource.authorizationHeader() }).then(response => {
            this.characters = response.body;
            this.$store.commit('set_loading', false);
        }, error => {
            if(error.status === 403){
                this.$store.commit('set_loading', false);
                localStorage.removeItem('user-token');
                this.$store.commit('update_logged_in');
                this.$router.push('/login');
            }
        });
    }
}
</script>

<style lang="scss">
@import '../variables';

    #characters {
        .character {
            cursor: pointer;
        }

        .create-character .card {
            background-color: $primary-cool;
            color: #fff;
        }

        .card-horizontal {

            .card-image {
                height: 100%;
                top: -10px;
                margin-left: -20px;
                margin-bottom: -20px;
            }
        }
    }
</style>
