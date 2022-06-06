import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { MatDialog, MatDialogRef} from '@angular/material/dialog';
import { first } from 'rxjs';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  providers: [AuthService],
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
  ) { }

  openDialog(): void {
    const dialogRef = this.dialog.open(DialogRegister, {
      width: '250px'
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
      .pipe(first())
      .subscribe({
        next: (value) => {console.warn(this.registerForm.value); this.openDialog();},
        error: (error) => {this.loading = false}
      });
  }

}

@Component({
  selector: 'dialog-register',
  templateUrl: 'dialog-register.component.html',
})
export class DialogRegister {
  constructor(
    public dialogRef: MatDialogRef<DialogRegister>
  ) {}

  onNoClick(): void {
    this.dialogRef.close();
  }
    
}
