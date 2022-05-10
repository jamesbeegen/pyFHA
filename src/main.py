# Created by James Beegen
# 
# Based on HUD guidelines as of 5/10/2022

class FHA_Purchase():

    def __set_monthly_payment(self):
        # Monthly interest
        c = (self.__rate/100) / 12

        return self.__loan_amount * ((c*(1+c)**self.__term)/(((1+c)**self.__term) - 1))


    def __get_annual_MIP(self):
        if self.__term == 15:
            if self.__base_loan_amount > 625500:
                if self.__ltv > 95:
                    return self.__base_loan_amount * .0105
                else:
                    return self.__base_loan_amount * .01
            else:
                if self.__ltv > 95:
                    return self.__base_loan_amount * .0085
                else:
                    return self.__base_loan_amount * .008
        else:
            if self.__base_loan_amount > 625500:
                if self.__ltv > 90:
                    return self.__base_loan_amount * .0095
                elif 78 < self.__ltv <= 90:
                    return self.__base_loan_amount * .007
                else:
                    return self.__base_loan_amount * .0045
            else:
                if self.__ltv > 90:
                    return self.__base_loan_amount * .007
                else:
                    return self.__base_loan_amount * .0045


    def __init__(self, p, d, r, t, hhl=False, il=False):
        self.__price = p
        self.__down_payment_percent = d
        self.__ltv = 100 - self.__down_payment_percent
        self.__rate = r
        self.__term = t*12
        self.__hawaiian_home_lands = hhl
        self.__indian_lands = il
        self.__down_payment = p * (d/100)
        self.__base_loan_amount = self.__price * (self.__ltv/100)

        if self.__indian_lands:
            self.__upfront_MIP = 0
        else:
            self.__upfront_MIP = self.__base_loan_amount * .0175

        self.__loan_amount = self.__base_loan_amount + self.__upfront_MIP
        self.__monthly_MIP = self.__get_annual_MIP() / 12
        self.__monthly_payment = self.__set_monthly_payment() + self.__monthly_MIP

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
        '''.format(self.__price, self.__down_payment, self.__rate, self.__base_loan_amount, self.__upfront_MIP, self.__loan_amount, self.__monthly_payment, self.__monthly_payment - (self.__get_annual_MIP()/12), self.__get_annual_MIP()/12)