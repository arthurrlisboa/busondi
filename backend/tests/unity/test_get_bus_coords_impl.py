import unittest
from backend.domain.repositories.real_time_repository import RealTimeRepository

from backend.domain.repositories.routes_repository import RoutesRepository
from backend.domain.route.get_bus_coords_impl import GetBusCoordsImpl
from backend.tests.mock.real_time_repository_mock import RealTimeRepositoryMock
from backend.tests.mock.routes_repository_mock import RoutesRepositoryMock

class TestGetBusCoordsImpl(unittest.TestCase):

    def setUp(self):
        routes_repo = RoutesRepository(RoutesRepositoryMock())
        real_time_repo = RealTimeRepository(RealTimeRepositoryMock())
        self.get_bus_coords = GetBusCoordsImpl(routes_repo, real_time_repo)

    def test_get_bus_coords_impl(self):
        bus_coords = self.get_bus_coords.get_bus_coords_impl('5102-01')

        self.assertEqual(bus_coords, [
            (-43.962638, -19.908195), 
            (-43.979139, -19.885632), 
            (-43.969587, -19.870928), 
            (-43.979224, -19.885632), 
            (-43.966019, -19.89857), 
            (-43.941044, -19.937846), 
            (-43.960387, -19.864423)])