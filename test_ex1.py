import ex1
import unittest


class TestFuncs(unittest.TestCase):

    def test_max_int(self):
        self.assertEqual(ex1.max_int(0, 2), 2)
        self.assertEqual(ex1.max_int(-1, -5), -1)
        self.assertEqual(ex1.max_int(-1, 2), 2)
        self.assertEqual(ex1.max_int(0, 0), 0)

    def test_min_int(self):
        self.assertEqual(ex1.min_int([0, 2, 7, 9]), 0)
        self.assertEqual(ex1.min_int([-1, -5]), -5)
        self.assertEqual(ex1.min_int([11, 2, 7]), 2)
        self.assertEqual(ex1.min_int([4, 5, 9, 78, -100, 90, 19, 33]), -100)

    def test_mysqrt(self):
        self.assertEqual(ex1.mysqrt(16), 4.00)
        self.assertEqual(ex1.mysqrt(10), 3.16)
        self.assertEqual(ex1.mysqrt(186), 13.64)
        self.assertEqual(ex1.mysqrt(2500), 50.00)

    def test_perimeter(self):
        self.assertEqual(ex1.perimeter(1), 6.28)
        self.assertEqual(ex1.perimeter(55), 345.58)
        self.assertEqual(ex1.perimeter(17), 106.81)
        self.assertEqual(ex1.perimeter(31.098), 195.39)

    def test_angle(self):
        self.assertEqual(ex1.angle(2, 2, 2), (60, 60, 60))
        self.assertEqual(ex1.angle(3, 4, 5), (37, 53, 90))
        self.assertEqual(ex1.angle(78, 26, 55), (146, 11, 23))
        self.assertEqual(ex1.angle(15, 15, 20), (48, 48, 84))

if __name__ == '__main__':
    unittest.main()
