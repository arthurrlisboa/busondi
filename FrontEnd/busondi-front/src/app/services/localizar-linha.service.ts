import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { RouteFull, Stop, StopFull } from '../screens/localizar-linha/linhas';

@Injectable({
  providedIn: 'root'
})
export class LocalizarLinhaService {
  private stopsUrl = "http://localhost:5000/stops"
  private routesUrl = "http://localhost:5000/routes"
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
    return this.http.get<RouteFull>(`${this.routesUrl}/${routId}`)
    // return this.http.get<RouteFull>(this.routesUrl+"/9550_01")
  }

  getStopWithBusTime(stopId: any) {
    return this.http.get<RouteInfoResponse>(this.stopsUrl+"/"+stopId)
  }

  locateLine(lineid: string, referencePointId: string, lineName: string, referencePointName: string){
    this.referencePoint = referencePointName;
    this.lineName = lineName;
    this.referencePointId = referencePointId;
    this.lineId = lineid;

    this.referencePoint = referencePointName;

    this.getStopWithBusTime(referencePointId).subscribe({
      next: v => { this.getLineDepartureTime(v.stop_routes, lineName); console.log(v)}
    });
  }

  getLineDepartureTime(routes: RouteInfo[], lineName: String){
    routes = routes.filter(function(obj) {return obj.route_name === lineName});

    if (routes.length > 0){
      console.log(routes)
      console.log(`Usou o nome ${lineName} para fazer a busca`)
      let routeInfo = routes[0]
      let timeArray = routeInfo.time.split(":")
      this.time = timeArray[0] + ' horas e ' + timeArray[1] + ' minutos';
    }

    else{
      //Todo - pegar do tempo os minutos
      let horas = '10';
      //Todo - pegar do tempo os segundos
      let minutos = '30';

      this.time = horas + ' horas e ' + minutos + ' minutos';
    }

  }

  updateLine(referencePointId: string, referencePointName: string){
      this.locateLine(this.lineId, referencePointId, this.lineName, referencePointName);
  }

  getDeparture(){
      return this.referencePoint;
  }

  getDepartureId(){
    return this.referencePointId;
}

  getLine(){
      return this.lineName;
  }

  getLineId(){
    return this.lineId;
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
export interface RouteInfo {
  route_id: string,
  route_name: string,
  time: string
}
export interface RouteInfoResponse {
  stop_routes: RouteInfo[]
}

