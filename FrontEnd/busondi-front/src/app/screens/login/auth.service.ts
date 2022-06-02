import { HttpClient, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable } from 'rxjs';
import { SubscriptionLog } from 'rxjs/internal/testing/SubscriptionLog';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private authUrl = 'login' //????

  constructor(
    private http: HttpClient
  ) { }

  authUser(): Observable<boolean> {
    return this.http.get<boolean>(this.authUrl);
  }
}
