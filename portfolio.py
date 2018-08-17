import pandas as pd

class Portfolio(object):


    def __init__(self,security_master,date_context):

        self._date_context = date_context
        self._security_master = security_master
        self._positions = {}
        self._positions_dimensions = {}

    class Position(object):

        def __init__(self,id,sm,amount,date_context):
            self._id = id
            self._sm = sm
            self._amount = amount
            self._date_context = date_context

        @property
        def id(self):
            return self._id
        @property
        def model(self):
            return self._sm['model']

        @property
        def quantity(self):
            return self._amount

    def positions(self):

        for id,position in self._positions.items():
            yield self.Position(id,self._security_master[id],position,self._date_context)

    def apply_statistic(self,*statistics):

        data = {}
        for stat in statistics:
            data[stat.name()] = {pos.id:stat(pos.model).compute(self._date_context) * pos.quantity for pos in self.positions()}

        return pd.DataFrame(data)










