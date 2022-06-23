from backend.domain.route.route import Route

class RoutesRepositoryMock:

    def return_all_routes_from_stop_impl(self, stop_id):
        return 0
      
    def return_route_stop_by_id_impl(self, stop_id, route_id):
        return 0
    
    def return_trips_from_route_impl(self, route_id):
        return 0
    
    def return_one_route_by_id_impl(self, route_id):
        if(route_id == '609-03'):
            return Route('609-03', '609', 'Serra Verde/Santa Monica (Cid.Admin-Sentido Sta Monica)', '609-03I', '112845400545', '112845400545')
        else:
            return 'Invalid route'
    
    def return_route_conversion_impl(self, route_id):
        return 0

    def return_all_routes_impl(self):
        return 0

    def return_route_by_id_impl(self, route_id):
        return 0       