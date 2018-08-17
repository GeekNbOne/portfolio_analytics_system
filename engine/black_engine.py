import numpy as np
from engine.option_engine import OptionEngine
from scipy.stats import norm


class BlackEngine(OptionEngine):

    def present_value(self, security, date_context):

        K = security.strike
        r = security.discount_rate(date_context)
        t = security.maturity_date.time_to_expiry(date_context)
        F = security.equity_factor.term_price(date_context, security.maturity_date)
        sigma = security.volatility(date_context)
        w = security.option_type

        return self._price(F,K,r,t,sigma,w)

    def present_value_for_volatility(self,sigma,security,date_context):
        K = security.strike
        r = security.discount_rate(date_context)
        t = security.maturity_date.time_to_expiry(date_context)
        F = security.equity_factor.term_price(date_context, security.maturity_date)
        w = security.option_type

        return self._price(F,K,r,t,sigma,w)



    def log_strike(self,security,date_context):
        K = security.strike
        F = security.equity_factor.term_price(date_context.pricing_date, security.maturity_date)
        return np.log(K/F)


    def _price(self,F,K,r,t,sigma,w):
        return w * np.exp(-r * t) * (
                F * norm.cdf(self._d1(F, K, t, sigma) * w) - K * norm.cdf(w * self._d2(F, K, t, sigma)))

    @staticmethod
    def _d1(F, K, t, sigma):
        return (np.log(F / K) + sigma ** 2 * 0.5 * t) / (sigma * np.sqrt(t))

    @staticmethod
    def _d2(F, K, t, sigma):
        return (np.log(F / K) - sigma ** 2 * 0.5 * t) / (sigma * np.sqrt(t))
