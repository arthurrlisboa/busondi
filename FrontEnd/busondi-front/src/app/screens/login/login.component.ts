import { Component, Inject } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { first } from 'rxjs';
import { AuthService } from '../../services/auth.service';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';

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
    private dialog: MatDialog,
    public authService: AuthService,
    private router: Router,
  ) { }

  openDialogFailure(): void {
    const dialogRef = this.dialog.open(DialogLogin, {
      width: '250px',
      data: "Erro ao realizar o login. Tente novamente"
    });

    dialogRef.updatePosition({ top: '10px'});

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }

  onSubmit() {
    this.loading = true;

    this.authService.loginUser(this.userForm.get('email')?.value, this.userForm.get('password')?.value)
      .pipe(first())
      .subscribe({
        next: (auth) => {this.authService.logUser(this.userForm.get('email')?.value); this.router.navigate(['home'])},
        error: (error) => {this.loading = false; this.openDialogFailure()}
      });
  }

}

@Component({
  selector: 'dialog-login',
  templateUrl: 'dialog-login.component.html',
})
export class DialogLogin {
  constructor(
    public dialogRef: MatDialogRef<DialogLogin>,
    @Inject(MAT_DIALOG_DATA) public text: string
  ) {}

  onNoClick(): void {
    this.dialogRef.close();
  }
    
}
