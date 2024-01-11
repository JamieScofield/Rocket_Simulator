from unittest import TestCase
import numpy as np
from resolving_vectors import ResolvingVectors


class TestResolvingVectors(TestCase):

    def setUp(self):
        self._initial_launch_velocity = 10
        self._launch_angle = 45
        self._resolving_vectors = ResolvingVectors(self._initial_launch_velocity, self._launch_angle)

    def test_resolve_initial_input_velocity(self):
        expected_return = np.array([7.071, 7.071])
        actual_return = self._resolving_vectors.resolve_initial_input_velocity()

        np.testing.assert_almost_equal(expected_return, actual_return, 3)

