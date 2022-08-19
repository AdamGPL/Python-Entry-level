print("Operatory logiczne (AND, OR, NOT)")

wiek = 11
kasa = 15
bilet = 30

if wiek >= 18 and kasa >= bliet:
    print("Możesz wejść.")
else:
    print("Nie mozesz wejsc")


if wiek <= 12 or kasa >= bilet:
    print("Możesz wejść z zniżka badz kupic zwykly bilet")
else:
    print("Nie mozesz wejsc na film dla dzieci")

if not wiek > 12 or kasa >= bilet:
    print("Zapraszamy")
else:
    print("Eh...")


if (True or False) and not False:      #operator and ma wyzszy priorytet niz or
    print("PRAWDA")
else:
    print("FAŁSZ")