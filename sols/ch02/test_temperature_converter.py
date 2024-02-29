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
    (50.009, 10.01),
    (10000, 5537.78),
    (-459.67, -273.15),
    (31.9, -0.06),
    (32.1, 0.06),
    (211.9, 99.94),
    (212.1, 100.06),
    (-459.66, -273.14),
    (9999.9, 5537.72),
    (0, -17.78),
    (1, -17.22),
    (-40, -40)],
)
def test_param_input_expect_result(
        valid_input, 
        expected_result):
    assert convert(valid_input) == expected_result

def test_when_passed_459_pt_68_expect_AssertionError():
    with pytest.raises(AssertionError):
        convert(-459.68)

def test_when_passed_10000_pt_1_expect_AssertionError():
    with pytest.raises(AssertionError):
        convert(10000.1)

def test_when_passed_10000_pt_1_expect_AssertionError():
    with pytest.raises(AssertionError):
        convert(10000.1)

def test_when_passed_10000_pt_1_expect_raises_message():
    with pytest.raises(AssertionError) as actual_raises:
        convert(10000.1)
    assert 'Input cannot be greater than 10000' == str(actual_raises.value) 

def test_when_passed_459_pt_68_expect_raises_message():
    with pytest.raises(AssertionError) as actual_raises:
        convert(-459.68)
    assert 'Input cannot be below -459.67' == str(actual_raises.value) 
