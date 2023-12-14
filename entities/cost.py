class Cost:
    def __init__(self, name, type, money):
        self._name= name
        self._type = type
        self._money = money

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, type):
        self._type = type

    @property
    def money(self):
        return self._money
    @money.setter
    def money(self, money):
        self._money = money