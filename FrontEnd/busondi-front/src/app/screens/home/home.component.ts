import { Component, OnInit } from '@angular/core';
import { FavoriteService } from '../../services/favorites.service';
import { LoginService } from '../../services/login.service'

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {


  constructor(private loginService: LoginService, private favoriteService: FavoriteService) {
   }

  ngOnInit(): void {}

  showIntro(){
     return !this.getLogged() || this.favoritesIsEmpty()
  }

  showFavorites(){
    return this.getLogged() && (!this.favoritesIsEmpty())
  }

  getLogged(): boolean{
    return this.loginService.getLogged();
  }

  favoritesIsEmpty(): boolean{
    return (this.favoriteService.getFavorites().length === 0)
  }

}
