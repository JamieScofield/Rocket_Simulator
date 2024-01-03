from unittest import TestCase

from equations import Equations


class TestEquations(TestCase):
    def setUp(self):
        self.equations = Equations()

    def test_calculate_horizontal_speed(self):

       initial_x_speed = 2

       self.assertEquals(2, self.equations.calculate_speed_along_x_axis(initial_x_speed))

    def test_calculate_vertical_speed_with_equal_velocity_to_acceleration(self):
        initial_y_speed = 9.81
        self.assertAlmostEquals(0, self.equations.calculate_speed_along_y_axis(initial_y_speed), 3)

    def test_calculate_vertical_speed_with_greater_velocity_to_acceleration(self):
        initial_y_speed = 10
        self.assertAlmostEquals(0.19, self.equations.calculate_speed_along_y_axis(initial_y_speed), 3)

    def test_calculate_vertical_position_along_y_axis_returns_correct_value(self):
        initial_y_velocity = 10
        self.assertAlmostEquals(5.095, self.equations.calculate_vertical_position_along_y_axis(initial_y_velocity), 3)
