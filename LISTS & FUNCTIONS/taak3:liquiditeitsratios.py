def calculate_current_ratio(activa, vorderingen_meer_dan_1_jaar, schulden_ten_hoogste_1_jaar, passiva):
    current_ratio = (activa - vorderingen_meer_dan_1_jaar) / (schulden_ten_hoogste_1_jaar + passiva)
    return f"De current ratio van de onderneming bedraagt: {round(current_ratio, 2)}"

def calculate_acid_test_ratio(activa, vorderingen_meer_dan_1_jaar, schulden_ten_hoogste_1_jaar, voorraden_biu):
    acid_test_ratio = (activa - vorderingen_meer_dan_1_jaar - voorraden_biu) / schulden_ten_hoogste_1_jaar
    return f"De acid test ratio van de onderneming bedraagt: {round(acid_test_ratio, 2)}"