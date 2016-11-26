<template>
    <div id="journal">
        <h4 class="view-title">Journal - {{ selected_journal.name }}     <i v-on:click="deleteJournal()" class="material-icons delete-journal">delete_forever</i></h4>

        <div id="entries" v-if="entries">

            <div class="card horizontal">
                <div class="card-stacked">
                    <div class="card-content">
                        <div class="input-wrapper">
                            <textarea class="new-entry" type="text" v-model="entry" placeholder="Write a new journal entry."></textarea>
                            <i v-if="entry.length" v-on:click="createEntry()" class="material-icons add-entry">add</i>
                        </div>
                    </div>
                </div>
            </div>

            <div v-for="entry of entries" class="card horizontal">
                <div class="card-stacked">
                    <div class="card-content">
                        <small>{{ entry.created_at }}</small>
                        <p>{{ entry.content }} - <i>{{ entry.author }}</i></p>
                        <i v-on:click="deleteEntry(entry)" class="material-icons delete-entry">delete</i>
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
            entries: [],
            entry: '',
        }
    },
    computed: {
        selected_journal(){
            return this.$store.state.selected_journal;
        },


    },
    methods: {
        createEntry(){
            let content = this.entry.trim();

            if(content){

                let entry = {
                    created_by: this.$store.state.user.user_id,
                    journal: this.selected_journal.id,
                    content: content,
                }

                this.$http.post('entries/', entry, { headers: resource.authorizationHeader() }).then(response => {
                    this.entries.push(response.body);
                    this.entry = '';
                }, error => {
                    console.error(error);
                    if(error.status === 403){
                        localStorage.removeItem('user-token');
                        this.$store.commit('update_logged_in');
                        this.$router.push('/login');
                    }
                });
            }
        },

        deleteEntry(entry){
            this.$http.delete(`entries/${ entry.id }/`, { headers: resource.authorizationHeader() }).then(response => {
                if(response.status == 204){
                    // If item is removed successfully, remove it from the entires array
                    this.entries.splice(this.entries.findIndex((item) => item == entry), 1);
                }
            }, error => {
                if(error.status === 403){
                    localStorage.removeItem('user-token');
                    this.$store.commit('update_logged_in');
                    this.$router.push('/login');
                }
            });
        },

        deleteJournal(){
            this.$http.delete(`journals/${ this.selected_journal.id }/`, { headers: resource.authorizationHeader() }).then(response => {
                if(response.status == 204){
                    this.$router.push('/dashboard');
                }
            }, error => {
                if(error.status === 403){
                    localStorage.removeItem('user-token');
                    this.$store.commit('update_logged_in');
                    this.$router.push('/login');
                }
            });
        },

    },
    created() {
        let journal = this.$store.state.selected_journal;

        if(!journal){
            this.$router.push('/dashboard');
        } else {
            this.$http.get('entries/journal', { params: { journal_id: this.selected_journal.id }}, { headers: resource.authorizationHeader() }).then(response => {
                this.entries = response.body;
            }, error => {
                if(error.status === 403){
                    localStorage.removeItem('user-token');
                    this.$store.commit('update_logged_in');
                    this.$router.push('/login');
                }
            });
        }
    },
    destroyed(){
        this.$store.commit('set_selected_journal', null);
    }
}
</script>

<style lang="scss">
    @import '../variables';

    #journal {
        .view-title {
            position: relative;

            .delete-journal {
                position: absolute;
                right: 0;
                padding: 10px;
                opacity: 0.2;
                cursor: pointer;
                transition: 0.3s;

                &:hover {
                    opacity: 1;
                    color: #fff;
                    background-color: $primary-hot;
                }
            }
        }

        #entries {
            .new-entry {
                border: none;
                margin-bottom: 0;
                height: 100px;
            }

            .card-content {
                position: relative;

                &:hover {
                    .delete-entry {
                        display: inherit;
                    }
                }

                .delete-entry {
                    position: absolute;
                    right: 5px;
                    padding: 12px;
                    top: 15px;
                    font-size: 24px;
                    cursor: pointer;
                    opacity: 0.2;
                    transition: 0.3s;
                    display: none;

                    &:hover {
                        background-color: $primary-hot;
                        color: #fff;
                        opacity: 1;
                    }
                }
            }
        }
        .input-wrapper {
            position: relative;

            .add-entry {
                position: absolute;
                top: 0;
                right: -10px;
                font-size: 24px;
                cursor: pointer;
                padding: 12px;
                transition: 0.3s;

                &:hover {
                    background-color: $primary-cool;
                    color: #fff;
                }
            }
        }
    }
</style>
