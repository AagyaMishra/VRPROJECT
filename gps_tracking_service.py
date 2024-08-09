import requests
import json

class GPSTrackingService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.gpsservice.com/tracking'

    def get_location(self, device_id):
        """Retrieve the current location of a device."""
        url = f"{self.base_url}/location/{device_id}"
        params = {'api_key': self.api_key}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def process_location_data(self, data):
        """Process and format location data."""
        # Example processing: Convert coordinates to a readable format
        latitude = data['latitude']
        longitude = data['longitude']
        return f"Latitude: {latitude}, Longitude: {longitude}"

if __name__ == "__main__":
    # Example usage
    api_key = 'your_api_key_here'
    device_id = 'device123'
    service = GPSTrackingService(api_key)
    location_data = service.get_location(device_id)
    formatted_data = service.process_location_data(location_data)
    print(formatted_data)
