import { Component, OnInit } from '@angular/core';
import { FavoriteService, Favorite } from '../../services/favorites.service';
import { AuthService } from 'src/app/services/auth.service';
import { Router } from '@angular/router';
import { LocalizarLinhaService } from 'src/app/services/localizar-linha.service';

@Component({
  selector: 'app-favorite-lines',
  templateUrl: './favorite-line.component.html',
  styleUrls: ['./favorite-line.component.css']
})

export class FavoriteLineComponent implements OnInit {
  favoriteLines = new Array<Favorite>();
  private deleted = false;

  constructor( 
    private router: Router,
    private service: LocalizarLinhaService,
    private favoritesService: FavoriteService,
    ) { 
  }

  ngOnInit(): void {
    this.getFavoriteLines();
  }
  
  getFavoriteLines(){
    this.favoritesService.getFavorites().subscribe({
      next: v => {this.favoriteLines = v.user_favorites;}
    });
  }

  reloadComponent(){
    let currentUrl = this.router.url;
    this.router.routeReuseStrategy.shouldReuseRoute = () => false;
    this.router.onSameUrlNavigation = 'reload';
    this.router.navigate([currentUrl]);
  }

  removeLine(favorite: Favorite): void {
    this.deleted = true;

    this.favoritesService.deleteFavorite(favorite)
    .subscribe( 
      () =>{
        console.log("Route removed successfully");
        this.ngOnInit();
        this.reloadComponent()
      })
  
  }

  locateLine(favoriteLine: Favorite) {
    console.log(favoriteLine.stop_name)
    this.service.locateLineOnRoute(favoriteLine.route_id, favoriteLine.route_short_name);
  }

  setConsultationParams(favoriteLine: Favorite){
    this.service.locateLine(favoriteLine.route_id, favoriteLine.stop_id, favoriteLine.route_short_name, favoriteLine.stop_name)
  }

}
