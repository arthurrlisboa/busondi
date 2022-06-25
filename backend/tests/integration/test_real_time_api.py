import unittest
from backend.api.api_connection import APIConnection
from backend.adapters.real_time_repository_impl import RealTimeRepositoryImpl

class TestRealTimeAPI(unittest.TestCase):
    
    def test_get_bus_coords_from_api(self):
        with APIConnection() as connection:
            data = connection.get_data()

        bus_coords = RealTimeRepositoryImpl().extract_bus_coords(data)

        self.assertEqual(list, type(bus_coords))
        self.assertEqual(tuple, type(bus_coords[0]))