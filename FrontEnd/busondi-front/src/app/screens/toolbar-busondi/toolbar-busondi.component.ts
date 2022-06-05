import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router"

@Component({
  selector: 'app-busondi-toolbar',
  templateUrl: './toolbar-busondi.component.html',
  styleUrls: ['./toolbar-busondi.component.css']
})
export class ToolbarBusondiComponent implements OnInit {

  logged = false
  name = ''

  constructor(private router: Router) {
    this.logged = true;
    this.name = 'Arthur';
   }

  ngOnInit(): void {
  }

  isCurrentPage( currentPage: string) : boolean {
    return this.router.url === currentPage
  }

  exitApp(): void {
    this.router.navigate(['home'])
    this.logged = false
  }

}
