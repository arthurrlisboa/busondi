import requests
import pandas as pd
import io
from time import sleep

REAL_TIME_URL = 'https://temporeal.pbh.gov.br?param=C'

class RealTimeRepositoryImpl:

    def extract_bus_coords_from_dataframe(bus_data):
        bus_coords = []
        for idx, row in bus_data.iterrows():
            lat = float(row['LT'].replace(',', '.'))
            lon = float(row['LG'].replace(',', '.'))
            bus_coords.append((lon, lat))
        return bus_coords
    
    def get_real_time_bus_coords_impl(route_number):
        while(True):
            try:
                real_time_rsp = requests.get(REAL_TIME_URL).content
                real_time_data = pd.read_csv(io.StringIO(real_time_rsp.decode('utf-8')), delimiter=';')
                # Columns names: ['EV', 'HR', 'LT', 'LG', 'NV', 'VL', 'NL', 'DG', 'SV', 'DT']
                real_time_data = real_time_data.rename(columns=lambda x: x.strip())
                bus_data = real_time_data.loc[real_time_data['NL'] == route_number]
                return RealTimeRepositoryImpl.extract_bus_coords_from_dataframe(bus_data)
            except:
                # HTTP Error 502: Bad Gateway
                sleep(1)