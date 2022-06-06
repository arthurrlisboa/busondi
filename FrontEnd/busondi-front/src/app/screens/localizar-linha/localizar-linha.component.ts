import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { LocationService } from 'src/app/services/location.service';
import { LoginService } from 'src/app/services/login.service';
import { FavoriteService } from '../../services/favorites.service';

@Component({
  selector: 'app-localizar-linha',
  templateUrl: './localizar-linha.component.html',
  styleUrls: ['./localizar-linha.component.css']
})
export class LocalizarLinhaComponent {

  private added = false
  save = false

  findForm = this.fb.group({
    line: ['', Validators.required],
    departure: ['', Validators.required]
  })

  constructor(
      private fb: FormBuilder,
      private loginService: LoginService,
      private locationservice: LocationService,
      private favoritesService: FavoriteService
   ) {   }

   getLogged(){
     return this.loginService.getLogged();
   }

  onSubmit() {

    let lineId = 'id qualquer prencher da lista';
    let departureId = 'id do ponto para buscar horário';

    let lineName = this.findForm.controls['line'].value;
    let departureName = this.findForm.controls['departure'].value;

    if(this.save === true && this.added === false){
      this.favoritesService.addFavorite(lineId, departureId, lineName, departureName);
      this.added = true;
    }
  
    this.locationservice.locateLine(lineId, departureId, lineName, departureName);

    console.warn(this.findForm.value);
  }

  saveLine() : void {
      this.save = !this.save;
  }

}
