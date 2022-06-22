from backend.domain.shape.get_shape_impl import GetShapeImpl

class GetShape:
    
    def __init__(self):
        self.impl = GetShapeImpl()
    
    def get_polygon(self, route_id):
        return self.impl.get_polygon_impl(route_id)