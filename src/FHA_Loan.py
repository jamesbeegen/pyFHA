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