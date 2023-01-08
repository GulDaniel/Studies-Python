import unittest
from city_functions import get_formatted_location

class CityCaseTest(unittest.TestCase):
    def test_city_country(self):
        formatted_location = get_formatted_location('santiago', 'chile')
        self.assertEqual(formatted_location, 'Santiago, Chile')

    def test_city_coutry_population(self):
        formatted_location = get_formatted_location('santiago', 'chile', '50000')
        self.assertEqual(formatted_location, 'Santiago, Chile, Population = 50000')

unittest.main()
