import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router"
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-busondi-toolbar',
  templateUrl: './toolbar-busondi.component.html',
  styleUrls: ['./toolbar-busondi.component.css']
})
export class ToolbarBusondiComponent implements OnInit {

  constructor(
    private router: Router,
    private authService: AuthService
  ) { }

  get getLogged(){
    return this.authService.getLogged();
  }

  get getName(){
    return this.authService.getName();
  }

  ngOnInit(): void {
  }

  isCurrentPage( currentPage: string) : boolean {
    return this.router.url === currentPage
  }

  exitApp(): void {
    this.authService.logoutUser()
      .subscribe({
        next: () => (this.router.navigate(['home']))
      });
  }

}
