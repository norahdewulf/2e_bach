class Geld:
    def __init__(self, bedrag):
        #als bedrag een integer is
        if isinstance(bedrag, int):
            if bedrag > 0:
                self.euros = bedrag
                #opgave: centen worden gelijkgesteld aan 0
                self.centen = 0
            #als het bedrag negatief is
            else:
                self.centen, self.euros = 0, 0
                print("Negatieve bedragen zijn niet toegelaten")

        #als bedrag een float is
        elif isinstance(bedrag, float):
            if bedrag > 0:
                self.euros = int(bedrag)
                self.centen = int((bedrag - self.euros) * 100) #wat er na de komma staat
            else:
                self.centen, self.euros = 0, 0
                print("Negatieve bedragen zijn niet toegelaten")

        #als bedrag een Geld object is
        elif isinstance(bedrag, Geld):
            self.centen = bedrag.centen
            self.euros = bedrag.euros

        #als bedrag een string is
        elif isinstance(bedrag, str):
            #ongeldige opmaak
            if "," and "€" not in bedrag or "-" in bedrag:
                self.centen, self.euros = 0, 0
                print("Opmaak Geld string niet correct")
            #geldige opmaak
            else:
                #symbool wegdoen
                gestript = bedrag.strip("€")
                #gestript = nieuwe bedrag
                #vervang de komma in gestript naar een punt
                vervang = gestript.replace(",", ".")
                #vervang = nieuwe bedrag
                #maak een float van de string vervang
                num = float(vervang)
                #num is ons finaal bedrag (wordt nu gezien als een float)
                self.euros = int(num)
                self.centen = int((num - self.euros) * 100)

    def get_centen(self):
        return self.centen

    def get_euros(self):
        return self.euros

    def __str__(self):
        return f"€{self.euros}.{self.centen:2d}" #die 2d zorgt ervoor dat centen altijd in 2 getallen weergegeven wordt

    def vermenigvuldig(self, n):
        nieuw_centen = self.centen * n
        nieuw_euros = self.euros * n
        nieuw_bedrag = nieuw_euros + nieuw_centen / 100
        return Geld(nieuw_bedrag)

    def optellen(self, g):
        nieuw_centen_opt = self.centen + g.centen
        nieuwe_euros_opt = self.euros + g.euros
        nieuw_bedrag_opt = nieuwe_euros_opt + nieuw_centen_opt / 100
        return Geld(nieuw_bedrag_opt)

bedrag1 = Geld(350.65)
print(str(bedrag1))