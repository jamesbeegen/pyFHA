# Created by James Beegen
# 
# Based on HUD guidelines as of 5/10/2022
from FHA_Loan import FHA_Loan

class FHA_Purchase(FHA_Loan):
    def __init__(self, p, d, r, t, hhl=False, il=False):
        super().__init__(p, r, t, hhl, il)
        self.down_payment_percent = d
        self.ltv = 100 - self.down_payment_percent
        self.down_payment = p * (d/100)
        self.base_loan_amount = self.price * (self.ltv/100)
        super().check_il()
        self.loan_amount = self.base_loan_amount + self.upfront_MIP
        self.monthly_MIP = super().get_annual_MIP() / 12
        self.monthly_payment = super().set_monthly_payment() + self.monthly_MIP

    def __str__(self):
        return '''
        Purchase Price: ${:,.2f}
        Down Payment: ${:,.2f}
        Interest Rate: {}%
        Base Loan Amount: ${:,.2f}
        Upfront MIP: ${:,.2f}
        Loan Amount: ${:,.2f}

        Monthly Payment:  ${:,.2f}
        Monthly P&I: ${:,.2f}
        Monthly MIP:  ${:,.2f}
        '''.format(self.price, self.down_payment, self.rate, self.base_loan_amount, self.upfront_MIP, self.loan_amount, self.monthly_payment, self.monthly_payment - (super().get_annual_MIP()/12), super().get_annual_MIP()/12)