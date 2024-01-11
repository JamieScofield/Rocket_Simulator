from environment import Environment
from equations import Equations
from resolving_vectors import ResolvingVectors

launch_angle = 45
initial_launch_velocity = 25
env = Environment(100, ResolvingVectors(initial_launch_velocity, launch_angle), Equations())
env.run_environment()
