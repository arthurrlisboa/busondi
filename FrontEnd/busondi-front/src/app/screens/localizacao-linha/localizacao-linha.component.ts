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
  }

  onSubmit() {
    // TODO: Use EventEmitter with form value
    console.warn(this.updateForm.value);
  }

  getLine(){
    return this.localizacaoService.getLine();
  }

  getTime(){
    return this.localizacaoService.getTime();
  }

}
