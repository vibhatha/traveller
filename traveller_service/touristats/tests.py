from io import StringIO
from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase
from touristats.models import AllCountryStats


class CheckDBCommandTest(TestCase):
    def setUp(self):
        self.out = StringIO()

    def test_successful_connection(self):
        """Test database connection when it's successful"""
        call_command("check_db", stdout=self.out)
        self.assertIn("Database connection successful", self.out.getvalue())

    @patch("django.db.backends.base.base.BaseDatabaseWrapper.cursor")
    def test_database_down(self, mock_cursor):
        """Test database connection when database is down"""
        # Mock the cursor to raise an OperationalError
        mock_cursor.side_effect = OperationalError("Could not connect to the database")

        call_command("check_db", stdout=self.out)
        self.assertIn("Database connection failed", self.out.getvalue())

    def test_connection_details(self):
        """Test if connection details are properly displayed"""
        call_command("check_db", stdout=self.out)
        output = self.out.getvalue()

        # Check if essential connection info is present
        self.assertIn("Connected to:", output)
        self.assertIn("Host:", output)
        self.assertIn("User:", output)

    def tearDown(self):
        self.out.close()


class TouristatsViewTest(TestCase):

    def setUp(self):
        # Create test data
        AllCountryStats.objects.create(
            country="TestCountry", year="2043", month="January", passengers=1
        )

    def test_touristats_view(self):
        arrivals_list = AllCountryStats.objects.all()
        print(arrivals_list)
        self.assertEqual(arrivals_list.count(), 1)
        self.assertEqual(arrivals_list[0].country, "TestCountry")
        self.assertEqual(arrivals_list[0].year, "2043")
        self.assertEqual(arrivals_list[0].month, "January")
        self.assertEqual(arrivals_list[0].passengers, 1)
