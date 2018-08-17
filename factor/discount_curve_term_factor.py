from factor import DiscountFactor
from factor.term_factor import TermFactor
import numpy as np


class DiscountCurveTermFactor(DiscountFactor, TermFactor):

    def discount_factor(self,date_context, maturity_date):
        rate = self.tenor_rate(date_context.pricing_date, maturity_date)
        tte = maturity_date.time_to_expiry(date_context)

        return np.exp(- tte * rate)

    def tenor_rate(self, date_context, maturity_date):
        return self.term_price(date_context, maturity_date)
