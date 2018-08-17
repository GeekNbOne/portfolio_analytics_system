from abc import ABC, abstractmethod


class Statistic(ABC):

    def __init__(self,model):
        self._model = model

    @property
    def model(self):
        return self._model

    @property
    @classmethod
    def name(self):
        return None

    @abstractmethod
    def compute(self,date_context):
        pass
