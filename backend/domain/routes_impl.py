from backend.domain.repository import Repository

class RoutesImpl:

    route_id = ''
    route_short_name = ''
    route_long_name = ''
    shape_id = ''
    initial_stop_id = ''
    final_stop_id = ''

    def __init__(self, route_id, route_short_name=None, route_long_name=None, shape_id=None, initial_stop_id=None, final_stop_id=None):
        self.route_id = route_id

        if(route_short_name is None):
            self.route_short_name = ''
        else:
            self.route_short_name = route_short_name

        if(route_long_name is None):
            self.route_long_name = ''
        else:
            self.route_long_name = route_long_name

        if(shape_id is None):
            self.shape_id = ''
        else:
            self.shape_id = shape_id

        if(initial_stop_id is None):
            self.initial_stop_id = ''
        else:
            self.initial_stop_id = initial_stop_id

        if(final_stop_id is None):
            self.final_stop_id = ''
        else:
            self.final_stop_id = final_stop_id

    def get_routes_from_stop(stop_id):
        stop_routes_list = []
        all_routes_from_stop = Repository.get_routes_from_stop_repo(stop_id)
        for entry in all_routes_from_stop:
            stop_routes_list.append([entry.route_stop_id, RoutesImpl(entry.route_id)])
        return stop_routes_list