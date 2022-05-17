import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LocalizarLinhaComponent } from '../screens/localizar-linha/localizar-linha.component';
import { HomeComponent } from '../screens/home/home.component';
import { LoginComponent } from '../screens/login/login.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: '/home',
    pathMatch: 'full'
  },
  {
    path: 'home',
    component: HomeComponent,
  },
  {
    path: 'localizar-linha',
    component: LocalizarLinhaComponent,
  },
  {
    path: 'login',
    component: LoginComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
