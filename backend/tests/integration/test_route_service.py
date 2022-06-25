import unittest
from backend.app import app

class TestRouteService(unittest.TestCase):

    def setUp(self):
        app.config.update({
            "TESTING": True,
        })
        self.client_app = app.test_client()
    
    def test_get_routes_info(self):
        route = '/api/routes'

        response = self.client_app.get(route)

        self.assertEqual(200, response.status_code)
        self.assertEqual(list, type(response.json))
        self.assertEqual(['route_id', 'route_short_name', 'route_long_name'], list(response.json[0].keys()))

    def test_get_route_info_by_route_id(self):
        route = '/api/routes/{}'.format('4801A-01')

        response = self.client_app.get(route)

        self.assertEqual(200, response.status_code)
        self.assertEqual('4801A-01', response.json['route_id'])
        self.assertEqual(list, type(response.json['stops']))
        self.assertEqual(['stop_id', 'stop_lat', 'stop_lon', 'stop_name'], list(response.json['stops'][0].keys()))
