class Verkeerslicht:
    def __init__(self, toestand = "rood"):
        self.toestand = toestand

    def __str__(self):
        return self.toestand

    def __repr__(self):
        return f"Verkeerslicht('{self.toestand}')"

    def volgende(self):
        if self.toestand == "rood":
            self.toestand = "groen"
        elif self.toestand == "groen":
            self.toestand = "oranje"
        else:
            self.toestand = "rood"

verkeer = Verkeerslicht()
print(str(verkeer)) #het staat op rood
verkeer.volgende() #switcht het licht naar groen
print(str(verkeer))
verkeer.volgende() #switcht het licth naar oranje
print(repr(verkeer))