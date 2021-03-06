import unittest
from unittest.mock import MagicMock, patch
from backend.domain.favorite.modify_favorite import ModifyFavorite

from backend.domain.repositories.favorites_repository import FavoritesRepository


class TestsModifyFavorite(unittest.TestCase):
    @patch.object(FavoritesRepository, "add_favorite")
    def test_new_favorite(self, mock_add_favorite: MagicMock):
        """Test create new favorite when default behaviour"""

        # when
        email = "valid@mail.com"
        route_id = "1"
        stop_id = "2"

        # then
        result = ModifyFavorite().new_favorite(email, route_id, stop_id)

        # assert
        mock_add_favorite.assert_called_once()
        self.assertTrue("success" in result.get("message"))

    @patch.object(FavoritesRepository, "remove_favorite")
    def test_exclude_favorite(self, mock_remove_favorite: MagicMock):
        """Test eclude favorite when default behaviour"""

        # when
        email = "valid@mail.com"
        route_id = "1"
        stop_id = "2"
        time = "11:22:33"

        # then
        result = ModifyFavorite().exclude_favorite(email, route_id, stop_id, time)

        # assert
        mock_remove_favorite.assert_called_once()
        self.assertTrue("success" in result.get("message"))
