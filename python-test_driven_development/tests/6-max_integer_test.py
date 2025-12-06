import unittest
max_integer = __import__('6-max_integer').max_integer
class TestAddIntegerMethod(unittest.TestCase):
    def test_position(slef):
        slef.assertEqual(max_integer([1,5,6]),6)
        slef.assertEqual(max_integer([8,5,6]),8)
        slef.assertEqual(max_integer([1,11,2]),11)
        slef.assertEqual(max_integer([-1, -11,-2]),-1)
        slef.assertEqual(max_integer([-5]),-5)
        slef.assertEqual(max_integer([]),None)
