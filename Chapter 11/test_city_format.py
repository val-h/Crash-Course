import unittest
from city_function import city_country_name

class NameFormatTest(unittest.TestCase):
    """A few test cases for basic format of a city-country relation"""

    def test_city_country_name(self):
        """Basic city-country test"""
        formatted_name = city_country_name('burgas', 'bulgaria')
        self.assertEqual(formatted_name, 'Burgas, Bulgaria')
    
    def test_city_region_country_name(self):
        """city, region and country test"""
        formatted_name = city_country_name('burgas', 'bulgaria', 'thrace')
        self.assertEqual(formatted_name, 'Burgas - Thrace, Bulgaria')

if __name__ == '__main__':
    unittest.main()
