from abc import ABC, abstractmethod
import numpy as np


class DiscountFactor(ABC):

    def discount_factor(self, date_context, maturity_date):
        tte = maturity_date.time_to_expiry(date_context)
        return np.exp(-self.tenor_rate(date_context, maturity_date) * tte)

    @abstractmethod
    def tenor_rate(self, date_context, maturity_date):
        pass
