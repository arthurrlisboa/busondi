import { Component, OnInit } from '@angular/core';

import {Inject, Injectable} from '@angular/core';
import { FavoriteService } from 'src/app/services/favorite.service';
import { LineQuery } from './LineQuery';

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

  constructor (private favoritesService: FavoriteService ) { 
  }

  ngOnInit(): void {
    console.log(this.userEmail);
  }
  
  getFavoriteLines() : LineQuery[]{
     return this.favoritesService.getFavorites();
  }

  removeLine(favoriteLine: LineQuery): void {

  }

}
