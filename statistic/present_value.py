from statistic.statistic import Statistic


class PresentValue(Statistic):

    def compute(self, date_context):
        return self.model.present_value(date_context)

    @classmethod
    def name(cls):
        return 'present_value'