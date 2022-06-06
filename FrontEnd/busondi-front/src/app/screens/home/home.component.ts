import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { FavoriteService } from 'src/app/services/favorite.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {


  constructor(private authService: AuthService, private favoriteLinesService: FavoriteService) {
   }

  ngOnInit(): void {}

  get getLogged(){
    return this.authService.getLogged();
  }

  favoritesIsEmpty(){
      return (this.favoriteLinesService.getFavorites().length === 0)
  }

  

}
