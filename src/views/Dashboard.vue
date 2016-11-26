<template>
    <div id="characters">

        <h4 class="view-title">{{ selected_character.first_name }} {{ selected_character.last_name }}
            <small class="character-level">
                <input type="text" v-model="selected_character.experience"
                                    v-on:change="updateCharacter"> XP
            </small>
            <small class="character-level">Level {{ selected_character.level }}</small>
            <small class="health">
                <input type="text" align="right" v-on:change="updateCharacter" v-model="selected_character.current_hitpoints"> / {{ selected_character.max_hitpoints }}
                <i class="health-icon material-icons">healing</i>
            </small>
        </h4>

        <div class="stats">
            <table>
                <thead>
                    <tr>
                      <th>Strength</th>
                      <th>Dexterity</th>
                      <th>Constitution</th>
                      <th>Intelligence</th>
                      <th>Charisma</th>
                      <th>Wisdom</th>
                    </tr>
                </thead>

                <tbody>
                    <tr>
                        <td><input class="attribute" type="text" v-model="selected_character.strength" v-on:change="updateCharacter">( + {{ selected_character.strength_modifier }} )</td>
                        <td><input class="attribute" type="text" v-model="selected_character.dexterity" v-on:change="updateCharacter">( + {{ selected_character.dexterity_modifier }} )</td>
                        <td><input class="attribute" type="text" v-model="selected_character.constitution" v-on:change="updateCharacter">( + {{ selected_character.constitution_modifier }} )</td>
                        <td><input class="attribute" type="text" v-model="selected_character.intelligence" v-on:change="updateCharacter">( + {{ selected_character.intelligence_modifier }} )</td>
                        <td><input class="attribute" type="text" v-model="selected_character.charisma" v-on:change="updateCharacter">( + {{ selected_character.charisma_modifier }} )</td>
                        <td><input class="attribute" type="text" v-model="selected_character.wisdom" v-on:change="updateCharacter">( + {{ selected_character.wisdom_modifier }} )</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="row">
            <div class="col m6">
                <div class="background">
                    <h5>Backstory</h5>
                    <textarea v-model="selected_character.backstory" v-on:change="updateCharacter" placeholder="Add a backstory." class="backstory"></textarea>
                </div>
            </div>

            <div class="col m6">
                <div v-if="journals">
                    <div class="row journal-section">
                        <h5> Journals</h5>
                        <div class="journals">
                            <div v-for="journal of journals" @click="selectJournal(journal)" class="journal col s12 m3 l3">
                                <div class="card">
                                    <div class="card-content">
                                        <span class="card-title">
                                            {{ journal.name }}
                                            <small class="entry-count">
                                                {{ journal.num_of_entries }}
                                                {{ journal.num_of_entries > 1 ? 'posts' : 'post' }}
                                            </small>
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <a class="btn-floating btn-large waves-effect waves-light red delete-character" @click="modalOpen = true">
            <i class="material-icons">delete_forever</i>
        </a>
        <delete-character-modal v-if="modalOpen" v-on:closeModal="modalOpen = false">
            <h5 slot="header">Delete Character?</h5>
            <p slot="body">This cannot be undone.</p>
            <button slot="footer" class="waves-effect waves-light btn red" @click="deleteCharacter"><i class="material-icons left">delete_forever</i>Delete</button>
        </delete-character-modal>


    </div>
</template>

<script>
import { resource } from '../resources';
import DeleteCharacterModal from '../components/Modal';

export default {
    data () {
        return {
            journals: [],
            characterError: '',
            modalOpen: false,
        }
    },
    computed: {
        selected_character(){
            return this.$store.state.selected_character;
        }
    },
    methods: {
        selectJournal(journal){
            this.$store.commit('set_selected_journal', journal);
            this.$router.push('/journal')
        },

        updateCharacter(){
            this.$store.commit('set_loading', true);
            this.$http.put(`characters/${ this.selected_character.id}/`, this.selected_character, { headers: resource.authorizationHeader() }).then(response => {
                this.$store.commit('set_loading', false);
                this.$store.commit('set_selected_character', response.body)
            },
            error => {
                this.$store.commit('set_loading', false);
                this.characterError = error.body;
            })
        },

        deleteCharacter(){
            this.$store.commit('set_loading', true);
            this.$http.delete(`characters/${ this.selected_character.id}/`, { headers: resource.authorizationHeader() }).then(response => {
                this.$store.commit('set_loading', false);
                this.$router.push('/characters');
            },
            error => {
                this.$store.commit('set_loading', false);
                this.characterError = error.body;
            })
        }
    },
    created() {
        let character = this.$store.state.selected_character;

        if(!character){
            this.$router.push('/characters');
        } else {
            this.$http.get('journals/character/', { params: { character_id: character.id }}, { headers: resource.authorizationHeader() }).then(response => {
                this.journals = response.body;
            }, error => {
                if(error.status === 403){
                    localStorage.removeItem('user-token');
                    this.$store.commit('update_logged_in');
                    this.$router.push('/login');
                }
            });
        }
    },
    components: {
        DeleteCharacterModal,
    }
}
</script>

<style lang="scss">
@import '../variables';

    #characters {
        .character-level {
            margin-left: 20px;
            font-size: 18px;
            opacity: 0.6;

            input {
                width: 80px;
                border: none;
                font-size: 20px;
                text-align: right;
            }
        }
        .health {
            position: relative;
            float: right;
            font-weight: 100;

            input {
                width: 50px;
                border: none;
                font-size: 25px;
                text-align: right;
            }

            .health-icon {
                color: maroon;
                margin-left: 5px;
                position: relative;
                top: 3px;
            }

        }
        .stats {
            .attribute {
                width: 25px;
                border: none;
                font-size: 18px;
            }
        }
        .backstory {
            min-height: 200px;
        }
        .journals {
            display: -webkit-flex;
            display: -ms-flexbox;
            display: flex;

            -webkit-flex-wrap: wrap;
            -ms-flex-wrap: wrap;
            flex-wrap: wrap;

            flex-direction: row;

            .journal {
                cursor: pointer;
                display: -webkit-flex;
                display: -ms-flexbox;
                display: flex;
                flex: 1 0 auto;

                .card {
                    width: 100%;
                    .card-content {
                        padding: 10px 0;
                        .card-title {
                            line-height: normal;
                            padding: 10px 0;
                            font-size: 20px;

                            .entry-count {
                                float: right;
                                margin-top: 3px;
                            }
                        }
                    }
                }
            }
        }
        .card-horizontal {
            .card-image {
                height: 100%;
                top: -10px;
                margin-left: -20px;
                margin-bottom: -20px;
            }
        }
        .delete-character {
            position: absolute;
            bottom: 100px;
            right: 30px;
        }
    }
</style>
