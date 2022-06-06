import { Component, OnInit } from '@angular/core';
import { DomSanitizer, SafeResourceUrl} from '@angular/platform-browser';
import { LocationService } from '../../services/location.service'

@Component({
  selector: 'app-localizacao-rota',
  templateUrl: './localizacao-rota.component.html',
  styleUrls: ['./localizacao-rota.component.css']
})
export class LocalizacaoRotaComponent implements OnInit {

  line = '';
  imgRecourse = null;

  constructor( private locationService: LocationService, private sanitizer: DomSanitizer) { 
    this.line = locationService.getLineRoute()
  }

  // image: Image;
  // imgRecourse: SafeResourceUrl;

  getImage(){
    // this.locationService.getImageRoute().subscribe(
    //   data => {
    //     this.image = data as any;
    //     this.imgRecourse = this.sanitizer.bypassSecurityTrustResourceUrl('data:image/jpg;base64,' + this.image.imageData);
    //   }
    // )
  }

  ngOnInit(): void {
    this.line = this.locationService.getLineRoute()
    this.getImage();
  }

  hasImageRecourse() : boolean{
    return this.imgRecourse !== null;
  }

}

