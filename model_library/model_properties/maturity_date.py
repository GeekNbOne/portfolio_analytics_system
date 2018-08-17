import warnings
import pandas as pd


class MaturityDate(object):

    def __init__(self, exact_date=None, constant_maturity=None, constant_maturity_time_basis=1):
        """
        :param exact_date:
        :param constant_maturity:
        :constant_maturity_time_basis: Time basis is the conversion of yearly time to another time scale
        e.g 5 years * 365 time_basis = 1825 (days), only applies to constant_maturity
        """

        if exact_date is None and constant_maturity is None:
            raise ValueError('You need to supply exact_date or constant_maturity')

        data_count = sum([1 if date is not None else 0 for date in [exact_date, constant_maturity]])

        if data_count > 1:
            warnings.warn(
                'More than one type of maturity has been supplied, exact date will be prioritize, then constant maturity')

        self._exact_date = pd.to_datetime(exact_date)
        self._constant_maturity = constant_maturity
        self._constant_maturity_time_basis = constant_maturity_time_basis

    def time_to_expiry(self, date_context, time_basis=1):

        if self._exact_date is not None:
            return (self._exact_date - date_context.analysis_date).days / 365.0 * time_basis
        else:
            return self._constant_maturity / self._constant_maturity_time_basis * time_basis

    def __str__(self):
        if self._exact_date is not None:
            return self._exact_date.strftime('%Y%m%d')
        else:
            return '{} years'.format(round(self._constant_maturity / self._constant_maturity_time_basis, 2))
