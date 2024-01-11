from unittest import TestCase
from unittest.mock import Mock

import numpy as np

from environment import Environment
from equations import Equations


class TestEnvironment(TestCase):

    def setUp(self):
        # mock objects
        self.equations = Equations()
        self.resolving_vectors = Mock()
        self.env.creating_plot = Mock()

        # mock objects return values
        self.resolving_vectors.resolve_initial_input_velocity = Mock()
        self.resolving_vectors.resolve_initial_input_velocity.return_value = np.array([70.711, 70.711])

        # variables inputs into env
        self.max_time = 10
        self.env = Environment(self.max_time, self.resolving_vectors, self.equations)
        self.env.creating_plot.return_value = None

        # running env
        self.env.run_environment()

    def test_run_simulation_returns_correct_horizontal_position(self):
        expected_x_positions = [70.711*_ for _ in range(11)]
        del(expected_x_positions[0])

        np.testing.assert_almost_equal((np.array(self.env.x_points_per_sec)), np.array(expected_x_positions))

    def test_run_simulation_returns_correct_vertical_position(self):
        expected_y_positions = self._calculate_expected_y_positions()
        actual_y_positions = self.env.y_points_per_sec
        rounded_actual_y_positions = []

        for position in actual_y_positions:
            rounded_actual_y_positions.append(round(position, 3))

        np.testing.assert_almost_equal(np.array(expected_y_positions), np.array(rounded_actual_y_positions), 3)


    def _calculate_expected_y_positions(self):
        y_velocity = 70.711
        initial_y_position = 0
        expected_y_positions = []
        for _ in range (10):
            new_y = self.equations.calculate_vertical_position_along_y_axis(y_velocity)
            y_velocity = self.equations.calculate_speed_along_y_axis(y_velocity)
            initial_y_position += new_y

            expected_y_positions.append(initial_y_position)
        return expected_y_positions
