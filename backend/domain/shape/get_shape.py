from domain.shape.get_shape_impl import GetShapeImpl

class GetShape:
    
    def get_polygon(route_id):
        return GetShapeImpl.get_polygon_impl(route_id)