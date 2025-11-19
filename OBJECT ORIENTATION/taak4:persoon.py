import datetime

class Persoon:
    def __init__(self, naam, voornaam, woonplaats, jaar_geboorte_datum, maand_geboorte_datum, dag_geboorte_datum):
        self.naam = naam
        self.voornaam = voornaam
        self.woonplaats = woonplaats
        self.geboortedatum = datetime.date(jaar_geboorte_datum, maand_geboorte_datum, dag_geboorte_datum)

    def get_naam(self):
        return self.naam

    def get_voornaam(self):
        return self.voornaam

    def get_woonplaats(self):
        return self.woonplaats

    def get_geboortedatum(self):
        return self.geboortedatum

    def set_voornaam(self, new_voornaam):
        self.voornaam = new_voornaam

    def set_woonplaats(self, new_woonplaats):
        self.woonplaats = new_woonplaats

    def is_ouder_dan(self, other_persoon):
        return self.geboortedatum > other_persoon.geboortedatum #zal TRUE / FALSE returnen

    def is_jonger_dan (self, other_persoon):
        return self.geboortedatum < other_persoon.geboortedatum

    def wonen_in_zelfde_satd(self, other_persoon):
        return self.woonplaats == other_persoon.woonplaats

persoon1 = Persoon("Janssens", "Jan", "Nederland", 2001, 11,11)
print(persoon1.get_geboortedatum())

persoon2 = Persoon("Rick", "Eric", "Frankrijk", 1999, 8, 11)

print(persoon1.is_ouder_dan(persoon2))