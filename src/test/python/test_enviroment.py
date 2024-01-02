from unittest import TestCase
from unittest.mock import Mock

from environment import Environment
from equations import Equations


class TestEnvironment(TestCase):

    def setUp(self):
        self.equations = Mock()
        self.initial_x_speed = 5
        self.initial_y_speed = 98.1
        self.max_time = 10
        self.env = Environment(self.initial_x_speed, self.initial_y_speed, self.max_time)
        self.env.run_simulation()

    def test_run_simulation_returns_correct_horizontal_position(self):
        expected_x_positions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

        self.assertEquals(self.env.x_points_per_sec, expected_x_positions)

    def test_run_simulation_returns_correct_vertical_position(self):
        expected_y_positions = [93.195, 176.58, 250.155, 313.92, 367.875, 412.02, 446.355, 470.88, 485.595, 490.5]

        self.assertEquals(expected_y_positions, self.env.y_points_per_sec)
