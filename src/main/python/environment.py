from equations import Equations


class Environment:

    def __init__(self, speed, max_time):
        self.equations = Equations()
        self.max_time = max_time
        self.speed = speed
        self.x_points_per_sec = []
    def run_simulation(self):
        time = 0
        initial_horizontal_x = 0

        while time < self.max_time:
            new_x = self.equations.calculate_distance_along_x_axis(self.speed)
            initial_horizontal_x += new_x
            self.x_points_per_sec.append(initial_horizontal_x)

            time += 1

        return print(self.x_points_per_sec)
