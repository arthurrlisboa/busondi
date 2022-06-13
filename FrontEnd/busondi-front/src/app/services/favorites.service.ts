import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AuthService } from './auth.service';
import { Router } from '@angular/router';
import { EmailValidator } from '@angular/forms';
@Injectable({
  providedIn: 'root'
})

export class FavoriteService {
  private favoritesUrl = 'http://127.0.0.1:5000/favorites';

  constructor(
    private http: HttpClient,
    private authService: AuthService,
    private router: Router
  ) { }

  getFavorites(){
      var email = this.authService.getEmail()
      let headers = new HttpHeaders();
      headers = headers.append("email", email);
      return this.http.get<FavoritesResponse>(this.favoritesUrl, {headers: headers});
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
    return this.http.delete(this.favoritesUrl, options)
  }

  addFavorite(id: string, stopId: string){
    return this.http.post<boolean>(this.favoritesUrl, {email: this.authService.getEmail(), route_id: id, stop_id: stopId })
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