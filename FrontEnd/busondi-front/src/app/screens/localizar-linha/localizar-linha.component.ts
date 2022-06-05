import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
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

  constructor(private fb: FormBuilder, private loginService: LoginService) {
   }

   getLogged(){
     return this.loginService.getLogged();
   }

  onSubmit() {
    // TODO: Use EventEmitter with form value
    console.warn(this.findForm.value);
  }

  saveLine() : void {
      this.save = !this.save;
  }

}
