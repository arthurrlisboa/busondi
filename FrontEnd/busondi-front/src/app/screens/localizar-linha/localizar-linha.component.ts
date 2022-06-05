import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-localizar-linha',
  templateUrl: './localizar-linha.component.html',
  styleUrls: ['./localizar-linha.component.css']
})
export class LocalizarLinhaComponent {

  save = false
  logged = true

  findForm = this.fb.group({
    line: ['', Validators.required],
    departure: ['', Validators.required]
  })

  constructor(private fb: FormBuilder) { }

  onSubmit() {
    // TODO: Use EventEmitter with form value
    console.warn(this.findForm.value);
  }

  saveLine() : void {
      this.save = !this.save;
  }

}
