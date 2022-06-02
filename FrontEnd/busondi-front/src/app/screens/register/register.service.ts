import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable } from 'rxjs';
import { SubscriptionLog } from 'rxjs/internal/testing/SubscriptionLog';


@Injectable({
  providedIn: 'root'
})
export class RegisterService {
  private registerUrl = 'users' //????

  constructor(
    private http: HttpClient
  ) { }

  createUser(email?: string, password?: string, name?: string): Observable<object> {
    return this.http.post<object>(this.registerUrl, {email: email, passeord: password, name: name});
  }
}
