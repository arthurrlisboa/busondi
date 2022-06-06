import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable } from 'rxjs';
import { LineQuery } from '../screens/favorite-line/LineQuery';

@Injectable({
  providedIn: 'root'
})
export class FavoriteService {
  private favoritesUrl = 'http://localhost:5000/favorites'

  favoriteLines : LineQuery[] = [
    { id: '12', name: '1404', stopId: '128371937', stopName: 'Rua geraldo magela, 150' },
    { id: '13', name: '54A', stopId: '128345937', stopName: 'Rua desenbargador joao neto, 160' },
    { id: '14', name: '54B', stopId: '12567567', stopName: 'Rua bom retiro, 176' },
    { id: '15', name: '5628', stopId: '62348889', stopName: 'Avenida Abílio machado, 67' },
  ];

  constructor(
    private http: HttpClient
  ) { }

  //getFavorites(): Observable<boolean> {
    //return this.http.get<boolean>(this.favoritesUrl);
  //}

  getFavorites() {
      return this.favoriteLines;
  }

  addFavorite(){

  }

  removeFavorites(){

  }

}

export interface Favorite {
    id: string;
    name: string;
    stopId: string;
    stopName: string; 
}