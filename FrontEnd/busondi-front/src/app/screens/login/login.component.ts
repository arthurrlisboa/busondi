import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { first } from 'rxjs';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  authorized: boolean = false;
  loading: boolean = false;

  userForm = this.fb.group({
    email: ['', Validators.required],
    password: ['', Validators.required]
  })

  constructor(
    private fb: FormBuilder,
    public authService: AuthService,
    private router: Router,
  ) { }

  onSubmit() {
    this.loading = true;

    this.authService.loginUser(this.userForm.get('email')?.value, this.userForm.get('password')?.value)
      .pipe(first())
      .subscribe({
        next: (auth) => {this.authService.logUser(this.userForm.get('email')?.value); this.router.navigate(['home'])},
        error: (error) => {this.loading = false}
      });
  }

}
