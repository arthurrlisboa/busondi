import { Component, Input, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { LocalizarLinhaService } from 'src/app/services/localizar-linha.service';
import { RouteFull, StopFull } from '../localizar-linha/linhas';

@Component({
  selector: 'app-localizacao-linha',
  templateUrl: './localizacao-linha.component.html',
  styleUrls: ['./localizacao-linha.component.css']
})

export class LocalizacaoLinhaComponent implements OnInit {
  data: StopFull = {};
  routeFull: any; 
  json: any;
  line = '';
  stopId = '';
  time = '';

  updateForm = this.fb.group({
    departure: ['', Validators.required]
  })

  constructor(
    private fb: FormBuilder,
    private localizarService: LocalizarLinhaService,
    private route: ActivatedRoute,
  ) { 
  }

  updateDeparture() {
    this.localizarService.getStopWithBusTime(this.updateForm.get('departure')?.value).subscribe({
      next: (v) => {this.data = v; this.json = JSON.stringify(this.data.stop_routes);}
    })
  }

  ngOnInit() {
    this.route.queryParams.subscribe({
      next: params => {
        this.line = params['line'].toString().replace("_", "-");
        this.stopId = params['stopId'];
        this.updateForm.patchValue({
          departure: this.stopId
        })
        this.localizarService.getStopWithBusTime(this.updateForm.get('departure')?.value).subscribe({
          next: (v) => {this.data = v; this.json = JSON.stringify(this.data.stop_routes);}
        })
        this.localizarService.getRouteStops(this.line).subscribe({
          next: (v) => {this.routeFull = v;}
        })
      }
    })
    
  }

}
