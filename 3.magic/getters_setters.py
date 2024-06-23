class C:
    def __init__(self, kg: float):
        self._mass_kg = kg

    @property
    def mass_g(self):
        return self._mass_kg * 1000

    @mass_g.getter
    def mass_kg(self):
        return self._mass_kg

    @mass_g.setter
    def mass_g(self, mass_g: float):
        self._mass_kg = mass_g / 1000

    @mass_g.deleter
    def mass_g(self):
        del self._mass_kg


c = C(2)
assert c.mass_g == 2000
c.mass_g = 4000
assert c.mass_kg == 4
assert c.mass_g == 4000
