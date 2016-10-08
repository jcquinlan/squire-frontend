export class LoginForm {
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
