from unittest import TestCase
from unittest.mock import Mock

from environment import Environment
from equations import Equations


class TestEnvironment(TestCase):

    def setUp(self):
        self.equations = Mock()
        self.env = Environment(self.equations)
        self.env.run_simulation()

    def test_run_simulation(self):
        self.equations.calculate_distance_along_x_axis.assert_called_with(5)
