from TunisiaWeatherForcast import format_response, get_weather, open_image
from unittest import TestCase, result

Gouvernourats = ["Sfax", "Tunis", "Ben Arous", "Kef", "Beja", "Ariana"]
class AppTest(TestCase):
    def test_get_weather(self):
        # Given 
        city_name = "Tunis"
        expected_response = 200

        # When
        result = get_weather(city_name)

        # Then
        self.assertEqual(expected_response, result)

    def test_format_response(self):
        # Given 
        city_json = {'coord': {'lon': 9, 'lat': 34}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 87.19, 'feels_like': 83.62, 'temp_min': 87.19, 'temp_max': 87.19, 'pressure': 1005, 'humidity': 16, 'sea_level': 1005, 'grnd_level': 1002}, 'visibility': 10000, 'wind': {'speed': 28.25, 'deg': 239, 'gust': 33.11}, 'clouds': {'all': 0}, 'dt': 1651767428, 'sys': {'country': 'TN', 'sunrise': 1651725066, 'sunset': 1651774214}, 'timezone': 3600, 'id': 2464461, 'name': 'Tunisia', 'cod': 200}
        expected_string = "City: Tunisia \nConditions: Clear Sky \nTemperature (°F): 85.5"
        # When
        results = format_response(city_json)
        # Then
        assert(expected_string == results)

    def test_get_weather_wrong(self):
        # Given 
        city_name = "jkjkhj"
        expected_response = 401
        # When
        result = get_weather(city_name)
        # Then
        # assert(expected_result == result)
        self.assertRaises(ValueError, expected_response, result)

    def test_open_icon_right(self):
        # Given
        icon_number= "04d"
        expected_result = 1
        # When
        result = open_image(icon_number)
        # Then
        assert (expected_result == result)

    def test_open_icon_wrong(self):
        # Given
        icon_number= "50d"
        expected_result = 1
        # When
        result = open_image(icon_number)
        # Then
        self.assertRaises(ValueError, expected_result, result)