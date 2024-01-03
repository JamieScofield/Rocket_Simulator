from equations import Equations


class Environment:

    def __init__(self, x_speed, y_speed, max_time):
        self.equations = Equations()
        self.max_time = max_time
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.x_points_per_sec = []
        self.y_points_per_sec = []
    def run_simulation(self):
        time = 0
        initial_x_position = 0
        initial_y_position = 0
        y_velocity = self.y_speed

        while time < self.max_time:

            new_x = self.equations.calculate_speed_along_x_axis(self.x_speed)

            new_y = self.equations.calculate_vertical_position_along_y_axis(y_velocity)
            y_velocity = self.equations.calculate_speed_along_y_axis(y_velocity)

            initial_x_position += new_x
            initial_y_position += new_y

            self.x_points_per_sec.append(initial_x_position)
            self.y_points_per_sec.append(initial_y_position)

            time += 1

        return print(self.x_points_per_sec)
