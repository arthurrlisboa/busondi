import { Component, OnInit } from '@angular/core';
import { FavoriteService, Favorite } from '../../services/favorites.service';
import { AuthService } from 'src/app/services/auth.service';
import { LocalizarLinhaService } from 'src/app/services/localizar-linha.service';

@Component({
  selector: 'app-favorite-lines',
  templateUrl: './favorite-line.component.html',
  styleUrls: ['./favorite-line.component.css']
})

export class FavoriteLineComponent implements OnInit {
  favoriteLines = new Array<Favorite>();

  constructor( private service: LocalizarLinhaService, private favoritesService: FavoriteService, private authService: AuthService) { 
  }

  ngOnInit(): void {
    this.getFavoriteLines();
  }
  
  getFavoriteLines(){
    this.favoritesService.getFavorites().subscribe({
      next: v => {this.favoriteLines = v.user_favorites}
    });
  }

  removeLine(favorite: Favorite): void {
    this.favoritesService.deleteFavorite(favorite);
    this.getFavoriteLines()
  }

  locateLine(favoriteLine: Favorite) {
    console.log(favoriteLine.stop_name)
    this.service.locateLineOnRoute(favoriteLine.route_id, favoriteLine.route_short_name);
  }

  setConsultationParams(favoriteLine: Favorite){
    this.service.locateLine(favoriteLine.route_id, favoriteLine.stop_id, favoriteLine.route_short_name, favoriteLine.stop_name)
  }

}
