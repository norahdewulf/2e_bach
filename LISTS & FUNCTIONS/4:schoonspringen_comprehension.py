def bereken_score(scores):
    scores_updated = [i for i in scores if 0 <= i <= 100] #maak een geupdate lijst aan mbv list comprehension (kortere manier van schrijven)

    scores_updated = sorted(scores_updated)
    scores_updated = scores_updated[1:-1] #hoogste en laagste scores uitsluiten
    # andere manier:
    # scores.remove(min(scores))
    # scores.remove(max(scores))

    final_score = int(f"{sum(scores_updated) / len(scores_updated):.0f}") #gemiddelde berekenen
    return final_score

print(bereken_score([100, 0, 55, 56, 102]))
print(bereken_score([100, 0, 55, 56]))
#beide zelfde output => goede test