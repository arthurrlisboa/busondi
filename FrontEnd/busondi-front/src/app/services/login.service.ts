import { Injectable } from '@angular/core';

@Injectable()

export class LoginService {

    private logged = true;
    private name = 'Ryan';
    private email = '';

    login(email: string, password: string) :void {
        //Todo - chamada back para recuperar nome e fazer login
        this.name='Arthur'
        this.email = email;

        this.logged = true;
    }

    unlog() :void {
        this.name = '';
        this.email = '';

        //Todo - chamada back para fazer deslogar

        this.logged = false;
    }

    registerUser(name: string, email: string, password: string) :void {
        //Todo - chamada back para cadastro
    }

    getLogged() :boolean{
        return this.logged;
    }

    getName() :string{
        return this.name;
    }

    getEmail() :string{
        return this.email;
    }

}