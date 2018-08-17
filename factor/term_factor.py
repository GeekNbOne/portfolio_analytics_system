from factor.factor import Factor
from scipy.interpolate import interp1d
import numpy as np

class TermFactor(Factor):

    def __init__(self, data_frame,how='optimum'):
        self._data_frame = data_frame
        self._how = how

    def term_price(self, date_context, maturity_date):


        tte = maturity_date.time_to_expiry(date_context)

        return self._interpolate(self.get_price_series(date_context),tte,date_context)

    def get_price_series(self,date_context):
        return self._data_frame.loc[date_context]

    def _interpolate(self, prices_series,tte,date_context):

        price_for_date =prices_series.values
        time_to_expiry = np.array([mat.time_to_expiry(date_context) for mat in prices_series.index])

        if self._how == 'optimum':
            return interp1d(time_to_expiry, price_for_date,bounds_error=False,fill_value= (price_for_date[0],price_for_date[-1]))(tte)
        elif self._how =='extrapolate':
            return interp1d(time_to_expiry, price_for_date,bounds_error=False, fill_value='extrapolate')(tte)
        else:
            raise NotImplementedError('How = {} is not implemented'.format(self._how))