from http import HTTPStatus
import json
import unittest
from unittest.mock import MagicMock, patch
from backend.controllers import favorite_controller
from backend.domain.favorite.get_favorite import GetFavorite
from backend.domain.favorite.modify_favorite import ModifyFavorite
from backend.tests import PATH_TEST

from backend.tests.unity.utils.test_base import TestBase

class TestFavoriteController(TestBase):
    @patch.object(ModifyFavorite, "new_favorite")
    def test_create_favorite(self, mock_create: MagicMock):
        """Test create favorite controller when default behaviour"""

        # when
        email = "valid@mail.com"
        data = {
            "email": email,
            "route_id": "routeId",
            "stop_id": "stopId"
        }

        # mock
        mock_create.return_value = {"value": "return"}

        # then
        response = self.app.post(
            PATH_TEST + "/favorites",
            follow_redirects=True,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )

        # assert
        self.assertEqual(response.status_code, HTTPStatus.OK)
        mock_create.assert_called_once_with(email, data.get("route_id"), data.get("stop_id"))

    @patch.object(ModifyFavorite, "new_favorite")
    def test_create_favorite_No_Route_id(self, mock_create: MagicMock):
        """Test create favorite controller when default behaviour"""

        # when
        email = "valid@mail.com"
        data = {
            "email": email,
            "stop_id": "stopId"
        }

        # then
        response = self.app.post(
            PATH_TEST + "/favorites",
            follow_redirects=True,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )

        # assert
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        mock_create.assert_not_called()

    @patch.object(ModifyFavorite, "new_favorite")
    def test_create_favorite_No_Stop_id(self, mock_create: MagicMock):
        """Test create favorite controller when default behaviour"""

        # when
        email = "valid@mail.com"
        data = {
            "email": email,
            "route_id": "routeId"
        }

        # then
        response = self.app.post(
            PATH_TEST + "/favorites",
            follow_redirects=True,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )

        # assert
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        mock_create.assert_not_called()

    @patch.object(ModifyFavorite, "exclude_favorite")
    def test_delete_favorite(self, mock_delete: MagicMock):
        """Test delete favorite controller when default behaviour"""

        # when
        email = "valid@mail.com"
        data = {
            "email": email,
            "route_id": "routeId",
            "stop_id": "stopId",
            "time": "11:22:33"
        }

        # mock
        mock_delete.return_value = {"value": "return"}

        # then
        response = self.app.delete(
            PATH_TEST + "/favorites",
            follow_redirects=True,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )

        # assert
        self.assertEqual(response.status_code, HTTPStatus.OK)
        mock_delete.assert_called_once_with(email, data.get("route_id"), data.get("stop_id"), data.get("time"))

    @patch.object(ModifyFavorite, "exclude_favorite")
    def test_delete_favorite_No_Route_id(self, mock_delete: MagicMock):
        """Test delete favorite controller when no route sent"""

        # when
        email = "valid@mail.com"
        data = {
            "email": email,
            "stop_id": "stopId",
            "time": "11:22:33"
        }

        # then
        response = self.app.delete(
            PATH_TEST + "/favorites",
            follow_redirects=True,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )

        # assert
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        mock_delete.assert_not_called()

    @patch.object(ModifyFavorite, "exclude_favorite")
    def test_delete_favorite_No_Stop_id(self, mock_delete: MagicMock):
        """Test delete favorite controller when no stop sent"""

        # when
        email = "valid@mail.com"
        data = {
            "email": email,
            "route_id": "routeId",
            "time": "11:22:33"
        }

        # then
        response = self.app.delete(
            PATH_TEST + "/favorites",
            follow_redirects=True,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )

        # assert
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        mock_delete.assert_not_called()

    @patch.object(ModifyFavorite, "exclude_favorite")
    def test_delete_favorite_No_Time(self, mock_delete: MagicMock):
        """Test delete favorite controller when no time sent"""

        # when
        email = "valid@mail.com"
        data = {
            "email": email,
            "route_id": "routeId",
            "stop_id": "stopId"
        }

        # then
        response = self.app.delete(
            PATH_TEST + "/favorites",
            follow_redirects=True,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )

        # assert
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        mock_delete.assert_not_called()

    @patch.object(ModifyFavorite, "exclude_favorite")
    def test_delete_favorite_Not_Found(self, mock_delete: MagicMock):
        """Test delete favorite controller when no favorite found"""

        # when
        email = "valid@mail.com"
        data = {
            "email": email,
            "route_id": "routeId",
            "stop_id": "stopId",
            "time": "11:22:33"
        }

        # mock
        mock_delete.side_effect = Exception()

        # then
        response = self.app.delete(
            PATH_TEST + "/favorites",
            follow_redirects=True,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )

        # assert
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        mock_delete.assert_called_once_with(email, data.get("route_id"), data.get("stop_id"), data.get("time"))

    @patch.object(GetFavorite, "get_all_user_favorites")
    def test_get_favorite(self, mock_get: MagicMock):
        """Test get favorite controller when default behaviour"""

        # when
        email = "valid@mail.com"

        # mock
        mock_get.return_value = {"user_favorites": 0}

        # then
        response = self.app.get(
            PATH_TEST + "/favorites",
            follow_redirects=True,
            headers={"Content-Type": "application/json", "email": email}
        )

        # assert
        self.assertEqual(response.status_code, HTTPStatus.OK)
        mock_get.assert_called_once_with(email)
