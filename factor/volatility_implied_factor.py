from factor.volatility_factor import VolatilityFactor



class VolatilityImpliedFactor(VolatilityFactor):

    def volatility(self,security,date_context):

        return security.implied_volatility(date_context)