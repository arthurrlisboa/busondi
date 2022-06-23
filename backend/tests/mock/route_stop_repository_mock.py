from backend.database.models.routes import Routes
from backend.domain.route_stop.route_stop import RouteStop

class RouteStopRepositoryMock:

    def return_all_stops_in_route_impl(self, route_id):
        if(route_id == '609-03'):
            return [
                RouteStop('609-03', 1, None, 0.0, 18568, '10100130600640'),
                RouteStop('609-03', 1, None, 0.0, 18568, '10100446100580')
            ]
        return 'Invalid Route ID'

    def return_all_routes_from_stop_impl(self, stop_id):
        if(stop_id == '104787000120'):
            return [
                RouteStop('609-01', 43, None, 7983.46, 18401, '104787000120'),
                RouteStop('609-02', 43, None, 7983.46, 18504, '104787000120'),
                RouteStop('609-03', 45, None, 9182.09, 18612, '104787000120')
            ]
        return 'Invalid Stop ID'
      
    def return_route_stop_by_id_impl(self, stop_id, route_id):
        return 0