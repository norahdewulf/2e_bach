import calendar

#bovenste deel van de kalender
def print_month_title(jaar, maand):
    naammaand = calendar.month_name[maand]  # Haalt de naam van de maand op
    print(f"          {naammaand}   {jaar}")  # Drie spaties aan het begin voor centreren
    print("-" * 29)
    print(" Mon Tue Wed Thu Fri Sat Sun")

#lichaam van de kalender (de cijfertjes)
def print_month_body(jaar, maand):
    kalendermaand = calendar.monthcalendar(jaar, maand)
    for week in kalendermaand:
        # Print elke dag of een lege plek als het 0 is
        print("".join(f"{dag:>4}" if dag != 0 else "    " for dag in week))

#gebruik de eerder gedefinieerde functies in deze functie
#drukt volledige kalender af
def print_month(jaar, maand):
    print_month_title(jaar, maand)
    print_month_body(jaar, maand)

print_month(2025, 1)