from plotly import graph_objects as go
import numpy as np

class DrawMapImpl:
    def draw_map_route_stops_bus_position_impl(polygon, bus_coord, stops_coord):
        poly_lon, poly_lat = polygon.exterior.coords.xy
        bus_lon, bus_lat = DrawMapImpl.get_lon_lat_from_tuples_list(bus_coord)
        stops_lon, stops_lat = DrawMapImpl.get_lon_lat_from_tuples_list(stops_coord)

        center_lon = DrawMapImpl.list_mean(stops_lon)
        center_lat = DrawMapImpl.list_mean(stops_lat)

        fig = go.Figure(go.Scattermapbox(
            lon = np.asarray(poly_lon),
            lat = np.asarray(poly_lat),
            mode='lines',
            line_width=2.5,
            name='Rota do ônibus'
        ))

        fig.add_trace(go.Scattermapbox(
            lon = stops_lon,
            lat = stops_lat,
            mode='markers',
            marker_size=8,
            name='Pontos de ônibus'))

        fig.add_trace(go.Scattermapbox(
            lon = bus_lon,
            lat = bus_lat,
            mode='markers',
            marker_size=8,
            name='Veículos'))

        fig.update_layout(
            margin ={'l':0,'t':0,'b':0,'r':0},
            mapbox = {
                'center': {"lat": center_lat, "lon": center_lon},
                'style': "open-street-map",
                'zoom': 14})

        return fig.to_html()

    def get_lon_lat_from_tuples_list(tuple_list):
        lon = [elem[0] for elem in tuple_list]
        lat = [elem[1] for elem in tuple_list]
        return lon, lat

    def list_mean(list):
        return sum(list) / len(list)