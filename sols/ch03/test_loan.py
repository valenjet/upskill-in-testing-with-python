# test_loan.py

from loan import Loan

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
        assert actual == 126.39
