import { Component, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { first, map, Observable, startWith } from 'rxjs';
import { Route, Stop } from './linhas';
import { LocalizarLinhaService } from './localizar-linha.service';

@Component({
  selector: 'app-localizar-linha',
  templateUrl: './localizar-linha.component.html',
  providers: [LocalizarLinhaService],
  styleUrls: ['./localizar-linha.component.css']
})
export class LocalizarLinhaComponent implements OnInit {
  stopOptions = new Array<Stop>();
  lineOptions = new Array<Route>();
  filteredLineOptions: Observable<Route[]>;
  
  findForm = this.fb.group({
    line: ['', Validators.required],
    departure: ['', Validators.required]
  })

  constructor(
    private fb: FormBuilder,
    private service: LocalizarLinhaService,
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

  private _filter(value: string): Route[] {
    const filterValue = value.toLowerCase();

    let foundShort = this.lineOptions.filter(option => option.route_short_name.toLowerCase().includes(filterValue));
    let foundLong = this.lineOptions.filter(option => option.route_long_name.toLowerCase().includes(filterValue));
    return [...foundShort, ...foundLong];
  }

  onSubmit() {
    // TODO: Use EventEmitter with form value
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

}
