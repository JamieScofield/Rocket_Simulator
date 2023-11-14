from setuptools import setup, find_packages
import os
env = os.getenv('PROFILES', "local")

test_requires = [
    "mock",
    "pytest",
    "pytest-cov",
    "parameterized"
]