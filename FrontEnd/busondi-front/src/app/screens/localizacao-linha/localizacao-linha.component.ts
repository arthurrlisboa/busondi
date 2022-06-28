import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { first, map, Observable, startWith } from 'rxjs';
import { LocalizarLinhaService } from 'src/app/services/localizar-linha.service';

@Component({
  selector: 'app-localizacao-linha',
  templateUrl: './localizacao-linha.component.html',
  styleUrls: ['./localizacao-linha.component.css']
})

export class LocalizacaoLinhaComponent implements OnInit{
  stopOptions = new Array<Stop>();
  filteredDepartureOptions: Observable<Stop[]>;
  updateForm = this.fb.group({
    departure: ['', Validators.required]
  })

  constructor(private fb: FormBuilder, private locationService: LocalizarLinhaService) { 
    this.updateForm.controls['departure'].setValue({stop_name: locationService.getDeparture(), stop_id: locationService.getDepartureId()});
  }

  ngOnInit(): void {
    this.locationService.getRouteStops(this.locationService.getLineId())
      .pipe(first())
      .subscribe({
        next: (itens) => {
          this.stopOptions = itens.stops
        }
      })

    this.filteredDepartureOptions = this.updateForm.controls["departure"].valueChanges.pipe(
      startWith(''),
      map(value => (typeof value === 'string' ? value : value?.stop_name)),
      map(name => (name ? this._filterDeparture(name) : this.stopOptions.slice())),
    );
  }

  private _filterDeparture(value: string): Stop[] {
    const filterValue = value.toLowerCase();
    if(this.stopOptions.length){
      let foundStop = this.stopOptions.filter(option => option.stop_name?.toLowerCase().includes(filterValue));
      return [...foundStop];
    }
    else return []
  }

  displayFnStop(stop: Stop) {
    return stop && stop.stop_name ? stop.stop_name : ""
  }

  getLine(){
    return this.locationService.getLine();
  }

  getTime(){
    return this.locationService.getTime();
  }

  onSubmit() {
    let departureId = this.updateForm.controls['departure'].value.stop_id;
    let departureName = this.updateForm.controls['departure'].value.stop_name;

    this.locationService.updateLine(departureId, departureName);
    console.warn(this.updateForm.value);
  }
}


export interface Stop{
  stop_id?: string;
  stop_lat?: number;
  stop_lon?: number;
  stop_name?: string;
}