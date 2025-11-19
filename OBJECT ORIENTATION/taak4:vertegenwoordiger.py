class Vertegenwoordiger:
    def __init__(self, naam = "", omzet = 0.0):
        self.naam = naam
        self.omzet = omzet

    def get_naam(self):
        return self.naam

    def get_omzet(self):
        return self.omzet

    def set_naam(self, naam):
        self.naam = naam

    def set_omzet(self, omzet):
        self.omzet = omzet

    def __str__(self):
        return f"Vertegenwoordiger[naam='{self.naam}',omzet={self.omzet}]"

vertegenwoordiger = Vertegenwoordiger("Jan Janssens", 567.89)
print(vertegenwoordiger.get_naam())
print(vertegenwoordiger.get_omzet())
vertegenwoordiger.set_naam("Hans Dewulf")

#stringfunctie oproepen:
print(vertegenwoordiger.__str__())
#andere manier van de stringfunctie op te roepen:
print(str(vertegenwoordiger))
#nog een andere manier:
print(vertegenwoordiger)