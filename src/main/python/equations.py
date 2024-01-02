


class Equations:

    gravitational_acceleration = -9.81

    def calculate_speed_along_x_axis(self, initial_x_speed):
        # acceleration is 0 in this context. so the distance travelled in a given second is the speed.
        return initial_x_speed

    def calculate_speed_along_y_axis(self, initial_y_speed: float):
        result = initial_y_speed + self.gravitational_acceleration
        return round(result, 3)

    def calculate_vertical_position_along_y_axis(self, y_velocity: float):
        result = y_velocity + (self.gravitational_acceleration/2)
        return round(result, 3)
