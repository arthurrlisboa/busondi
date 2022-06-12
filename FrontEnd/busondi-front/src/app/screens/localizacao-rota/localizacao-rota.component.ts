import { Component, OnInit } from '@angular/core';
import { LocalizarLinhaService } from 'src/app/services/localizar-linha.service';
import { LocationService } from '../../services/location.service'

@Component({
  selector: 'app-localizacao-rota',
  templateUrl: './localizacao-rota.component.html',
  styleUrls: ['./localizacao-rota.component.css']
})
export class LocalizacaoRotaComponent implements OnInit {

  line = '';

  constructor( private locationService: LocalizarLinhaService) { 
    this.line = locationService.getLineRoute()
  }

  ngOnInit(): void {
    this.line = this.locationService.getLineRoute()
  }

}
