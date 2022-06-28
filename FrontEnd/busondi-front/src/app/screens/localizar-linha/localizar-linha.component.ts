import { Component, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { first, map, Observable, startWith } from 'rxjs';
import { Route, RouteFull, Stop } from './linhas';
import { LocalizarLinhaService } from '../../services/localizar-linha.service';
import { AuthService } from 'src/app/services/auth.service';
import { FavoriteService } from '../../services/favorites.service';
import { MatOptionSelectionChange } from '@angular/material/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-localizar-linha',
  templateUrl: './localizar-linha.component.html',
  styleUrls: ['./localizar-linha.component.css']
})
export class LocalizarLinhaComponent implements OnInit {
  stopOptions = new Array<Stop>();
  lineOptions = new Array<RouteFull>();
  filteredLineOptions: Observable<RouteFull[]>;
  filteredDepartureOptions: Observable<Stop[]>;
  save = false
  private added = false
  findForm = this.fb.group({
    line: ['', Validators.required],
    departure: ['', Validators.required]
  })

  constructor(
    private fb: FormBuilder,
    private service: LocalizarLinhaService,
    private authService: AuthService,
    private favoritesService: FavoriteService,
    private router: Router,
  ) { }

  ngOnInit() {
    this.filteredLineOptions = this.findForm.controls["line"].valueChanges.pipe(
      startWith(''),
      map(value => (typeof value === 'string' ? value : value?.route_short_name)),
      map(name => (name ? this._filter(name) : this.lineOptions.slice())),
    );
    this.filteredDepartureOptions = this.findForm.controls["departure"].valueChanges.pipe(
      startWith(''),
      map(value => (typeof value === 'string' ? value : value?.stop_name)),
      map(name => (name ? this._filterDeparture(name) : this.stopOptions.slice())),
    );
    this.service.getRoutes()
      .pipe(first())
      .subscribe({
        next: (itens) => {
          this.lineOptions = itens;    
        }
      });
  }

  get getLogged(){
    return this.authService.getLogged();
  }

  private _filter(value: string): RouteFull[] {
    const filterValue = value.toLowerCase();

    let foundShort = this.lineOptions.filter(option => option.route_short_name.toLowerCase().includes(filterValue));
    let foundLong = this.lineOptions.filter(option => option.route_long_name.toLowerCase().includes(filterValue));
    return [...foundShort, ...foundLong];
  }

  private _filterDeparture(value: string): Stop[] {
    const filterValue = value.toLowerCase();
    if(this.stopOptions.length){
      let foundStop = this.stopOptions.filter(option => option.stop_name?.toLowerCase().includes(filterValue));
      return [...foundStop];
    }
    else return []
  }

  changeDeparture(event: MatOptionSelectionChange, routeId: string) {
    this.service.getRouteStops(routeId)
    .pipe(first())
    .subscribe({
      next: (itens) => {
        console.log(itens)
        this.stopOptions = itens.stops;
        console.log(this.stopOptions);       
      }
    });
  }

  onSubmit() {
    let lineId = this.findForm.controls['line'].value.route_id;
    let departureId = this.findForm.controls['departure'].value.stop_id;

    let lineName = this.findForm.controls['line'].value.route_short_name;
    let departureName = this.findForm.controls['departure'].value.stop_name;

    this.service.locateLine(lineId, departureId, lineName, departureName);

    if(this.save === true){
      this.favoritesService.addFavorite(lineId, departureId)
      .subscribe(() => console.log("Route added to favorites successfully"));
    }
    this.router.navigate(['localizar-linha/resultado'])
  }


  displayFn(route: Route) {
    return route && route.route_short_name ? route.route_short_name + " - " + route.route_long_name : ""
  }

  displayFnStop(stop: Stop) {
    return stop && stop.stop_name ? stop.stop_name : ""
  }

  saveLine() : void {
      this.save = !this.save;
  }

}