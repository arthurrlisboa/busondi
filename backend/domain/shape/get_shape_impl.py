import shapely

class GetShapeImpl:

    def __init__(self, routes_repo, shapes_repo):
        self.routes_repo = routes_repo
        self.shapes_repo = shapes_repo
    
    def get_polygon_impl(self, route_id):
        route = self.routes_repo.return_one_route_by_id(route_id)
        polygon_shape = self.shapes_repo.return_shape_by_id(route.shape_id)
        return shapely.wkt.loads(polygon_shape)