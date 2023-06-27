"""
python -m unittest
python -m unittest -v
"""

import unittest
import lesson_29

class TestPlusFunction(unittest.TestCase):
    def test_plus(self):
        test_num = 10
        result = lesson_29.plus(test_num)
        self.assertEqual(result, 15)

    def test_plus_not_equal(self):
        test_num = 10
        result = lesson_29.plus(test_num)
        self.assertNotEqual(result, 15) # 15 != 10

    def test_passing_string(self):
        test_val = 'a'
        result = lesson_29.plus(test_val)
        self.assertIsInstance(result, ValueError)
    
unittest.main()