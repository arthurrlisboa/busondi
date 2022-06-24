import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private loginUrl = 'http://127.0.0.1:5000/api/login'
  private logoutUrl = 'http://127.0.0.1:5000/api/logout'
  private usersUrl = 'http://127.0.0.1:5000/api/users'
  private logged = false;
  private name = '';
  private email = '';

  constructor(
    private http: HttpClient
  ) { }

  loginUser(email?: string, password?: string): Observable<boolean> {
    return this.http.post<boolean>(this.loginUrl, {email: email, password: password});
  }

  logUser(email: string) {
    var name = email.split("@")[0];

    this.logged = true;
    this.name = name;
    this.email = email;
  }

  logoutUser(): Observable<boolean> {
    this.logged = false;
    return this.http.post<boolean>(this.logoutUrl, {});
  }

  createUser(email?: string, password?: string, name?: string): Observable<object> {
    return this.http.post<responseMsg>(this.usersUrl, {email: email, password: password, name: name});
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

interface responseMsg {
  message: string;
}