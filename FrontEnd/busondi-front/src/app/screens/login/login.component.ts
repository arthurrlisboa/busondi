import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { first } from 'rxjs';
import { AuthService } from './auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  providers: [AuthService],
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  authorized: boolean = false;
  loading: boolean = false;

  userForm = this.fb.group({
    username: ['', Validators.required],
    password: ['', Validators.required]
  })

  constructor(
    private fb: FormBuilder,
    private authService: AuthService
  ) { }

  onSubmit() {
    this.loading = true;

    this.authService.authUser(this.userForm.get('username')?.value, this.userForm.get('password')?.value)
      .pipe(first())
      .subscribe({
        next: (auth) => {this.authorized =  auth},
        error: (error) => {this.loading = false}
      });
  }

}
