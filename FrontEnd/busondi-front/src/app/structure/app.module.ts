import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { MatSliderModule } from '@angular/material/slider';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatButtonModule } from '@angular/material/button';
import { MatButtonToggleModule}  from '@angular/material/button-toggle';
import { MatDividerModule } from '@angular/material/divider';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatDialogModule } from '@angular/material/dialog';


import { HomeComponent } from '../screens/home/home.component';
import { LocalizarLinhaComponent } from '../screens/localizar-linha/localizar-linha.component';
import { LocalizacaoLinhaComponent } from '../screens/localizacao-linha/localizacao-linha.component';
import { LoginComponent } from '../screens/login/login.component';
import { RegisterComponent } from '../screens/register/register.component';
import { DialogRegister }  from '../screens/register/register.component';
import { ToolbarUnloggedComponent } from '../screens/toolbar-unlogged/toolbar-unlogged.component';

import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { AuthService } from '../screens/login/auth.service';
import { HttpClientModule } from '@angular/common/http';
import { RegisterService } from '../screens/register/register.service';
import { LocalizarLinhaService } from '../screens/localizar-linha/localizar-linha.service';
import { MatSelectModule } from '@angular/material/select';
import { MatAutocompleteModule } from '@angular/material/autocomplete';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LoginComponent,
    LocalizarLinhaComponent,
    LocalizacaoLinhaComponent,
    RegisterComponent,
    DialogRegister,
    ToolbarUnloggedComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    MatSliderModule,
    MatToolbarModule,
    MatIconModule,
    MatSidenavModule,
    MatButtonModule,
    MatButtonToggleModule,
    MatDividerModule,
    MatInputModule,
    MatSelectModule,
    MatFormFieldModule,
    MatDialogModule,
    HttpClientModule,
    MatAutocompleteModule
  ],
  providers: [
    AuthService,
    RegisterService,
    LocalizarLinhaService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
