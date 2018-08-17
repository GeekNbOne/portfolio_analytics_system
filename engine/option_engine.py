from engine.engine import Engine
from abc import ABC, abstractmethod
from scipy.optimize import newton


class OptionEngine(Engine, ABC):

    @abstractmethod
    def present_value_for_volatility(self, sigma, security, date_context):
        pass

    def vega_for_volatility(self, sigma, security, date_context):
        variation = 0.001
        f_down = self.present_value_for_volatility(sigma - variation, security, date_context)
        f_up = self.present_value_for_volatility(sigma + variation, security, date_context)

        return (f_up - f_down) / (variation * 2)

    def implied_volatility(self, security, date_context):

        price = security.price

        if price is None:
            raise ValueError('To use implied volatility factor, you need to supply a price for the option')

        if price < 0:
            raise ValueError('The price supplied in inferior to 0, option price shall be sent as a long position')

        error_fun = lambda sigma: self.present_value_for_volatility(sigma, security, date_context) - price
        f_prime = lambda sigma: self.vega_for_volatility(sigma, security, date_context)

        return newton(error_fun, security.initial_volatility, f_prime)
