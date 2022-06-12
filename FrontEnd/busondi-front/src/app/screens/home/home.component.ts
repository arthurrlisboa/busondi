import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { Favorite, FavoriteService } from '../../services/favorites.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  favoriteLines = new Array<Favorite>();


  constructor(private authService: AuthService, private favoriteLinesService: FavoriteService) {
   }

  ngOnInit(): void {
    // this.favoriteLinesService.getFavorites().subscribe({
    //   next: v => {this.favoriteLines = v}
    // });
  }

  get getLogged(){
    return this.authService.getLogged();
  }

  favoritesIsEmpty(){
      return (false)
  }

  showIntro(){
     return !this.getLogged || this.favoritesIsEmpty()
  }

  showFavorites(){
    return this.getLogged && (!this.favoritesIsEmpty())
  }

}
