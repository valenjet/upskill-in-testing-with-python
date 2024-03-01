import pytest

from decimal import Decimal
from calculator import Calculator

@pytest.mark.parametrize("principal, rate_per_period, term_in_periods, expected_payment_amount", [
    (7499, 0.001492, 113, Decimal('72.16')),
    (8753, 0.005442, 139, Decimal('89.93')),
    (61331, 0.005908, 359, Decimal('412.07')),
])
def test_compute_payment_with_provided_loan_data_expect_proper_monthly_payment(
        principal, 
        rate_per_period, 
        term_in_periods, 
        expected_payment_amount):
    # Act
    actual = Calculator.compute_payment_per_period(principal, rate_per_period, term_in_periods)

    # Assert
    assert actual == expected_payment_amount

@pytest.mark.parametrize("principal, rate_per_period, term_in_periods, expected_payment_per_period", [
    (7499, 0.001492, 0, 72.16),
    (7499, 0.001492, -1, 72.16),
    (7499, 0.001492, -2, 72.16),
    (7499, 0.001492, float('-inf'), 72.16),  # Adjusted to use float('-inf') as Python does not have int.MinValue
    (7499, 0.001492, 361, 72.16),
    (7499, 0.001492, 362, 72.16),
    (7499, 0.001492, float('inf'), 72.16),  # Adjusted to use float('inf') as Python does not have int.MaxValue
])
def test_compute_payment_with_invalid_term_in_months_expect_value_error(principal, rate_per_period, term_in_periods, expected_payment_per_period):
    with pytest.raises(ValueError):
        Calculator.compute_payment_per_period(principal, rate_per_period, term_in_periods)

@pytest.mark.parametrize("principal, rate_per_period, term_in_months, expected_payment_per_period", [
    (0, 0.001492, 360, 72.16),
    (999.99, 0.001492, 360, 72.16),
    (1000000, 0.001492, 360, 72.16),
    (4999999, 0.001492, 360, 72.16),
])
def test_compute_payment_with_invalid_principal_expect_value_error(principal, rate_per_period, term_in_months, expected_payment_per_period):
    with pytest.raises(ValueError):
        Calculator.compute_payment_per_period(principal, rate_per_period, term_in_months)

@pytest.mark.parametrize("annual_percentage_rate, expected_rate_per_period", [
    (1.79, 0.001492),
    (6.53, 0.005442),
    (7.09, 0.005908),
])
def test_rate_per_month_with_valid_annual_percentage_rate_expect_proper_rate_per_period(annual_percentage_rate, expected_rate_per_period):
    actual = Calculator.compute_rate_per_period(annual_percentage_rate)
    assert pytest.approx(actual, Decimal('0.000001')) == Decimal(expected_rate_per_period)

@pytest.mark.parametrize("annual_percentage_rate", [
    (0),
    (-1),
    (20.0),
    (21.1),
])
def test_rate_per_month_when_annual_percentage_rate_is_invalid_expect_value_error(annual_percentage_rate):
    with pytest.raises(ValueError):
        Calculator.compute_rate_per_period(annual_percentage_rate)

def test_max_term_in_months_always_expect_360():
    assert Calculator.MaxTermInMonths == 360
