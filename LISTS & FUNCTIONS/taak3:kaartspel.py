import random

def kaartspel(seed):
    symbolen = ["Hearts", "Spades", "Diamonds", "Clubs"]
    waarden = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    #maakt een lijst aan van 52 kaarten (list comprehension => korter geschreven) (range(0,52) = 0,...,51 => 52 getallen/kaarten)
    deck = [x for x in range(0,52)]

    #moet je doen om een seed te kunnen genereren
    random.seed(seed)
    #shuffel de deck lijst zodat je deze lijst terugkrijgt met verschillende volgorde van de getallen 0 tot en met 52
    random.shuffle(deck)

    #we willen 4 kaarten uit het deck selecteren (range(4) = 0,1,2,3)
    #aangezien door de shuffle verschillende getallen altijd op verschillende indexen staan nemen we gewoon de eerste 4 getallen uit deze lijst en linken deze aan een symbool en een waarde
    for i in range(4):
        symbool = symbolen[deck[i] // 13]
        waarde = waarden[deck[i] % 13]
        print(f"Card number {deck[i]} is {waarde} of {symbool}")

kaartspel(1)
#voor verschillende waarden van seed zijn er verschillende random combinaties