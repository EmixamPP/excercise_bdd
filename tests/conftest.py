import pytest
from temperature_control_unit.TemperatureControlUnit import TemperatureControlUnit

# Define a fixture to create an instance of TemperatureControlUnit
@pytest.fixture(scope="session")
def temperature_unit():
    # Initialize and return an instance of TemperatureControlUnit
    return TemperatureControlUnit()

# Use a hook to provide a custom marker for BDD features
def pytest_configure(config):
    config.addinivalue_line("markers", "bdd: mark a test as a BDD test")

# Define a hook to inject the application instance into BDD steps
@pytest.hookimpl(tryfirst=True)
def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    if "temperature_unit" in request.fixturenames:
        step_func(request.getfixturevalue("temperature_unit"))
