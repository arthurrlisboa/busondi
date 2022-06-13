import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { LocalizarLinhaService } from 'src/app/services/localizar-linha.service';

@Component({
  selector: 'app-localizacao-linha',
  templateUrl: './localizacao-linha.component.html',
  styleUrls: ['./localizacao-linha.component.css']
})

export class LocalizacaoLinhaComponent{

  updateForm = this.fb.group({
    departure: ['', Validators.required]
  })

  constructor(private fb: FormBuilder, private locationService: LocalizarLinhaService) { 
    this.updateForm.controls['departure'].setValue(locationService.getDeparture());
  }

  getLine(){
    return this.locationService.getLine();
  }

  getTime(){
    return this.locationService.getTime();
  }

  onSubmit() {
    let idDeparture = 'id do departure novo';
    let departureName = this.updateForm.controls['departure'].value;

    this.locationService.updateLine(idDeparture, departureName);
    console.warn(this.updateForm.value);
  }
}
