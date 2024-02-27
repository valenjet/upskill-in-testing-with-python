# test_temperature_converter.py

from temperature_converter import convert

def test_when_passed_32_expect_0():
    assert convert(32) == 0

def test_when_passed_212_expect_100():
    assert convert(212) == 100

def test_when_passed_104_expect_40():
    assert convert(104) == 40

def test_when_passed_minus_4_expect_minus_20():
    assert convert(-4) == -20
