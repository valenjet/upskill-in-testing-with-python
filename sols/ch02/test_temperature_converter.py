# test_temperature_converter.py

import pytest
from temperature_converter import convert

@pytest.mark.parametrize("valid_input, expected_result", [
    (32, 0),
    (212, 100),
    (104, 40),
    (-4, -20),
    (105.8, 41),
    (105.6, 40.89),
    (36.815, 2.67),
    (221.1, 105.06),
    (50.009, 10.01)],
)
def test_param_input_expect_result(
        valid_input, 
        expected_result):
    assert convert(valid_input) == expected_result

def test_when_passed_459_pt_67_expect_AssertionError():
    with pytest.raises(AssertionError):
        assert  convert(-459.68)