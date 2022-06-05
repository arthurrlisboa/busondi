import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { LoginService } from 'src/app/services/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  userForm = this.fb.group({
    email: ['', Validators.required],
    password: ['', Validators.required]
  })

  constructor(private fb: FormBuilder, private loginService: LoginService) { }

  submitForm() {
    let email = this.userForm.controls['email'].value;
    let password = this.userForm.controls['password'].value;;

    this.loginService.login(email, password)
    console.warn(this.userForm.value);
  }

}
