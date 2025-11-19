import datetime
import re

class Rijksregisternummer:
    def __init__(self, nummer):
        assert isinstance(nummer, str), "ongeldig type"
        nummer = re.sub(r'\D', '', nummer)  # Verwijder alle niet-cijferkarakters
        assert len(nummer) == 11, f"ongeldig formaat ({len(nummer)} {'cijfer' if len(nummer) == 1 else 'cijfers'})"
        self.nummer = nummer

    def __repr__(self):
        return f"Rijksregisternummer('{self.nummer}')"

    def __str__(self):
        return f"{self.nummer[:2]}.{self.nummer[2:4]}.{self.nummer[4:6]}-{self.nummer[6:9]}.{self.nummer[9:11]}"

    def geslacht(self):
        return 'vrouw' if int(self.nummer[6:9]) % 2 == 0 else 'man'

    def controlegetal(self, y2k=False):
        basis = int(self.nummer[:9])
        if y2k:
            basis += 2000000000
        controle = 97 - (basis % 97)
        return controle

    def geboortedatum(self):
        jaar = int(self.nummer[:2])
        maand = int(self.nummer[2:4])
        dag = int(self.nummer[4:6])

        controle_getal = int(self.nummer[9:11])
        controle_post2000 = 97 - ((int("2" + self.nummer[:9])) % 97)

        # Bepaal de eeuw
        if controle_getal == controle_post2000:
            eeuw = 2000
        else:
            eeuw = 1900

        # Valideer de datum
        try:
            datum = datetime.date(eeuw + jaar, maand, dag)
        except ValueError:
            # Datum is niet valide (bijvoorbeeld 30 februari), genereer foutmelding
            raise AssertionError("ongeldige geboortedatum")

        return datum

    def geldig(self):
        try:
            geboortedatum = self.geboortedatum()
            controle_getal = int(self.nummer[9:11])
            return controle_getal in [self.controlegetal(), self.controlegetal(True)]
        except:
            return False