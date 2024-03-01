import decimal

from decimal import Decimal

class Calculator:
    MaxTermInMonths = Decimal('360')
    MinPrincipalAmount = Decimal('1000')
    MaxPrincipalAmount = Decimal('1000000')
    PeriodsPerYear = Decimal('12')

    @staticmethod
    def compute_rate_per_period(annual_percentage_rate: Decimal) -> Decimal:
        if annual_percentage_rate < Decimal('0.01') or annual_percentage_rate >= Decimal('20.0'):
            raise ValueError(f"AnnualPercentageRate {annual_percentage_rate}% is not valid")

        rate_per_month = (Decimal(annual_percentage_rate) / Decimal('100')) / Calculator.PeriodsPerYear
        return rate_per_month.quantize(Decimal('.000001'), rounding=decimal.ROUND_HALF_UP)

    @staticmethod
    def compute_payment_per_period(principal_amount: Decimal, rate_per_period: Decimal, term_in_periods: Decimal) -> Decimal:
        if Decimal(term_in_periods) <= Decimal('0') or Decimal(term_in_periods) > Calculator.MaxTermInMonths:
            raise ValueError("termInPeriods is out of range")

        if Decimal(principal_amount) < Calculator.MinPrincipalAmount or Decimal(principal_amount) >= Calculator.MaxPrincipalAmount:
            raise ValueError(f"Principal {principal_amount} is not valid")

        # Convert rate_per_period to Decimal for type compatibility
        exponent_base = Decimal('1') + Decimal(rate_per_period)

        # Use Decimal's own exponentiation function instead of math.pow to avoid type incompatibility
        exponent = exponent_base ** Decimal(-1 * Decimal(term_in_periods))

        payment = (Decimal(rate_per_period) * Decimal(principal_amount)) / (Decimal('1') - Decimal(exponent))
        payment = payment.quantize(Decimal('.01'), rounding=decimal.ROUND_HALF_UP)

        return payment
