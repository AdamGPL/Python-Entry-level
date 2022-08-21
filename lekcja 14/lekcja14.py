print("Lekcja 14 - Podstawowe operacje na plikach (.txt)")

plik = open("test.txt", "a") # r / w+ / w / a
print(plik.writable())   # sprawdzenie czy plik jest do zapisu

if plik.writable():
    ile = plik.write(input("Wpisz hasło: ") + "\n")
    print("Zapisano: ", ile," znaki/ów.")
plik.close()

plik = open("test.txt", "r")

if plik.readable():
    print("Zawartość pliku:")
    for linia in plik:
        print(linia)