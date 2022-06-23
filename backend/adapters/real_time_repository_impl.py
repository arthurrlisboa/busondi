import requests
import pandas as pd
import io
from time import sleep

class RealTimeRepositoryImpl:
    
    def __init__(self):
        self.real_time_url = 'https://temporeal.pbh.gov.br?param=C'

    def extract_bus_coords_from_dataframe(self, bus_data):
        bus_coords = []
        for idx, row in bus_data.iterrows():
            lat = float(row['LT'].replace(',', '.'))
            lon = float(row['LG'].replace(',', '.'))
            bus_coords.append((lon, lat))
        return bus_coords
    
    def get_real_time_bus_coords_impl(self, route_number):
        while(True):
            try:
                real_time_rsp = requests.get(self.real_time_url).content
                real_time_data = pd.read_csv(io.StringIO(real_time_rsp.decode('utf-8')), delimiter=';')
                # Columns names: ['EV', 'HR', 'LT', 'LG', 'NV', 'VL', 'NL', 'DG', 'SV', 'DT']
                real_time_data = real_time_data.rename(columns=lambda x: x.strip())
                bus_data = real_time_data.loc[real_time_data['NL'] == route_number]
                return RealTimeRepositoryImpl().extract_bus_coords_from_dataframe(bus_data)
            except:
                # HTTP Error 502: Bad Gateway
                sleep(1)