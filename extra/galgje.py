class Galgje:
    def __init__(self, woord, beurten = 6):
        self.woord = woord
        if beurten == 0: #als de gebruiker 0 beurten in geeft wil dat zeggen dat hij maar evenveel gokken heeft als letters in het woord
            self.beurten = len(woord)
        else:
            self.beurten = beurten
        #de puntjes staan voor het aantal letters die we zoeken (en gevonden hebben) in het woord
        #is geen argument!
        self.gok = "." * len(woord)

    def __str__(self):
        if self.gok.lower() != self.woord.lower() and self.beurten > 1:
            return f"Je hebt nog {self.beurten} beurten.\n{self.gok}"

        #als je nog maar 1 beurt hebt dan mag je niet 'beurten' in de zin hebben maar 'beurt'
        elif self.gok.lower() != self.woord.lower() and self.beurten == 1:
            return f"Je hebt nog {self.beurten} beurt.\n{self.gok}"

        #als al je beurten op zijn
        else:
            if self.gok.lower() == self.woord.lower():
                #als self.gok == self.woord dan zal het aantal beurten gelijk worden aan 0 omdat je niet meer moet raden
                self.beurten = 0
                return f"Proficiat! Je hebt het woord geraden!\n{self.woord}"
            else:
                return f"Ai, je bent opgehangen.\n{self.woord}"

    def raadLetter(self, letter):
        #al de beurten zijn op en je hebt het woord n geraden
        # len(str(self.letter)) == 1, and
        if self.beurten == 0:
            print(f'Sorry, het spel is reeds voorbij.')
            return
        assert letter == str(letter) and len(str(letter)) == 1, f'argument is geen letter'
        assert letter not in self.gok, f'letter is al eens geprobeerd'

        if letter.lower() in self.woord.lower():
            i = 0
            self.gokNieuw = ""
            while i < len(self.woord):
                if letter == self.woord.lower()[i]:
                    self.gokNieuw = self.gokNieuw + self.woord[i]
                    i += 1
                else:
                    self.gokNieuw = self.gokNieuw + self.gok[i]
                    i += 1
            self.gok = self.gokNieuw
            print(f'Correct: letter {letter} komt {self.woord.lower().count(letter)} keer voor in het woord.\n{self.__str__()}')
        else:
            self.beurten -= 1
            print(f'Fout: letter {letter} komt niet voor in het woord.\n{self.__str__()}')