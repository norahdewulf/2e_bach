jaar = int(input())

#enkel eeuwjaren deelbaar door 400 zijn schrikkeljaren!!!
#eeuwjaren zijn deelbaar door 100 met restwaarde 0! => apart stukje
#dus hieronder: geen eeuwjaar (n deelbaar door 100) OR wel eeuwjaar
if (jaar % 4 == 0 and jaar % 100 != 0) or (jaar % 400 == 0):
    print("schrikkeljaar")
else:
    print("geen schrikkeljaar")