# loan.py

from calculator import Calculator

class Loan:
    MAX_TERM_IN_MONTHS = 360

    principal: int = 0
    annual_percentage_rate: int = 0

    def __init__(self, principal: int, annual_percentage_rate: int):
        self.principal = principal
        self.annual_percentage_rate = annual_percentage_rate

    def compute_payment(self, term_in_months: int):
        # a term_in_months outside expected boundaries raises a ValueError
        if term_in_months <= 0:
            raise ValueError("Parameter 'term_in_months' must be greater than 0.")

        # a term_in_months cannot be greater than the max term in months
        if term_in_months > self.MAX_TERM_IN_MONTHS:
            raise ValueError(f"Parameter 'term_in_months' must be less than or equal to {self.MAX_TERM_IN_MONTHS}.")
        
        principal = self.principal
        # dividing the annual interest rate by the number of periods in a year
        rate_per_period = self.annual_percentage_rate / 1200

        payment = Calculator.compute_payment_per_period(principal, rate_per_period, term_in_months)

        return payment