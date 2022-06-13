import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { RouteFull, Stop, StopFull } from '../screens/localizar-linha/linhas';

@Injectable({
  providedIn: 'root'
})
export class LocalizarLinhaService {
  private stopsUrl = "http://127.0.0.1:5000/stops"
  private routesUrl = "http://127.0.0.1:5000/routes"
  private time = ''
  private referencePoint = ''
  private lineName = '';
  private referencePointId = '';
  private lineId = '';
  private lineRouteId = '';
  private lineRouteName = '';

  constructor(
    private http: HttpClient
  ) { }

  getBusStops() {
    return this.http.get<Array<Stop>>(this.stopsUrl)
  }

  getRoutes() {
    return this.http.get<Array<RouteFull>>(this.routesUrl)
  }

  getRouteStops(routId: any) {
    return this.http.get<RouteFull>(`${this.routesUrl}/${routId.replace("-", "_")}`)
    // return this.http.get<RouteFull>(this.routesUrl+"/9550_01")
  }

  getStopWithBusTime(stopId: any) {
    return this.http.get<StopFull>(this.stopsUrl+"/"+stopId)
    // return this.http.get<StopFull>(this.stopsUrl+"/100446103230")
  }

  locateLine(lineid: string, referencePointId: string, lineName: string, referencePointName: string){
    //Todo fazer request do tempo com o id do ponto e buscar no resultado, com o id da linha, o tempo que falta - formato 

    //Todo - pegar do tempo os minutos
    let horas = '10';

    //Todo - pegar do tempo os segundos
    let minutos = '30';

    this.referencePointId = '';
    this.lineId = '';

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

  locateLineOnRoute(lineId: string, lineName: string){
    console.log(lineName);
    this.lineRouteId = lineId;
    this.lineRouteName = lineName
  }

  getLineRoute(){
      return this.lineRouteName;
  }

}

