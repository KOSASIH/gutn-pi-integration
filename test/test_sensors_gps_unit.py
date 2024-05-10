import pytest
from gutn_pi_integration.sensors.gps import GPS

@pytest.fixture
def gps():
    return GPS()

def test_gps_initialization(gps):
    assert isinstance(gps, GPS)

def test_gps_method(gps):
    result = gps.get_location()
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], float)
    assert isinstance(result[1], float)
