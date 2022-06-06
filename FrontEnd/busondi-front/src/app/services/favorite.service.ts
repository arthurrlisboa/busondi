import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class FavoriteService {
  private favoritesUrl = 'http://localhost:5000/favorites'

  constructor(
    private http: HttpClient
  ) { }

  getFavorites(): Observable<boolean> {
    return this.http.get<boolean>(this.favoritesUrl);
  }

}

export interface Favorite {
    id: string;
    name: string;
    stopId: string;
    stopName: string; 
}