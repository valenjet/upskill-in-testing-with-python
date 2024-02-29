# temperature_converter.py

# these are physical constants
ABS_ZERO_CELSIUS = -273.15
ABS_ZERO_FAHRENHEIT = -459.67

# limit the input
MAX_FAHRENHEIT = 10000

def convert(fahrenheit: float) -> float:
    # short-circuit for absolute zero
    if fahrenheit == ABS_ZERO_FAHRENHEIT:
        return ABS_ZERO_CELSIUS

    # guard against invalid input
    assert fahrenheit <= MAX_FAHRENHEIT, f'Input cannot be greater than {MAX_FAHRENHEIT}'
    assert fahrenheit > ABS_ZERO_FAHRENHEIT, f'Input cannot be below {ABS_ZERO_FAHRENHEIT}'

    # this is the mathematical formula
    celsius = (5 * (fahrenheit - 32)) / 9

    # be sure to round to 2 decimal places
    return round(celsius, 2)
