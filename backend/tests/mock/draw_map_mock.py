from plotly import graph_objects as go
import numpy as np

class DrawMapMock:

    def draw_map_route_stops_bus_position_impl():
        poly_lon = [-43.9428964472, -43.9422687041, -43.9403954009, -43.9400881573, -43.9388536998, -43.9372950691, -43.9370212181, -43.9364718788, -43.9375943925, -43.9379225006, -43.9371881908, -43.9376702366, -43.9360200903, -43.9361599042, -43.938972628, -43.9438116139, -43.9435525716, -43.943737874, -43.9459440969, -43.948475, -43.949062, -43.950886, -43.952425, -43.953434, -43.953692, -43.953653, -43.95406, -43.954986, -43.955812, -43.95634, -43.956823, -43.958427, -43.959511, -43.960149, -43.961318, -43.962445, -43.963427, -43.964398, -43.965342, -43.966254, -43.966656, -43.966705, -43.966289, -43.965863, -43.965752, -43.96557, -43.964494, -43.964417, -43.964859, -43.965272, -43.966353, -43.966801, -43.967123, -43.967595, -43.968448, -43.969644, -43.970733, -43.971658, -43.973429, -43.974268, -43.974842, -43.975239, -43.975652, -43.976113, -43.976553, -43.9765963021, -43.9758203482, -43.9752079673, -43.9748488584, -43.9742655125, -43.9739512314, -43.9726514838, -43.9716589957, -43.970523613, -43.9680228484, -43.9652002377, -43.9650979062, -43.9650024067, -43.9646411996, -43.9628859799, -43.9622720451, -43.9620401782, -43.9619023266, -43.9618199776, -43.9617627476, -43.9611848442, -43.9607350557, -43.960303509, -43.9595615923, -43.958247562, -43.9580145446, -43.9579612213, -43.9581096249, -43.9583749852, -43.9593561052, -43.9598999526, -43.9590175753, -43.9590919394, -43.959975229, -43.9428964472]
        poly_lat = [-19.9474957947, -19.9476039937, -19.9407097891, -19.9397718274, -19.9400641248, -19.9392614508, -19.9387555397, -19.9365712253, -19.9346591991, -19.9341058145, -19.9312658, -19.9311098681, -19.9252010824, -19.9248998711, -19.9241757975, -19.9229575582, -19.9220807326, -19.9217585423, -19.9212736707, -19.917343, -19.916989, -19.916609, -19.916256, -19.915545, -19.915056, -19.913843, -19.913566, -19.912013, -19.910424, -19.909687, -19.9093, -19.908487, -19.908023, -19.907892, -19.90795, -19.90827, -19.906747, -19.905274, -19.903776, -19.902324, -19.901668, -19.901108, -19.899514, -19.897771, -19.895986, -19.895365, -19.893941, -19.893335, -19.891944, -19.891584, -19.890904, -19.890051, -19.889269, -19.888644, -19.887725, -19.886464, -19.885362, -19.88489, -19.88431, -19.883942, -19.883443, -19.882625, -19.88092, -19.879235, -19.877545, -19.8771483743, -19.8765564144, -19.8760431743, -19.8752012724, -19.873720677, -19.8733994599, -19.8724549503, -19.8725476323, -19.8716894862, -19.8697907415, -19.8700579106, -19.8702381569, -19.8702593284, -19.870010131, -19.8686674235, -19.8681906189, -19.8681417211, -19.8681421267, -19.868165932, -19.8681818906, -19.8688653685, -19.8693756863, -19.869061228, -19.8684990006, -19.8675033807, -19.8673274203, -19.8671444766, -19.8667757154, -19.8660574627, -19.8648790023, -19.8642529476, -19.8635287188, -19.8633829163, -19.8640527938, -19.9474957947]
        stops_lon = [-43.93779403502927, -43.94097579785661, -43.94626442520561, -43.93682125149422, -43.94455013644543, -43.9364668288804, -43.93683222704595, -43.9373738206421, -43.9405083406234, -43.9409522710909, -43.9415358610267, -43.9419962198647, -43.93749715205314, -43.95607489100124, -43.95994403939118, -43.9634890951145, -43.96620372186111, -43.96608729247668, -43.9657464902479, -43.9658066698136, -43.96785845639805, -43.97279632855811, -43.9428036848118, -43.9380695060553, -43.9586003765398, -43.9601336795569, -43.9597995043323, -43.959374914484, -43.9705591816526, -43.9684607693784, -43.9666582422688, -43.9634097113632, -43.9629240935212, -43.9757972413964, -43.9736313157599]
        stops_lat = [-19.92442643258235, -19.92364947359565, -19.92071271208315, -19.93591050243273, -19.92152839545358, -19.9267854030977, -19.92814288190163, -19.93010548193524, -19.9412539950543, -19.9428437403061, -19.9449994013886, -19.946679055668, -19.9326943644191, -19.90995224699728, -19.90794316212856, -19.90663254358811, -19.902356949653, -19.89932426999088, -19.8963039120875, -19.8912142861161, -19.88823505464308, -19.88447883908858, -19.9474620978635, -19.9396855858187, -19.8677767503174, -19.868955555478, -19.8638735607605, -19.864866091972, -19.87174063299, -19.8701745351716, -19.8699405466065, -19.8690793687567, -19.8687068926792, -19.8765457470447, -19.8731349491841]
        bus_lon = [-43.941844, -43.958324, -43.960395, -43.939009, -43.979192, -43.979252, -43.979027]
        bus_lat = [-19.94593, -19.866356, -19.864377, -19.924278, -19.885648, -19.88564, -19.885968]
        center_lat = -19.904517583395826
        center_lon = -43.954394216378326

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

        return fig