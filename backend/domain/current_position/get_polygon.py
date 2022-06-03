from backend.domain.current_position.get_polygon_impl import GetPolygonImpl

class GetPolygon:
    
    def get_polygon(route_id):
        return GetPolygonImpl.get_polygon_impl(route_id)