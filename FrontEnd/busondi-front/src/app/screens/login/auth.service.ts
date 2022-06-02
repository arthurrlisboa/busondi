import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private authUrl = 'login' //????

  constructor(
    private http: HttpClient
  ) { }

  authUser(email?: string, password?: string): Observable<boolean> {
    return this.http.post<boolean>(this.authUrl, {email: email, passeord: password});
  }
}
