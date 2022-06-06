import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private loginUrl = 'http://localhost:5000/login'
  private logoutUrl = 'http://localhost:5000/logout'
  private usersUrl = 'http://127.0.0.1:5000/users'
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
    this.logged = true;
    this.name = email;
    this.email = email;
  }

  logoutUser(): Observable<boolean> {
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