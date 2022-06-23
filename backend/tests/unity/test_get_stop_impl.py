import unittest
from backend.domain.bus_stop.get_stop_impl import GetStopImpl
from backend.tests.mock.stops_repository_mock import StopsRepositoryMock
from backend.tests.mock.route_stop_repository_mock import RouteStopRepositoryMock
from backend.domain.repositories.stops_repository import StopsRepository
from backend.domain.repositories.route_stop_repository import RouteStopRepository

class TestGetStopImpl(unittest.TestCase):

    def setUp(self):
        stops_repo = StopsRepository(StopsRepositoryMock())
        route_stop_repo = RouteStopRepository(RouteStopRepositoryMock())
        self.get_stop = GetStopImpl(stops_repo, route_stop_repo)

    def test_get_all_stops(self):
        stops_list = self.get_stop.get_all_stops_impl()
        self.assertEqual(stops_list[0].__dict__, {
            'stop_id' : '10100130600640', 
            'stop_name' : 'Estacao Move  Barreiro', 
            'stop_lat' : -19.97477301931237, 
            'stop_lon' : -44.0220132041767})
        self.assertEqual(stops_list[1].__dict__, {
            'stop_id' : '10100446100580', 
            'stop_name' : 'Estacao Move Senai', 
            'stop_lat' : -19.90639647366688, 
            'stop_lon' : -43.94348498583775})
        self.assertEqual(stops_list[2].__dict__, {
            'stop_id' : '10100446100880', 
            'stop_name' : 'Estacao Move Hospital Odilon Behrens', 
            'stop_lat' : -19.90394540382196, 
            'stop_lon' : -43.94459982011109})

    def test_get_stop_by_id(self):
        stop = self.get_stop.get_stop_by_id_impl('104787000120')
        self.assertEqual(stop.__dict__, {
            'stop_id' : '104787000120', 
            'stop_name' : 'Rua Norte 120', 
            'stop_lat' : -19.8305153133411, 
            'stop_lon' : -43.9687279827209})

    def test_get_stop_coordinates(self):
        coords = self.get_stop.get_stops_coordinates_impl(['10100130600640', '10100446100580'])
        self.assertEqual(coords[0], (-44.0220132041767, -19.97477301931237))
        self.assertEqual(coords[1], (-43.94348498583775, -19.90639647366688))


    def test_get_stops_from_route(self):
        stops_list = self.get_stop.get_stops_from_route_impl('609-03')
        self.assertEqual(stops_list[0].__dict__, {
            'stop_id' : '10100130600640', 
            'stop_name' : 'Estacao Move  Barreiro', 
            'stop_lat' : -19.97477301931237, 
            'stop_lon' : -44.0220132041767})
        self.assertEqual(stops_list[1].__dict__, {
            'stop_id' : '10100446100580', 
            'stop_name' : 'Estacao Move Senai', 
            'stop_lat' : -19.90639647366688, 
            'stop_lon' : -43.94348498583775})
