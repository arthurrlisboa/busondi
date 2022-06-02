import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {

  registerForm = this.fb.group({
    email: ['', Validators.required],
    username: ['', Validators.required],
    password: ['', Validators.required]
  })

  constructor(private fb: FormBuilder, private dialog: MatDialog) { }

  openDialog(): void {
    const dialogRef = this.dialog.open(DialogRegister, {
      width: '250px'
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }

  onSubmit() {
    // TODO: Use EventEmitter with form value
    console.warn(this.registerForm.value);
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
