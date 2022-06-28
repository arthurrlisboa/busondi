from backend.api.api_connection import APIConnection

class RealTimeRepositoryImpl:

    def extract_bus_coords(self, bus_data):
        bus_coords = []
        for idx, row in bus_data.iterrows():
            lat = float(row['LT'].replace(',', '.'))
            lon = float(row['LG'].replace(',', '.'))
            bus_coords.append((lon, lat))
        return bus_coords

    def get_real_time_bus_coords_impl(self, route_number):
        with APIConnection() as connection:
            real_time_data = connection.get_data()
        bus_data = real_time_data.loc[real_time_data['NL'] == route_number]
        return self.extract_bus_coords(bus_data)