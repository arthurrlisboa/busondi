import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { LocationService } from 'src/app/services/location.service';
import { LoginService } from 'src/app/services/login.service';

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

  constructor(private fb: FormBuilder, private loginService: LoginService, private locationservice: LocationService) {
   }

   getLogged(){
     return this.loginService.getLogged();
   }

  onSubmit() {
    // TODO: Use EventEmitter with form value
    let lineId = 'id qualquer prencher da lista';
    let departureId = 'id do ponto para buscar horário';

    let lineName = this.findForm.controls['line'].value;
    let departureName = this.findForm.controls['departure'].value;
  
    this.locationservice.locateLine(lineId, departureId, lineName, departureName);

    console.warn(this.findForm.value);
  }

  saveLine() : void {
      this.save = !this.save;
  }

}
