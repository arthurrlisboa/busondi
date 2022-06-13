import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { AuthService } from 'src/app/services/auth.service';
import { LocalizarLinhaService } from 'src/app/services/localizar-linha.service';
import { LocationService } from 'src/app/services/location.service';
import { FavoriteService } from '../../services/favorites.service';

@Component({
  selector: 'app-localizar-linha',
  templateUrl: './localizar-linha.component.html',
  styleUrls: ['./localizar-linha.component.css']
})
export class LocalizarLinhaComponent {

  save = false

  findForm = this.fb.group({
    line: ['', Validators.required],
    departure: ['', Validators.required]
  })

  constructor(
      private fb: FormBuilder,
      private loginService: AuthService,
      private locationservice: LocalizarLinhaService,
      private favoritesService: FavoriteService
   ) {   }

   getLogged(){
     return this.loginService.getLogged();
   }

  onSubmit() {
    let lineId = '620-01';
    let departureId = '101544000238';

    let lineName = this.findForm.controls['line'].value;
    let departureName = this.findForm.controls['departure'].value;

    if(this.save === true){
      this.favoritesService.addFavorite(lineId, departureId);
    }
  
    this.locationservice.locateLine(lineId, departureId, lineName, departureName);

    console.warn(this.findForm.value);
  }

  saveLine() : void {
      this.save = !this.save;
  }

}
