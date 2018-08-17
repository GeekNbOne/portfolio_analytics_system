from abc import ABC, abstractmethod

class Model(ABC):

    @abstractmethod
    def present_value(self,date_context):
        pass



