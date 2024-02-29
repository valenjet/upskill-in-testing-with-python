# temperature_converter.py

def convert(fahrenheit: float) -> float:
    assert fahrenheit > -459.67

    celsius = (5 * (fahrenheit - 32)) / 9

    return float(round(celsius, 2))
