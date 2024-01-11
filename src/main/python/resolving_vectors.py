import numpy as np


class ResolvingVectors:

    def __init__(self, initial_launch_velocity, launch_angle):
        self._initial_launch_velocity = initial_launch_velocity
        self._launch_angle = launch_angle
        self._angle_in_rad = np.radians(self._launch_angle)
    def resolve_initial_input_velocity(self):
        vx_resolved = self._initial_launch_velocity * np.cos(self._angle_in_rad)
        vy_resolved = self._initial_launch_velocity * np.sin(self._angle_in_rad)
        return np.array([vx_resolved, vy_resolved])

