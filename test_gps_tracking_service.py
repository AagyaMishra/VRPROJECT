import unittest
from gps_tracking_service import GPSTrackingService

class TestGPSTrackingService(unittest.TestCase):
    def setUp(self):
        self.api_key = 'test_api_key'
        self.service = GPSTrackingService(self.api_key)

    def test_get_location(self):
        """Test the get_location method with a mock API response."""
        # Mocking the requests.get method
        with unittest.mock.patch('requests.get') as mocked_get:
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.json.return_value = {'latitude': 37.7749, 'longitude': -122.4194}
            result = self.service.get_location('device123')
            self.assertEqual(result['latitude'], 37.7749)
            self.assertEqual(result['longitude'], -122.4194)

    def test_process_location_data(self):
        """Test the process_location_data method."""
        data = {'latitude': 37.7749, 'longitude': -122.4194}
        result = self.service.process_location_data(data)
        self.assertEqual(result, "Latitude: 37.7749, Longitude: -122.4194")

if __name__ == "__main__":
    unittest.main()
