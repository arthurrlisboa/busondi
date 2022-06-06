import { Component, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { first, map, Observable, startWith } from 'rxjs';
import { Route, Stop } from './linhas';
import { LocalizarLinhaService } from '../../services/localizar-linha.service';
import { AuthService } from 'src/app/services/auth.service';
import { LocationService } from 'src/app/services/location.service';
import { FavoriteService } from '../../services/favorites.service';

@Component({
  selector: 'app-localizar-linha',
  templateUrl: './localizar-linha.component.html',
  styleUrls: ['./localizar-linha.component.css']
})
export class LocalizarLinhaComponent implements OnInit {
  stopOptions = new Array<Stop>();
  lineOptions = new Array<Route>();
  filteredLineOptions: Observable<Route[]>;
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
  ) { }

  ngOnInit() {
    this.filteredLineOptions = this.findForm.controls["line"].valueChanges.pipe(
      startWith(''),
      map(value => (typeof value === 'string' ? value : value?.route_short_name)),
      map(name => (name ? this._filter(name) : this.lineOptions.slice())),
    );
    this.service.getRoutes()
      .pipe(first())
      .subscribe({
        next: (itens) => {this.lineOptions = itens}
      });
    // this.findForm.controls["line"].valueChanges.pipe(
    //   startWith(null),
    //   map(value => this.service.getRouteStops(value)
    //     .pipe(first())
    //     .subscribe({
    //       next: (itens) => {this.stopOptions = itens.stops}
    //     })
    //   )
    // )
    // Ta errado, fazer funcionar
  }

  get getLogged(){
    return this.authService.getLogged();
  }

  private _filter(value: string): Route[] {
    const filterValue = value.toLowerCase();

    let foundShort = this.lineOptions.filter(option => option.route_short_name.toLowerCase().includes(filterValue));
    let foundLong = this.lineOptions.filter(option => option.route_long_name.toLowerCase().includes(filterValue));
    return [...foundShort, ...foundLong];
  }

  onSubmit() {
       // TODO: Use EventEmitter with form value

    let lineId = 'id qualquer prencher da lista';
    let departureId = 'id do ponto para buscar horário';

    let lineName = this.findForm.controls['line'].value;
    let departureName = this.findForm.controls['departure'].value;
  
    this.service.locateLine(lineId, departureId, lineName, departureName);

    if(this.save === true && this.added === false){
      this.favoritesService.createFavorite(lineId, departureId);
      this.added = true;
    }

    console.warn(this.findForm.value);
  }

  getRouteStops(){
    let routeId = this.findForm.get("line")?.value.route_id

    this.service.getRouteStops(routeId)
      .pipe(first())
      .subscribe({
        next: (itens) => {this.stopOptions = itens.stops}
      })
  }

  displayFn(route: Route) {
    return route && route.route_short_name ? route.route_short_name + " - " + route.route_long_name : ""
  }

  saveLine() : void {
      this.save = !this.save;
  }

}
