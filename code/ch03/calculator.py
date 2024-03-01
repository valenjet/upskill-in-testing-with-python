import decimal
from decimal import Decimal
import math

class Calculator:
    MaxTermInMonths = 360
    MinPrincipalAmount = Decimal('1000')
    MaxPrincipalAmount = Decimal('1000000')
    PeriodsPerYear = Decimal('12')

    @staticmethod
    def compute_rate_per_period(annual_percentage_rate):
        if annual_percentage_rate < Decimal('0.01') or annual_percentage_rate >= Decimal('20.0'):
            raise ValueError(f"AnnualPercentageRate {annual_percentage_rate}% is not valid")

        rate_per_month = (annual_percentage_rate / Decimal('100')) / Calculator.PeriodsPerYear
        return rate_per_month.quantize(Decimal('.000001'), rounding=decimal.ROUND_HALF_UP)

    @staticmethod
    def compute_payment_per_period(principal_amount, rate_per_period, term_in_periods):
        if term_in_periods <= 0 or term_in_periods > Calculator.MaxTermInMonths:
            raise ValueError("termInPeriods is out of range")

        if principal_amount < Calculator.MinPrincipalAmount or principal_amount >= Calculator.MaxPrincipalAmount:
            raise ValueError(f"Principal {principal_amount:,.2f} is not valid")

        exponent_base = float(Decimal('1') + rate_per_period)
        exponent = Decimal(math.pow(exponent_base, -1 * term_in_periods))

        payment = (rate_per_period * principal_amount) / (Decimal('1') - exponent)
        payment = payment.quantize(Decimal('.01'), rounding=decimal.ROUND_HALF_UP)

        return payment
