import unittest
from backend.domain.bus_stop.get_stop import GetStop
from backend.tests.mock.stops_repository_mock import StopsRepositoryMock
from backend.tests.mock.route_stop_repository_mock import RouteStopRepositoryMock
from backend.domain.repositories.stops_repository import StopsRepository
from backend.domain.repositories.route_stop_repository import RouteStopRepository
from backend.domain.route_stop.get_route_stop import GetRouteStop

class TestGetRouteStop(unittest.TestCase):

    def setUp(self):
        stops_repo = StopsRepository(StopsRepositoryMock())
        route_stop_repo = RouteStopRepository(RouteStopRepositoryMock())
        get_stop = GetStop(stops_repo, route_stop_repo)
        self.get_route_stop = GetRouteStop(route_stop_repo, get_stop)

    def test_get_coordinates_stops_in_route(self):
        coords = self.get_route_stop.get_coordinates_stops_in_route('609-03')
        self.assertEqual(coords, [
            (-44.0220132041767, -19.97477301931237), 
            (-43.94348498583775, -19.90639647366688)])
