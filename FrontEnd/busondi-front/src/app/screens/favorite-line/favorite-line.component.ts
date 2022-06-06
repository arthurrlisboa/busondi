import { Component, OnInit } from '@angular/core';
import { LocationService } from '../../services/location.service';
import { LineQuery, FavoriteService } from '../../services/favorites.service';

@Component({
  selector: 'app-favorite-lines',
  templateUrl: './favorite-line.component.html',
  styleUrls: ['./favorite-line.component.css']
})

export class FavoriteLineComponent implements OnInit {

  favoriteLines  : LineQuery[] = [
    { id: '1404', name: '1404', stopId: '128371937', stopName: 'Rua geraldo magela, 150' },
    { id: '54a', name: '54 A', stopId: '128345937', stopName: 'Rua desenbargador joao neto, 160' },
    { id: '54b', name: '54 B', stopId: '12567567', stopName: 'Rua bom retiro, 176' },
    { id: '5628', name: '5628', stopId: '62348889', stopName: 'Avenida Abílio machado, 67' },
  ];

  constructor( private service: LocationService, private favoritesService: FavoriteService) { 
  }

  ngOnInit(): void {
  }

  setConsultationParams(favoriteLine: LineQuery){
    this.service.locateLine(favoriteLine.id, favoriteLine.stopId, favoriteLine.name, favoriteLine.stopName)
  }

  removeLine(favoriteLine: LineQuery): void {
    this.favoritesService.removeFavorites(favoriteLine);
  }

}
