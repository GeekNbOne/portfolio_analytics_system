from factor.factor import Factor
from abc import ABC, abstractmethod



class VolatilityFactor(Factor,ABC):

    @abstractmethod
    def volatility(self,security,date_context):
        pass

