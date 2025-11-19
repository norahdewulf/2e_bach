naam = "Norah Dewulf"

naam2 = "hans dewulf"

omgekeerde_naam = naam[::-1]

print(omgekeerde_naam)

#alles in kleine letters naam[::-1].lower()
#alles in hoofdletters naam[::-1].upper()

#print(naam2.capitalize())

#islower() of isupper() returnen TRUE / FALSE statement
#vraag: zijn alle letters in 'omgekeerde_naam' kleine letter? => naam[::-1].islower() => FALSE

#naam[::-1].endswith("N") => TRUE
#naam[::-1].find("e") => 4 (index)
#rfind is als een letter meer dan een keer voorkomt en je de verste wilt aanduiden
#naam[::-1].replace("f", "d") => dluweD haroN
#omgekeerde_naam = naam[::-1].title() => Fluwed Haron => eerste letters van de string krijgen een hoofdletter, de rest worden kleine letters