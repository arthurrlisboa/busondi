import { Component, Inject } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import { Router } from '@angular/router';
import { first } from 'rxjs';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  loading = false;

  registerForm = this.fb.group({
    email: ['', Validators.required],
    username: ['', Validators.required],
    password: ['', Validators.required]
  })

  constructor(
    private fb: FormBuilder,
    private dialog: MatDialog,
    private authService: AuthService,
    private router: Router,
  ) { }

  openDialogSuccess(): void {
    const dialogRef = this.dialog.open(DialogRegister, {
      width: '250px',
      data: "Conta criada com sucesso!"
    });

    dialogRef.updatePosition({ top: '10px'});

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      this.router.navigate(['login'])
    });
  }

  openDialogFailure(): void {
    const dialogRef = this.dialog.open(DialogRegister, {
      width: '250px',
      data: "Erro ao cadastrar usuário."
    });

    dialogRef.updatePosition({ top: '10px'});

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }

  onSubmit() {
    this.loading = true;

    this.authService.createUser(
      this.registerForm.get('email')?.value,
      this.registerForm.get('password')?.value,
      this.registerForm.get('username')?.value
    )
      .subscribe({
        next: (value) => {this.openDialogSuccess();},
        error: (error) => {this.openDialogFailure();}
      });
  }

}

@Component({
  selector: 'dialog-register',
  templateUrl: 'dialog-register.component.html',
})
export class DialogRegister {
  constructor(
    public dialogRef: MatDialogRef<DialogRegister>,
    @Inject(MAT_DIALOG_DATA) public text: string
  ) {}

  onNoClick(): void {
    this.dialogRef.close();
  }
    
}
