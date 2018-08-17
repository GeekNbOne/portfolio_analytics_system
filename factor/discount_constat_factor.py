from factor.discount_factor import DiscountFactor


class DiscountConstantFactor(DiscountFactor):

    def __init__(self, rate):
        self._rate = rate

    def tenor_rate(self,date_context,maturity_date):
        return self._rate

