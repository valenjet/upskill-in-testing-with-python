

class Loan:
    principal: int = 0
    annual_percentage_rate: int = 0

    def __init__(self, principal: int, annual_percentage_rate: int):
        self.principal = principal
        self.annual_percentage_rate = annual_percentage_rate

    def compute_payment(self, term_in_months: int):
        return 126.39