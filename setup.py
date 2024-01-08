from setuptools import setup, find_packages



test_requires = [
    "mock",
    "pytest",
    "pytest-cov"
]
setup(
    name="Rocket_Simulator",
    version='0.5',
    author='Jamie Scofield',
    packages=find_packages(where="src/main/python"),
    tests_require=test_requires,
    install_requires=[
        "numpy",
        "matplotlib",
        test_requires
    ]
)