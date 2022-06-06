import { Component, OnInit } from '@angular/core';
import { FAVORITE_LINES } from './mock-LineQuery';
import {Inject, Injectable} from '@angular/core';
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
  favoriteLines = FAVORITE_LINES;


  constructor( ) { 
  }

  ngOnInit(): void {
    console.log(this.userEmail);
  }

  removeLine(favoriteLine: LineQuery): void {

  }

}
