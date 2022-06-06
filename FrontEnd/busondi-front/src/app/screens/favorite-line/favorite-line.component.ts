import { Component, OnInit } from '@angular/core';
import { FAVORITE_LINES } from './mock-LineQuery';
import {Inject, Injectable} from '@angular/core';
import { LineQuery } from './LineQuery';
import { LocationService } from '../../services/location.service';

@Component({
  selector: 'app-favorite-lines',
  templateUrl: './favorite-line.component.html',
  styleUrls: ['./favorite-line.component.css']
})

@Injectable({
  providedIn: 'root'
})

export class FavoriteLineComponent implements OnInit {

  userEmail = '';
  favoriteLines = FAVORITE_LINES;


  constructor( private service: LocationService) { 
  }

  ngOnInit(): void {
    console.log(this.userEmail);
  }

  setConsultationParams(favoriteLine: LineQuery){
    this.service.locateLine(favoriteLine.id, favoriteLine.stopId, favoriteLine.name, favoriteLine.stopName)
  }

  removeLine(favoriteLine: LineQuery): void {

  }

}
