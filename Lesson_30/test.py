import unittest
import lesson_30

class TestPlusFunction(unittest.TestCase):
    def setUp(self):
        # self.x - 5
        print('Works all the time!')

    def test_plus(self):
        test_num = 10
        print('test_num')
        result = lesson_30.plus(test_num)
        self.assertEqual(result, 15)

    def test_plus_not_equal(self):
        test_num = 10
        result = lesson_30.plus(test_num)
        self.assertNotEqual(result, 15) # 15 != 10

    def test_plus_passing_string(self):
        test_val = 'a'
        result = lesson_30.plus(test_val)
        self.assertIsInstance(result, ValueError)

    def test_plus_none_as_arg(self):
        test_val = None
        result = lesson_30.plus(test_val)
        self.assertEqual(result, 'please enter a number')
        
    def test_plus_passing_string(self):
        result = lesson_30.plus()
        self.assertEqual(result, 'please enter a number')

    def tearDown(self):
        print('Ending tests workflow!')
        # del self.x