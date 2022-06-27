import unittest
from backend.domain.repositories.routes_repository import RoutesRepository
from backend.domain.repositories.route_stop_repository import RouteStopRepository
from backend.domain.route.bus_schedule import BusSchedule
from backend.tests.mock.routes_repository_mock import RoutesRepositoryMock
from backend.tests.mock.route_stop_repository_mock import RouteStopRepositoryMock

class TestBusSchedule(unittest.TestCase):
    def setUp(self):
        routes_repo = RoutesRepository(RoutesRepositoryMock())
        route_stop_repo = RouteStopRepository(RouteStopRepositoryMock())
        self.bus_schedule = BusSchedule(routes_repo, route_stop_repo)

    def test_get_arrival_time(self):
        arrival_time = self.bus_schedule.get_arrival_time('104787000120', '609-01')
        self.assertEqual(arrival_time, '9:38:18.610000')
