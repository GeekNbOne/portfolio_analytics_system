from factor.volatility_factor import VolatilityFactor


class VolatilityConstantFactor(VolatilityFactor):

    def __init__(self,volatility):
        self._volatility = volatility

    def volatility(self,security,date_context):
        return self._volatility
