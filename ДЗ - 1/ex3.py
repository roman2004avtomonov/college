class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def to_pounds(self):
        return self.__kg * 2.205

obj = KgToPounds(10)
print(obj.kg)

obj.kg = 20
print(obj.kg)

obj.kg = '30'