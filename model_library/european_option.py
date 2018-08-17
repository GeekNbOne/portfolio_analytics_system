from model_library.model import Model


class EuropeanOption(Model):

    def __init__(self, maturity_date, strike, is_call, equity_factor, discount_factor, volatility_factor, engine
                 , price=None, initial_volatility=0.2, multiplier=100):
        if not maturity_date.__class__.__name__ == 'MaturityDate':
            raise TypeError('The parameter maturity_date shall be an objetc of class MaturityDate')

        self._maturity_date = maturity_date
        self._strike = strike
        self._equity_factor = equity_factor
        self._discount_factor = discount_factor
        self._volatility_factor = volatility_factor
        self._is_call = is_call
        self._engine = engine
        self._multiplier = multiplier
        self._price = price
        self._initial_volatility = initial_volatility

    @property
    def maturity_date(self):
        return self._maturity_date

    @property
    def option_type(self):
        return 1 if self._is_call else -1

    @property
    def strike(self):
        return self._strike

    @property
    def equity_factor(self):
        return self._equity_factor

    @property
    def initial_volatility(self):
        return self._initial_volatility

    @property
    def price(self):
        return self._price

    def present_value(self, date_context):
        return self._engine.present_value(self, date_context) * self._multiplier

    def implied_volatility(self, date_context):
        return self._engine.implied_volatility(self, date_context)

    def volatility(self, date_context):
        return self._volatility_factor.volatility(self, date_context)

    def discount_rate(self, date_context):
        return self._discount_factor.tenor_rate(date_context, self._maturity_date)
