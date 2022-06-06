import { Component, OnInit } from '@angular/core';
import { LocationService } from '../../services/location.service';
import { LineQuery, FavoriteService } from '../../services/favorites.service';

@Component({
  selector: 'app-favorite-lines',
  templateUrl: './favorite-line.component.html',
  styleUrls: ['./favorite-line.component.css']
})

export class FavoriteLineComponent implements OnInit {

  constructor( private service: LocationService, private favoritesService: FavoriteService) { 
  }

  ngOnInit(): void {
  }

  getFavoriteLines(){
    return this.favoritesService.getFavorites();
  }

  setConsultationParams(favoriteLine: LineQuery){
    this.service.locateLine(favoriteLine.id, favoriteLine.stopId, favoriteLine.name, favoriteLine.stopName)
  }

  removeLine(favoriteLine: LineQuery): void {
    this.favoritesService.removeFavorites(favoriteLine);
  }

}
