import unittest
import shapely
from backend.domain.route.draw_map_impl import DrawMapImpl

class TestDrawMapImpl(unittest.TestCase):
    def test_draw_map_route_stops_bus_position_impl(self):
        ref_polygon = 'POLYGON ((-43.9428964472 -19.9474957947, -43.9422687041 -19.9476039937, -43.9403954009 -19.9407097891, -43.9400881573 -19.9397718274, -43.9388536998 -19.9400641248, -43.9372950691 -19.9392614508, -43.9370212181 -19.9387555397, -43.9364718788 -19.9365712253, -43.9375943925 -19.9346591991, -43.9379225006 -19.9341058145, -43.9371881908 -19.9312658, -43.9376702366 -19.9311098681, -43.9360200903 -19.9252010824, -43.9361599042 -19.9248998711, -43.938972628 -19.9241757975, -43.9438116139 -19.9229575582, -43.9435525716 -19.9220807326, -43.943737874 -19.9217585423, -43.9459440969 -19.9212736707, -43.948475 -19.917343, -43.949062 -19.916989, -43.950886 -19.916609, -43.952425 -19.916256, -43.953434 -19.915545, -43.953692 -19.915056, -43.953653 -19.913843, -43.95406 -19.913566, -43.954986 -19.912013, -43.955812 -19.910424, -43.95634 -19.909687, -43.956823 -19.9093, -43.958427 -19.908487, -43.959511 -19.908023, -43.960149 -19.907892, -43.961318 -19.90795, -43.962445 -19.90827, -43.963427 -19.906747, -43.964398 -19.905274, -43.965342 -19.903776, -43.966254 -19.902324, -43.966656 -19.901668, -43.966705 -19.901108, -43.966289 -19.899514, -43.965863 -19.897771, -43.965752 -19.895986, -43.96557 -19.895365, -43.964494 -19.893941, -43.964417 -19.893335, -43.964859 -19.891944, -43.965272 -19.891584, -43.966353 -19.890904, -43.966801 -19.890051, -43.967123 -19.889269, -43.967595 -19.888644, -43.968448 -19.887725, -43.969644 -19.886464, -43.970733 -19.885362, -43.971658 -19.88489, -43.973429 -19.88431, -43.974268 -19.883942, -43.974842 -19.883443, -43.975239 -19.882625, -43.975652 -19.88092, -43.976113 -19.879235, -43.976553 -19.877545, -43.9765963021 -19.8771483743, -43.9758203482 -19.8765564144, -43.9752079673 -19.8760431743, -43.9748488584 -19.8752012724, -43.9742655125 -19.873720677, -43.9739512314 -19.8733994599, -43.9726514838 -19.8724549503, -43.9716589957 -19.8725476323, -43.970523613 -19.8716894862, -43.9680228484 -19.8697907415, -43.9652002377 -19.8700579106, -43.9650979062 -19.8702381569, -43.9650024067 -19.8702593284, -43.9646411996 -19.870010131, -43.9628859799 -19.8686674235, -43.9622720451 -19.8681906189, -43.9620401782 -19.8681417211, -43.9619023266 -19.8681421267, -43.9618199776 -19.868165932, -43.9617627476 -19.8681818906, -43.9611848442 -19.8688653685, -43.9607350557 -19.8693756863, -43.960303509 -19.869061228, -43.9595615923 -19.8684990006, -43.958247562 -19.8675033807, -43.9580145446 -19.8673274203, -43.9579612213 -19.8671444766, -43.9581096249 -19.8667757154, -43.9583749852 -19.8660574627, -43.9593561052 -19.8648790023, -43.9598999526 -19.8642529476, -43.9590175753 -19.8635287188, -43.9590919394 -19.8633829163, -43.959975229 -19.8640527938, -43.9428964472 -19.9474957947))'
        polygon = shapely.wkt.loads(ref_polygon)
        bus_coords = [(-43.941844, -19.94593), (-43.958324, -19.866356), (-43.960395, -19.864377), (-43.939009, -19.924278), (-43.979192, -19.885648), (-43.979252, -19.88564), (-43.979027, -19.885968)]
        stops_coords = [(-43.93779403502927, -19.92442643258235), (-43.94097579785661, -19.92364947359565), (-43.94626442520561, -19.92071271208315), (-43.93682125149422, -19.93591050243273), (-43.94455013644543, -19.92152839545358), (-43.9364668288804, -19.9267854030977), (-43.93683222704595, -19.92814288190163), (-43.9373738206421, -19.93010548193524), (-43.9405083406234, -19.9412539950543), (-43.9409522710909, -19.9428437403061), (-43.9415358610267, -19.9449994013886), (-43.9419962198647, -19.946679055668), (-43.93749715205314, -19.9326943644191), (-43.95607489100124, -19.90995224699728), (-43.95994403939118, -19.90794316212856), (-43.9634890951145, -19.90663254358811), (-43.96620372186111, -19.902356949653), (-43.96608729247668, -19.89932426999088), (-43.9657464902479, -19.8963039120875), (-43.9658066698136, -19.8912142861161), (-43.96785845639805, -19.88823505464308), (-43.97279632855811, -19.88447883908858), (-43.9428036848118, -19.9474620978635), (-43.9380695060553, -19.9396855858187), (-43.9586003765398, -19.8677767503174), (-43.9601336795569, -19.868955555478), (-43.9597995043323, -19.8638735607605), (-43.959374914484, -19.864866091972), (-43.9705591816526, -19.87174063299), (-43.9684607693784, -19.8701745351716), (-43.9666582422688, -19.8699405466065), (-43.9634097113632, -19.8690793687567), (-43.9629240935212, -19.8687068926792), (-43.9757972413964, -19.8765457470447), (-43.9736313157599, -19.8731349491841)]

        map = DrawMapImpl.draw_map_route_stops_bus_position_impl(polygon, bus_coords, stops_coords)
        with open('backend/tests/mock/draw_map_return.txt', 'r') as file:
            expected_return = str.encode(file.read())
        self.assertEqual(map.split(b'\n'), expected_return.split(b'\n'))

    def test_get_lon_lat_from_tuples_list(self):
        lon, lat = DrawMapImpl.get_lon_lat_from_tuples_list([(-43.937921, -19.934238), (-43.979214, -19.885677), (-43.97923, -19.884855), (-43.975711, -19.876461), (-43.959153, -19.908332), (-43.960059, -19.86411)])
        self.assertEqual(lon, [-43.937921, -43.979214, -43.97923, -43.975711, -43.959153, -43.960059])
        self.assertEqual(lat, [-19.934238, -19.885677, -19.884855, -19.876461, -19.908332, -19.86411])

    def test_list_mean(self):
        mean = DrawMapImpl.list_mean([1, 2, 3, 4, 5])
        self.assertEqual(mean, 3)