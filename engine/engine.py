from abc import ABC, abstractmethod

class Engine(ABC):

    @abstractmethod
    def present_value(self,security,date_context):
        pass