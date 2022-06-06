import { Component, OnInit } from '@angular/core';
import { LocationService } from '../../services/location.service';
import { LineQuery, FavoriteService, Favorite } from '../../services/favorites.service';

@Component({
  selector: 'app-favorite-lines',
  templateUrl: './favorite-line.component.html',
  styleUrls: ['./favorite-line.component.css']
})

export class FavoriteLineComponent implements OnInit {
  favoriteLines = new Array<Favorite>();

  constructor( private service: LocationService, private favoritesService: FavoriteService) { 
  }

  ngOnInit(): void {
    this.getFavoriteLines();
  }
  
  getFavoriteLines(){
    this.favoritesService.getFavorites().subscribe({
       next: v => {this.favoriteLines = v}
     });
  }

  removeLine(favoriteId: any): void {
    let item = this.favoriteLines.find(x => x.favorite_id == favoriteId)
    this.favoritesService.deleteFavorite(item?.route_id, item?.stop_id, item?.time);
  }

  locateLine(favoriteLine: LineQuery) {
    console.log(favoriteLine.name)
    this.service.locateLineOnRoute(favoriteLine.id, favoriteLine.name);
  }

}
