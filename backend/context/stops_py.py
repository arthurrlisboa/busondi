from backend.database.models.bus_stops import BusStops
from backend.app import busondi_database, app

def get_stops():
    # TODO: Pegar lista de pontos do banco de dados e retornar no formato json
    stops = BusStops.query.all()
    dict = {}
    for i in stops:
        dict[i] = {
            'stop_lat' : i.stop_lat,
            'stop_lon': i.stop_lon,
            'stop_id' : i.stop_id,
            'stop_name' : i.stop_name
        }

    return dict