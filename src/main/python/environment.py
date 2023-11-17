from equations import Equations


class Environment:

    def __init__(self, equations: Equations):
        self.equations = equations


    max_time = 100
    speed = 5

    def run_simulation(self):
        pass