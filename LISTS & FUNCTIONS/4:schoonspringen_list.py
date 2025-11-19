#bij lees_scores() staat er niets tussen de haakjes wat er voor zorgt dat de input deel van de functie is
def lees_scores():
    list = []
    while True:
        #input is deel van de functie
        #vraagt een input zolang de while loop True is
        score = input()
        if score == 'stop':
            return list
            break
        list.append(int(score))

def bereken_score(scores): #scores is een lijst die aangemaakt is door bovenstaande functie
    scores_updated = [] #we maken een nieuwe lijst aan zonder de scores groter of gelijk aan 0 en kleiner of gelijk aan 100
    for i in scores:
        if 0 <= i <= 100:
            scores_updated.append(i)

    scores_updated = sorted(scores_updated)
    scores_updated = scores_updated[1:-1] #hoogste en laagste scores uitsluiten
    # andere manier:
    # scores_updated.remove(min(scores_updated))
    # scores_updated.remove(max(scores_updated))

    final_score = int(f"{sum(scores_updated) / len(scores_updated):.0f}") #bereken het gemiddelde
    return final_score

scores = lees_scores()
print(bereken_score(scores))