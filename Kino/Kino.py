print("")
print("")
print("Witamy w symulatorze kina!")
print("===================================================================")
print("Dzień dobry! Poproszę o informację o wieku, budźecie i ilości osób?")
wiek = int(input("Podaj wiek najmlodszej osoby: "))
budzet = int(input("Ile masz pieniedzy? "))
osoby = int(input("Ile osób? "))



#dodaj()
cennik = [10, 12, 25, 20, 15, 20]


if wiek <= 5 and osoby <= 1:
    print("Maluszku przyjdź z kimś starszym.")
else:
    print("Możesz obejżeć Smerfy 10zl/os lub Gumisie 12zl/os")

    wybor = str("]")
    wybor = input("Którą bajkę wybierasz?...")
    if wybor == "Smerfy" and budzet >= cennik[0] * osoby:
        print("Dobrze. Oto twój/twoje ", osoby ,"bilet/y na ", wybor ,". Sala 5 miłego seansu.")
    elif wybor == "Gumisie" and budzet >= cennik[1] * osoby:
        print("Dobrze. Oto twój/twoje ", osoby ,"bilet/y na ", wybor ,". Sala 7 miłego seansu.")
    else:
        print("Nie masz wystarczającej ilości pieniędzy. Mamy nadzieję, że do nas wrócisz.")

if wiek >= 18:
    print("Mamy w ofercie Noc horrorów 25zl/os, Kino akcji 20zl/os")
    wybor1 = str("]")
    wybor1 = input("Którą film wybierasz?...")
    if wybor1 == "Noc horrorów" and budzet >= cennik[2] * osoby:
        print("Dobrze. Oto twój/twoje ", osoby ,"bilet/y na ", wybor1 ,". Sala 666 miłego seansu.")
    elif wybor == "Kino akcji" and budzet >= cennik[3] * osoby:
        print("Dobrze. Oto twój/twoje ", osoby ,"bilet/y na ", wybor1 ,". Sala 10 miłego seansu.")
    else:
        print("Nie masz wystarczającej ilości pieniędzy. Mamy nadzieję, że do nas wrócisz.")

if wiek > 5 and wiek <= 18:
    print("Mamy w ofercie Super auta 15zl/os, Królowa 20zl/os")
    wybor2 = str("]")
    wybor2 = input("Którą film wybierasz?...")
    if wybor2 == "Super auta" and budzet >= cennik[4] * osoby:
        print("Dobrze. Oto twój/twoje ", osoby ,"bilet/y na ", wybor2 ,". Sala 19 miłego seansu.")
    elif wybor == "Królowa" and budzet >= cennik[5] * osoby:
        print("Dobrze. Oto twój/twoje ", osoby ,"bilet/y na ", wybor2 ,". Sala 25 miłego seansu.")
    else:
        print("Nie masz wystarczającej ilości pieniędzy. Mamy nadzieję, że do nas wrócisz.")






