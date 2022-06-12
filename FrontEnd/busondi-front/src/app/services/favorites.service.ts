import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})

export class FavoriteService {
  private favoritesUrl = 'http://localhost:5000/favorites';

  private favoriteLines : LineQuery[] = [
    { id: '1404', name: '1404', stopId: '128371937', stopName: 'Rua geraldo magela, 150' },
    { id: '54a', name: '54 A', stopId: '128345937', stopName: 'Rua desenbargador joao neto, 160' },
    { id: '54b', name: '54 B', stopId: '12567567', stopName: 'Rua bom retiro, 176' },
    { id: '5628', name: '5628', stopId: '62348889', stopName: 'Avenida Abílio machado, 67' },
  ];

  constructor(
    private http: HttpClient,
    private authService: AuthService
  ) { }

  getFavorites() {
      return this.http.get<Favorite[]>(this.favoritesUrl);
  }

  deleteFavorite(favorite: Favorite) {
    var options = {
      body: {
        email: this.authService.getEmail(),
        route_id: favorite.route_id,
        stop_id: favorite.stop_id,
        time: favorite.time
      },
    };

    return this.http.delete(this.favoritesUrl, options);
  }

  addFavorite(id: string, stopId: string){
    this.http.post(this.favoritesUrl, {email: this.authService.getEmail(), route_id: id, stop_id: stopId});
  }

  removeFavorites( favorite: LineQuery){
    this.favoriteLines = this.favoriteLines.filter(function(value, index, arr){ 
      return value.id !== favorite.id && value.stopId !== favorite.stopId;
    });
  }

}

export interface LineQuery {
    id: string;
    name: string;
    stopId: string;
    stopName: string; 
}

export interface Favorite {
  favorite_id: string;
  route_id: string;
  route_short_name: string;
  stop_id: string;
  stop_name: string;
  time: string;
}
