import pandas as pd

class DateContext(object):

    def __init__(self,analysis_date,pricing_date = None):
        self._analysis_date = pd.to_datetime(analysis_date)

        if pricing_date is None:
            self._pricing_date = self._analysis_date
        else:
            self._pricing_date = pd.to_datetime(pricing_date)


    @property
    def analysis_date(self):
        return self._analysis_date

    @property
    def pricing_date(self):
        return self._pricing_date