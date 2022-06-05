export interface Stop{
    stop_id: string;
    stop_lat: number;
    stop_lon: number;
    stop_name: string;
}

export interface Route {
    route_id: string;
    route_short_name: string;
    route_long_name: string;
}

export interface RouteFull {
    route_id: string;
    route_short_name: string;
    route_long_name: string;
    stops: Array<Stop>
}