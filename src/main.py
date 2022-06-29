# Created by James Beegen
# 
# Based on HUD guidelines as of 5/10/2022
class FHA_Loan(object):
    def set_monthly_payment(self):
        # Monthly interest
        c = (self.rate/100) / 12

        return self.loan_amount * ((c*(1+c)**self.term)/(((1+c)**self.term) - 1))

    def get_annual_MIP(self):
        if self.term == 15:
            if self.base_loan_amount > 625500:
                if self.ltv > 95:
                    return self.base_loan_amount * .0105
                else:
                    return self.base_loan_amount * .01
            else:
                if self.__ltv > 95:
                    return self.base_loan_amount * .0085
                else:
                    return self.base_loan_amount * .008
        else:
            if self.base_loan_amount > 625500:
                if self.ltv > 90:
                    return self.base_loan_amount * .0095
                elif 78 < self.ltv <= 90:
                    return self.base_loan_amount * .007
                else:
                    return self.base_loan_amount * .0045
            else:
                if self.ltv > 90:
                    return self.base_loan_amount * .007
                else:
                    return self.base_loan_amount * .0045

    def check_il(self):
        if self.indian_lands:
            self.upfront_MIP = 0
        else:
            self.upfront_MIP = self.base_loan_amount * .0175

    def __init__(self, p, r, t, hhl=False, il=False):
        self.price = p
        self.rate = r
        self.term = t*12
        self.hawaiian_home_lands = hhl
        self.indian_lands = il
        
        
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


class FHA_Refinance(FHA_Loan):
    def __init__(self, p, e, r, t, cash_out=0, hhl=False, il=False):
        super().__init__(p, r, t, hhl, il)
        self.equity = e
        self.cash_out = cash_out
        self.ltv = 100 - ((self.equity - self.cash_out)/self.price) * 100
        self.base_loan_amount = self.price * (self.ltv/100)
        super().check_il()
        self.loan_amount = self.base_loan_amount + self.upfront_MIP
        self.monthly_MIP = super().get_annual_MIP() / 12
        self.monthly_payment = super().set_monthly_payment() + self.monthly_MIP

    def __str__(self):
        return '''
        Home Value: ${:,.2f}
        Equity: ${:,.2f}
        Cash out: ${:,.2f}
        Interest Rate: {}%
        Base Loan Amount: ${:,.2f}
        Upfront MIP: ${:,.2f}
        Loan Amount: ${:,.2f}

        Monthly Payment:  ${:,.2f}
        Monthly P&I: ${:,.2f}
        Monthly MIP:  ${:,.2f}
        '''.format(self.price, self.equity, self.cash_out, self.rate, self.base_loan_amount, self.upfront_MIP, self.loan_amount, self.monthly_payment, self.monthly_payment - (super().get_annual_MIP()/12), super().get_annual_MIP()/12)

loan = FHA_Refinance(200000, 100000, 5, 30, cash_out = 2000)
print(loan)