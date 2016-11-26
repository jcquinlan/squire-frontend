export class CreateCharacterForm {
    constructor(){
        this.first_name = '';
        this.last_name = '';
        this.class_type = '';
        this.race = '';
        this.background = '';
        this.max_hitpoints = '';
        this.armor_class = '';
    }

    clean(){
        this.first_name = '';
        this.last_name = '';
        this.class_type = '';
        this.race = '';
        this.background = '';
        this.max_hitpoints = '';
        this.armor_class = '';
    }

    parse(){
        return {
            "first_name": this.first_name,
            "last_name": this.last_name,
            "class_type": this.class_type,
            "race": this.race,
            "background": this.background,
            "max_hitpoints": this.max_hitpoints,
            "armor_class": this.armor_class,
        }
    }

    is_valid(){
        for(let key of Object.keys(this)){
            if(key != 'undefined' && !this[key]) return false;
        }
        return true;
    }
}
