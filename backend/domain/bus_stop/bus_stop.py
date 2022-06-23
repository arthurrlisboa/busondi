class BusStop:

    def __init__(self, stop_id, stop_name, stop_lat, stop_lon):
        self.stop_id = stop_id
        self.stop_name = stop_name
        self.stop_lat = stop_lat
        self.stop_lon = stop_lon

    def to_dict(self) -> dict:
        return {
            'stop_id': self.stop_id,
            'stop_lat' : self.stop_lat,
            'stop_lon': self.stop_lon,
            'stop_name' : self.stop_name
        }
