import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Route, RouteFull, Stop } from './linhas';

@Injectable({
  providedIn: 'root'
})
export class LocalizarLinhaService {
  private stopsUrl = "http://localhost:5000/stops"
  private routesUrl = "http://127.0.0.1:5000/routes"
  private time = ''
  private referencePoint = ''
  private lineName = '';
  private referencePointId = '';
  private lineId = '';

  constructor(
    private http: HttpClient
  ) { }

  getBusStops() {
    return this.http.get<Array<Stop>>(this.stopsUrl)
  }

  getRoutes() {
    return this.http.get<Array<Route>>(this.routesUrl)
  }

  getRouteStops(routId: any) {
    return this.http.get<RouteFull>(`${this.routesUrl}${routId}`)
  }

  locateLine(lineid: string, referencePointId: string, lineName: string, referencePointName: string){
    //Todo fazer request do tempo com o id do ponto e buscar no resultado, com o id da linha, o tempo que falta - formato 

    //Todo - pegar do tempo os minutos
    let horas = '10';

    //Todo - pegar do tempo os segundos
    let minutos = '30';

    this.referencePoint = referencePointName;
    this.lineName = lineName;

    this.time = horas + ' horas e ' + minutos + ' minutos';
  }

  updateLine(referencePointId: string, referencePointName: string){
      this.locateLine(this.lineId, referencePointId, this.lineName, referencePointName);
  }

  getDeparture(){
      return this.referencePoint;
  }

  getLine(){
      return this.lineName;
  }

  getTime(){
      return this.time;
  }

}

