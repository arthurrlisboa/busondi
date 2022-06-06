import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { LocalizarLinhaService } from '../localizar-linha/localizar-linha.service';

@Component({
  selector: 'app-localizacao-linha',
  templateUrl: './localizacao-linha.component.html',
  styleUrls: ['./localizacao-linha.component.css']
})

export class LocalizacaoLinhaComponent{

  updateForm = this.fb.group({
    departure: ['', Validators.required]
  })

  constructor(private fb: FormBuilder, private localizacaoService: LocalizarLinhaService) { 
    this.updateForm.controls['departure'].setValue(localizacaoService.getDeparture());
  }

  getLine(){
    return this.localizacaoService.getLine();
  }

  getTime(){
    return this.localizacaoService.getTime();
  }

  onSubmit() {
    let idDeparture = 'id do departure novo';
    let departureName = this.updateForm.controls['departure'].value;

    this.localizacaoService.updateLine(idDeparture, departureName);
    console.warn(this.updateForm.value);
  }

}
