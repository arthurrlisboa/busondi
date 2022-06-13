import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})

export class FavoriteService {
  private favoritesUrl = 'http://127.0.0.1:5000/favorites';

  constructor(
    private http: HttpClient,
    private authService: AuthService
  ) { }

  getFavorites(){
      return this.http.get<FavoritesResponse>(this.favoritesUrl);
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
    var options = {
      body: {
        email: this.authService.getEmail(),
        route_id: id,
        stop_id: stopId
      },
    };

    this.http.post<boolean>(this.favoritesUrl, options);
  }

}

export interface Favorite {
  favorite_id: string;
  route_id: string;
  route_short_name: string;
  stop_id: string;
  stop_name: string;
  time: string;
}

export interface FavoritesResponse {
  user_favorites: Favorite[]
}