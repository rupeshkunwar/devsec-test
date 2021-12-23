import unittest
from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

from python import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.db_patch().start()

    @staticmethod
    def db_patch():
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 1
        return patch(
            "python.utils.connect_db", return_value=(mock_conn, mock_cursor)
        )

    def test_health(self):
        response = self.client.get("/healthz")
        self.assertEqual("Healthy", response.json())

    def test_sample_api(self):
        response = self.client.put("get_hit_count/12345")
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json())

    def tearDown(self):
        pass
