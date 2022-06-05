import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router"
import { LoginService } from 'src/app/services/login.service';

@Component({
  selector: 'app-busondi-toolbar',
  templateUrl: './toolbar-busondi.component.html',
  styleUrls: ['./toolbar-busondi.component.css']
})
export class ToolbarBusondiComponent implements OnInit {

  constructor(private router: Router, private loginService: LoginService) { }

  getLogged(){
    return this.loginService.getLogged();
  }

  getName(){
    return this.loginService.getName();
  }

  ngOnInit(): void {
  }

  isCurrentPage( currentPage: string) : boolean {
    return this.router.url === currentPage
  }

  exitApp(): void {
    this.loginService.unlog();
    this.router.navigate(['home'])
  }

}
