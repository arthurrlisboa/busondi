from backend.domain.repositories.routes_repository import RoutesRepository
from backend.domain.repositories.shapes_repository import ShapesRepository

import requests
import pandas as pd
import io

REAL_TIME_URL = 'https://temporeal.pbh.gov.br?param=C'

class GetMapImpl:

    def get_bus_dataframe_from_api(route_number):
        real_time_rsp = requests.get(REAL_TIME_URL).content
        real_time_data = pd.read_csv(io.StringIO(real_time_rsp.decode('utf-8')), delimiter=';')
        # Columns names: ['EV', 'HR', 'LT', 'LG', 'NV', 'VL', 'NL', 'DG', 'SV', 'DT']
        real_time_data = real_time_data.rename(columns=lambda x: x.strip())
        bus_data = real_time_data.loc[real_time_data['NL'] == route_number]
        return bus_data

    def get_bus_coords_from_api(route_number):
        bus_data = GetMapImpl.get_bus_dataframe_from_api(route_number)

        bus_coords = []
        for idx, row in bus_data.iterrows():
            lat = float(row['LT'].replace(',', '.'))
            lon = float(row['LG'].replace(',', '.'))
            bus_coords.append((lon, lat))
        return bus_coords

    def get_actual_map_impl(route_id):
        route = RoutesRepository.return_one_route_by_id(route_id)
        route_number = RoutesRepository.return_route_conversion(route_id)
        polygon_shape = ShapesRepository.return_shape_by_id(route.shape_id)

        bus_coords = GetMapImpl.get_bus_coords_from_api(route_number)
        print(bus_coords)
        return [route_number, polygon_shape]
