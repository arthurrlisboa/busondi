import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-localizar-linha',
  templateUrl: './localizar-linha.component.html',
  styleUrls: ['./localizar-linha.component.css']
})
export class LocalizarLinhaComponent {
  findForm = this.fb.group({
    line: ['', Validators.required],
    departure: ['', Validators.required],
    time: ['', Validators.required]
  })

  constructor(private fb: FormBuilder) { }

  onSubmit() {
    // TODO: Use EventEmitter with form value
    console.warn(this.findForm.value);
  }

}
