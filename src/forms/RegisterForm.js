export class RegisterForm {
    constructor(){
        this.username = '';
        this.email = '';
        this.password = '';
        this.confirm_password = '';
    }

    clean(){
        this.username = '';
        this.email = '';
        this.password = '';
        this.confirm_password = '';
    }

    parse(){
        return {
            "username": this.username,
            "email": this.email,
            "password": this.password,
        }
    }
}
