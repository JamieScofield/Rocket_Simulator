from unittest import TestCase
from unittest.mock import Mock

from environment import Environment
from equations import Equations


class TestEnvironment(TestCase):

    def setUp(self):
        self.equations = Mock()
        self.initial_speed = 5
        self.max_time = 10
        self.env = Environment(self.initial_speed, self.max_time)
        self.env.run_simulation()

    def test_run_simulation_returns_correct_horizontal_position(self):
        expected_x_positions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

        self.assertEquals(self.env.x_points_per_sec, expected_x_positions)
