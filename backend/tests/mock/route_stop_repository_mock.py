from backend.domain.route_stop.route_stop import RouteStop

class RouteStopRepositoryMock:

    def return_all_stops_in_route_impl(self, route_id):
        if(route_id == '609-03'):
            return [
                RouteStop('609-03', 1, None, 0.0, 18568, '10100130600640'),
                RouteStop('609-03', 1, None, 0.0, 18568, '10100446100580')
            ]
        else:
            return 'Invalid Route ID'