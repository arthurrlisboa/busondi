import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Route, RouteFull, Stop, StopFull } from '../screens/localizar-linha/linhas';

@Injectable({
  providedIn: 'root'
})
export class LocalizarLinhaService {
  private stopsUrl = "http://127.0.0.1:5000/stops"
  private routesUrl = "http://127.0.0.1:5000/routes"

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
    return this.http.get<RouteFull>(`${this.routesUrl}/${routId.replace("-", "_")}`)
    // return this.http.get<RouteFull>(this.routesUrl+"/9550_01")
  }

  getStopWithBusTime(stopId: any) {
    return this.http.get<StopFull>(this.stopsUrl+"/"+stopId)
    // return this.http.get<StopFull>(this.stopsUrl+"/100446103230")
  }

}
