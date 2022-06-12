import { Component, OnInit } from '@angular/core';
import { LocationService } from '../../services/location.service';
import { LineQuery, FavoriteService, Favorite } from '../../services/favorites.service';
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
    //this.favoritesService.getFavorites().subscribe({
    //   next: v => {this.responseToFavorite(v)}
     //});

    return this.responseToFavorite('teste')
  }

  responseToFavorite(response: any){
    this.favoriteLines = [
      { favorite_id: '1', route_id: '1404', route_short_name: '1404', stop_id: '128371937', stop_name: 'Rua geraldo magela, 150', time: '12:00:00' },
      { favorite_id: '2', route_id: '54a', route_short_name: '54 A', stop_id: '128345937', stop_name: 'Rua desenbargador joao neto, 160' , time: '12:00:00'},
      { favorite_id: '3', route_id: '54b', route_short_name: '54 B', stop_id: '12567567', stop_name: 'Rua bom retiro, 176', time: '12:00:00' },
      { favorite_id: '4', route_id: '5628', route_short_name: '5628', stop_id: '62348889', stop_name: 'Avenida Abílio machado, 67', time: '12:00:00' },
    ];
  
    return this.favoriteLines;
  }

  removeLine(favoriteId: any): void {
    let item = this.favoriteLines.find(x => x.favorite_id == favoriteId)
    this.favoritesService.deleteFavorite(item?.route_id, item?.stop_id, item?.time);
  }

  locateLine(favoriteLine: Favorite) {
    console.log(favoriteLine.stop_name)
    this.service.locateLineOnRoute(favoriteLine.route_id, favoriteLine.route_short_name);
  }

}
