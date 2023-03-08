
import unittest
from circle import getArea, getPerimeter

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(5),78.53975)
        self.assertAlmostEqual(getArea(10),314.159)
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(10),62.8318)
        self.assertAlmostEqual(getPerimeter(4),25.13272)

unittest.main()
