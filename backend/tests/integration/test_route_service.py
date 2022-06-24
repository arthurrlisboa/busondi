import unittest
import json
from backend.app import app

class TestRouteService(unittest.TestCase):

    def setUp(self):
        app.config.update({
            "TESTING": True,
        })
        self.client_app = app.test_client()
    
    def test_get_route_info_by_route_id(self):
        with self.client_app:
            route = '/api/routes/{}'.format('4801A-01')

            response = self.client_app.get(route)

            self.assertEqual(200, response.status_code)
            self.assertEqual('4801A-01', response.json['route_id'])
            self.assertEqual(list, type(response.json['stops']))
            self.assertEqual(['stop_id', 'stop_lat', 'stop_lon', 'stop_name'], list(response.json['stops'][0].keys()))
