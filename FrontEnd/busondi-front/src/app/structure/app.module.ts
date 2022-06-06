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
import { ToolbarBusondiComponent } from '../screens/toolbar-busondi/toolbar-busondi.component';
import { FavoriteLineComponent } from '../screens/favorite-line/favorite-line.component';
import { LocalizacaoRotaComponent } from '../screens/localizacao-rota/localizacao-rota.component';
import { FavoriteService } from '../services/favorites.service';

import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { AuthService } from '../services/auth.service';
import { HttpClientModule } from '@angular/common/http';
import { LocalizarLinhaService } from '../services/localizar-linha.service';
import { MatSelectModule } from '@angular/material/select';
import { MatAutocompleteModule } from '@angular/material/autocomplete';


@NgModule({
  declarations: [
    AppComponent,
    FavoriteLineComponent,
    HomeComponent,
    LoginComponent,
    LocalizarLinhaComponent,
    LocalizacaoLinhaComponent,
    LocalizacaoRotaComponent,
    RegisterComponent,
    DialogRegister,
    ToolbarBusondiComponent
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
    LocalizarLinhaService,
    FavoriteService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
