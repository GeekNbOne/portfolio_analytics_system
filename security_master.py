class SecurityMaster(object):

    def __init__(self):

        self._securities = {}
        self._autogenerated_id = 0

    def add_security(self, model, id=None, **dimensions):

        self._validate_dimensions(dimensions)

        if id is None:
            id = self._generate_id()

        self._securities[id] = {'model': model}
        self._securities[id].update(dimensions)

    def __getitem__(self, item):
        return self._securities[item]

    def _generate_id(self):

        while self._autogenerated_id in self._securities:
            self._autogenerated_id += 1

        return self._autogenerated_id

    def _validate_dimensions(self,dimensions):
        if 'model' in dimensions:
            raise KeyError('model is a restricted dimension name')