import unittest

from backend.domain.repositories.route_stop_repository import RouteStopRepository
from backend.domain.repositories.routes_repository import RoutesRepository
from backend.tests.mock.routes_repository_mock import RoutesRepositoryMock
from backend.tests.mock.route_stop_repository_mock import RouteStopRepositoryMock
from backend.domain.route.get_route_impl import GetRouteImpl

class TestGetRouteImpl(unittest.TestCase):

    def setUp(self):
        route_stop_repo = RouteStopRepository(RouteStopRepositoryMock())
        routes_repo = RoutesRepository(RoutesRepositoryMock())
        self.get_route = GetRouteImpl(routes_repo, route_stop_repo)

    def test_get_routes_from_stop_impl(self):
        routes_list = self.get_route.get_routes_from_stop_impl('104787000120')

        self.assertEqual(routes_list[0][0], 18401)
        self.assertEqual(routes_list[1][0], 18504)
        self.assertEqual(routes_list[2][0], 18612)

        self.assertEqual(routes_list[0][1].__dict__, {
            'route_id': '609-01', 
            'route_short_name': '609', 
            'route_long_name': '', 
            'shape_id': '', 
            'initial_stop_id': '', 
            'final_stop_id': ''})
        self.assertEqual(routes_list[1][1].__dict__, {
            'route_id': '609-02', 
            'route_short_name': '609', 
            'route_long_name': '', 
            'shape_id': '', 
            'initial_stop_id': '', 
            'final_stop_id': ''})
        self.assertEqual(routes_list[2][1].__dict__, {
            'route_id': '609-03', 
            'route_short_name': '609', 
            'route_long_name': '', 
            'shape_id': '', 
            'initial_stop_id': '', 
            'final_stop_id': ''})

    def test_get_all_routes_impl(self):
        routes_list = self.get_route.get_all_routes_impl()

        self.assertEqual(routes_list[0].__dict__, {
            'route_long_name': 'Jardim Filadelfia/Boa Vista A (Principal)', 
            'route_id': '4801A-01', 
            'initial_stop_id': '', 
            'final_stop_id': '', 
            'shape_id': '', 
            'route_short_name': '4801A'})
        self.assertEqual(routes_list[1].__dict__, {
            'route_long_name': 'Casa Branca/Sao Francisco Via Est. Jose Candido (Principal)', 
            'route_id': '9550-01', 
            'initial_stop_id': '', 
            'final_stop_id': '',
            'shape_id': '', 
            'route_short_name': '9550'})
        self.assertEqual(routes_list[2].__dict__, {
            'route_long_name': 'Ermelinda/Salgado Filho (Principal)', 
            'route_id': '4205-01', 
            'initial_stop_id': '', 
            'final_stop_id': '', 
            'shape_id': '', 
            'route_short_name': '4205'})

    def test_get_route_by_id_impl(self):
        route = self.get_route.get_route_by_id_impl('609-03')
        
        self.assertEqual(route.__dict__, {
            'route_id': '609-03', 
            'route_short_name': '609', 
            'route_long_name': 'Serra Verde/Santa Monica (Cid.Admin-Sentido Sta Monica)', 
            'shape_id': '', 
            'initial_stop_id': '', 
            'final_stop_id': ''})