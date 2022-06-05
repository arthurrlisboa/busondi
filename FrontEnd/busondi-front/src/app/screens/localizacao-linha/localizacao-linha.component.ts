import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-localizacao-linha',
  templateUrl: './localizacao-linha.component.html',
  styleUrls: ['./localizacao-linha.component.css']
})

export class LocalizacaoLinhaComponent{

  line = '';
  time = '';

  updateForm = this.fb.group({
    departure: ['', Validators.required]
  })

  constructor(private fb: FormBuilder) { 
    this.line = '1405';
    this.time = "15 minutos e 30 segundos";
  }

  onSubmit() {
    // TODO: Use EventEmitter with form value
    console.warn(this.updateForm.value);
  }

}
