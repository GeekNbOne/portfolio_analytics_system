from factor.term_factor import TermFactor
from model_library.model_properties.maturity_date import MaturityDate


class FutureFactor(TermFactor):

    def __init__(self,data_frame,future_maturity_object):
        super(FutureFactor, self).__init__(data_frame)
        self._future_maturity_object = future_maturity_object



    def get_price_series(self,date_context):
        series = self._data_frame.loc[date_context.pricing_date]

        fut_maturity = {index:MaturityDate(date) for index,date in enumerate(self._future_maturity_object.values(date_context.analysis_date),1)}

        series.rename(fut_maturity,inplace=True)

        return series








