def annuiteit(bedrag, rentevoet, jaar):
    resultaat = (bedrag*rentevoet)/(1-(1+rentevoet)**(-jaar))

    return resultaat

def _aflossingstabel_rente(bedrag, rente, jaar):
    rentedelen = []
    kapitaal = bedrag
    aflossing = kapitaal / jaar #bedrag dat elk jaar afgelost moet worden
    for i in range(1,jaar+1): #"range(1, 6)"
        rentedeel = kapitaal * rente
        kapitaal -= aflossing #het deel dat in jaar i wordt afgelost mag ervan getrokken worden
        rentedelen.append(rentedeel)

    return rentedelen

def _aflossingstabel_kapitaal(bedrag, rente, jaar):
    kapitaaldelen = []
    annu = annuiteit(bedrag, rente, jaar) #annuiteit
    rentes = _aflossingstabel_rente(bedrag, rente, jaar) #rentedeel
    for i in range(1,jaar+1):
        kapitaaldeel = annu - rentes[i-1] #i-1 want op index O ([0]) staat het rentedeel van jaar 1
        kapitaaldelen.append(kapitaaldeel)

    return kapitaaldelen

def aflossingstabel_print(bedrag,rente,jaar):
    rentes = _aflossingstabel_rente(bedrag, rente, jaar)
    kapitalen = _aflossingstabel_kapitaal(bedrag, rente, jaar)
    annu = annuiteit(bedrag,rente,jaar)
    print("+------+----------+----------+----------+")
    for i in range(jaar):
        #i + 1 doen want range start bij 0 en eindigt bij jaar-1
        print(f"|{i+1:>5} | {annu:.2f} | {rentes[i]:8.2f} | {kapitalen[i]:8.2f} |")
    print("+------+----------+----------+----------+")

aflossingstabel_print(50000,0.05,5)