from equations import Equations
import numpy as np
import matplotlib.pyplot as plt

from resolving_vectors import ResolvingVectors


class Environment:

    def __init__(self, max_time, resolving_vectors: ResolvingVectors, equations: Equations):
        self.equations = equations
        self.resolving_vectors = resolving_vectors
        self.max_time = max_time
        self.x_points_per_sec = []
        self.y_points_per_sec = []
        self._initial_resolved_x_velocity = resolving_vectors.resolve_initial_input_velocity()[0]
        self._initial_resolved_y_velocity = resolving_vectors.resolve_initial_input_velocity()[1]

        
    def run_environment(self):
        self.simulation()
        self._creating_plot()

    def simulation(self):
        time = 0
        initial_x_position = 0
        initial_y_position = 0
        y_velocity = self._initial_resolved_y_velocity

        while time < self.max_time:
            new_x = self.equations.calculate_speed_along_x_axis(self._initial_resolved_x_velocity)

            new_y = self.equations.calculate_vertical_position_along_y_axis(y_velocity)
            y_velocity = self.equations.calculate_speed_along_y_axis(y_velocity)

            initial_x_position += new_x
            initial_y_position += new_y

            self.x_points_per_sec.append(initial_x_position)
            self.y_points_per_sec.append(initial_y_position)

            time += 1

            if initial_y_position < 0:
                break
    def _creating_plot(self):
        positional_x_axis_array = np.array(self.x_points_per_sec)
        positional_y_axis_array = np.array(self.y_points_per_sec)

        plt.plot(positional_x_axis_array, positional_y_axis_array)
        plt.show()
