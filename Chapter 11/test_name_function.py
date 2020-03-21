import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    def test_first_last_name(self):
        """Do random names like Miskit Fiskit"""
        formated_name = get_formatted_name('miskit', 'fiskit')
        self.assertEqual(formated_name, 'Miskit Fiskit')

if __name__ == '__main__':
    unittest.main()