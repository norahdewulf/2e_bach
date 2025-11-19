class BankRekening:
    def __init__(self, naam, rekeningnummer, bedrag = 0):
        self.naam = naam
        self.rekeningnummer = rekeningnummer
        self.bedrag = bedrag

    def __str__(self):
        return f"'{self.naam}, {self.rekeningnummer}, bedrag: {self.bedrag}'"

    def __repr__(self):
        return f"BankRekening('{self.naam}','{self.rekeningnummer}', {self.bedrag})"

    def storten(self, bedrag):
        #je kan alleen een positief bedrag overschrijven naar iemand
        if bedrag > 0:
            self.bedrag += bedrag
        else:
            print("ongeldig bedrag")

    def afhalen(self, bedrag):
        if bedrag > 0:
            self.bedrag -= bedrag
        else:
            print("ongeldig bedrag")

bankrekening1 = BankRekening("Hans Dewulf", "abcdefghijk", 99.98)
print(bankrekening1)
print(str(bankrekening1))
print(repr(bankrekening1))

print(bankrekening1.storten(400.10))
print(bankrekening1.bedrag)