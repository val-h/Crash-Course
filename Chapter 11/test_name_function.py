import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    def test_first_last_name(self):
        """Do random names like Miskit Fiskit work"""
        formatted_name = get_formatted_name('miskit', 'fiskit', 'biskit')
        self.assertEqual(formatted_name, 'Miskit Biskit Fiskit')
    
    def test_first_middle_last_name(self):
        """Do names like Wolfgang Amadeus Mozart work"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
