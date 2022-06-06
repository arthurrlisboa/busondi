import { Component, OnInit } from '@angular/core';
import {Inject, Injectable} from '@angular/core';
import { LocationService } from '../../services/location.service';
import { Favorite, FavoriteService } from '../../services/favorites.service';

@Component({
  selector: 'app-favorite-lines',
  templateUrl: './favorite-line.component.html',
  styleUrls: ['./favorite-line.component.css']
})

@Injectable({
  providedIn: 'root'
})

export class FavoriteLineComponent implements OnInit {

  constructor( private service: LocationService, private favoritesService: FavoriteService) { 
  }

  ngOnInit(): void {
  }

  getLines() : Favorite[]{
    return this.favoritesService.getFavorites();
  }

  setConsultationParams(favoriteLine: Favorite){
    this.service.locateLine(favoriteLine.id, favoriteLine.stopId, favoriteLine.name, favoriteLine.stopName)
  }

  removeLine(favoriteLine: Favorite): void {
    this.favoritesService.removeFavorites(favoriteLine);
  }

}
