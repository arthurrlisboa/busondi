import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Route, RouteFull, Stop } from './linhas';

@Injectable({
  providedIn: 'root'
})
export class LocalizarLinhaService {
  private stopsUrl = "http://localhost:5000/stops"
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
    return this.http.get<RouteFull>(`${this.routesUrl}${routId}`)
  }

}
