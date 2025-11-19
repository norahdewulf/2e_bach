class Verwarming:
    def __init__(self, naam, temperatuur = 10.0, minimum = 0.0, maximum = 100.0):
        self.naam = naam
        self._temperatuur = temperatuur
        self.minimum = minimum
        self.maximum = maximum

    def __str__(self):
        return f"{self.naam}: huidige temperatuur: {self._temperatuur:.1f}; toegelaten min: {self.minimum:.1f}; toegelaten max: {self.maximum:.1f}"

    def __repr__(self):
        #vergeet niet af te ronden op 1 getal na de komma
        return f"Verwarming('{self.naam}', {self._temperatuur:.1f}, {self.minimum:.1f}, {self.maximum:.1f})"

    def get_temperatuur(self):
        return self._temperatuur

    def temperatuur(self):
        return float(f"{self._temperatuur:.1f}")

    def wijzig_temperatuur(self, n):
        self._temperatuur += n
        if self._temperatuur < self.minimum:
            self._temperatuur = self.minimum
        elif self._temperatuur > self.maximum:
            self._temperatuur = self.maximum

verwarming1 = Verwarming("keuken")
print(str(verwarming1))
print(repr(verwarming1))
print(verwarming1.get_temperatuur())
verwarming1.wijzig_temperatuur(2)
print(verwarming1.temperatuur())
verwarming1.wijzig_temperatuur(-20)
print(verwarming1.temperatuur())
print(verwarming1.minimum)
