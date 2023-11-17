from unittest import TestCase

from equations import Equations


class TestEquations(TestCase):

    def setUp(self):
        self.equations = Equations()

    def test_calculate_speed(self):

       initial_speed = 2

       self.assertEquals(2, self.equations.calculate_distance_along_x_axis(initial_speed))
