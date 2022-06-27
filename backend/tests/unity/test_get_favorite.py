import unittest
from unittest.mock import MagicMock, patch
from backend.database.models.favorites import Favorites
from backend.domain.bus_stop.bus_stop import BusStop
from backend.domain.bus_stop.get_stop import GetStop
from backend.domain.favorite.get_favorite import GetFavorite

from backend.domain.repositories.favorites_repository import FavoritesRepository
from backend.domain.route.get_route import GetRoute
from backend.domain.route.route import Route


class TestsGetFavorite(unittest.TestCase):
    @patch.object(GetStop, "get_stop_by_id")
    @patch.object(GetRoute, "get_route_by_id")
    @patch.object(FavoritesRepository, "return_all_user_favorites")
    def test_get_all_user_favorites(
        self,
        mock_return_all_user_favorites: MagicMock,
        mock_get_route_by_id: MagicMock,
        mock_get_stop_by_id: MagicMock,
    ):
        """Test create new favorite when default behaviour"""

        # when
        favorite_id = 1
        email = "valid@mail.com"
        route_id = "123"
        stop_id = "321"
        route_name = "route_name"
        stop_name = "stop_name"

        favorites = [Favorites(favorite_id, email, route_id, stop_id)]
        route = Route(route_id, route_short_name=route_name)
        stop = BusStop(stop_id, stop_name, 1.1, 2.2)

        # mock
        mock_return_all_user_favorites.return_value = favorites
        mock_get_route_by_id.return_value = route
        mock_get_stop_by_id.return_value = stop

        # then
        result = GetFavorite().get_all_user_favorites(email)

        # assert
        mock_return_all_user_favorites.assert_called_once_with(email)
        mock_get_route_by_id.assert_called_once_with(route_id)
        mock_get_stop_by_id.assert_called_once_with(stop_id)
        self.assertEqual(result[0].get("favorite_id"), favorite_id)

    @patch.object(GetStop, "get_stop_by_id")
    @patch.object(GetRoute, "get_route_by_id")
    @patch.object(FavoritesRepository, "return_all_user_favorites")
    def test_get_all_user_favorites_NoFavorites(
        self,
        mock_return_all_user_favorites: MagicMock,
        mock_get_route_by_id: MagicMock,
        mock_get_stop_by_id: MagicMock,
    ):
        """Test create new favorite when user has no favorites"""

        # when
        email = "valid@mail.com"

        # mock
        mock_return_all_user_favorites.return_value = []

        # then
        result = GetFavorite().get_all_user_favorites(email)

        # assert
        mock_return_all_user_favorites.assert_called_once_with(email)
        mock_get_route_by_id.assert_not_called()
        mock_get_stop_by_id.assert_not_called()
        self.assertTrue(len(result) == 0)
