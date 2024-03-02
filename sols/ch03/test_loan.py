# test_loan.py

import sys
import pytest

from loan import Loan
from decimal import Decimal

class TestLoan():

    def test_compute_payment_with_provided_loan_data_expect_proper_payment_amount(self):
        # Arrange
        loan = Loan(
            principal=12000,
            annual_percentage_rate=12
        )

        # Act
        actual = loan.compute_payment(300)

        # Assert
        assert actual == Decimal('126.39')

def test_compute_payment_when_invalid_term_in_months_is_zero_expect_value_error():
    """
    Test that providing a zero value for term_in_months to compute_payment raises a ValueError.
    """
    # Arrange
    class_under_test = Loan(principal=7499, annual_percentage_rate=1.79)

    # Act
    with pytest.raises(Exception) as exc_info:
        class_under_test.compute_payment(0)

    # Assert
    assert exc_info.type == ValueError


def test_compute_payment_when_invalid_term_in_months_is_zero_expect_exc_with_param_name():
    """
    Test that providing a zero value for term_in_months to compute_payment raises message with the parameter name.
    """
    # Arrange
    loan = Loan(principal=7499, annual_percentage_rate=1.79)

    # Act
    with pytest.raises(Exception) as exc_info:
        loan.compute_payment(0)

    # Assert
    assert "term_in_months" in str(exc_info.value), "Expected an error for invalid 'term_in_months' parameter"


MAX_INT = sys.maxsize
MIN_INT = ~sys.maxsize

@pytest.mark.parametrize("principal, annual_percentage_rate, term_in_months", [
    (7499, 1.79, 0),
    (7499, 1.79, -1),
    (7499, 1.79, -73),
    (7499, 1.79, MIN_INT),
    (7499, 1.79, Loan.MAX_TERM_IN_MONTHS + 1),
    (7499, 1.79, Loan.MAX_TERM_IN_MONTHS * 5),
    (7499, 1.79, MAX_INT),
])
def test_compute_payment_with_invalid_term_in_months_expect_value_error_exception(
        principal, annual_percentage_rate, term_in_months):

    # Arrange
    loan = Loan(principal, annual_percentage_rate)
    
    # Act & Assert
    with pytest.raises(ValueError):  # expect the ValueError exception
        loan.compute_payment(term_in_months)


# Data-drive the test function with multiple data sets
@pytest.mark.parametrize("principal, annual_percentage_rate, term_in_months, expected", [
    (7499, 1.79, 113, Decimal('72.16')),
    (8753, 6.53, 139, Decimal('89.92')), # use prime or arbitrary numbers in test data
    (61331, 7.09, 359, Decimal('412.08')),
])
def test_compute_payment_with_provided_loan_data_expect_proper_monthly_payment(
        principal, annual_percentage_rate, term_in_months, expected):
    """
    Test to verify that the Loan.compute_payment method calculates the correct 
    monthly payment given specific loan data.
    """
    # Arrange
    loan = Loan(principal, annual_percentage_rate)

    # Act
    actual = loan.compute_payment(term_in_months)

    # Assert
    assert actual == expected, "Computed payment does not match the expected payment."
