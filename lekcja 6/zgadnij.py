from random import randint
print("Zgadywator liczb 3000")
los = randint(1,10)
odp = -1
raz = 0
print("Zgadnij liczbę z przedziału od 1-10")

while odp != los:
    raz += 1
    odp = int(input("Podaj liczbę: "))
    if odp > los:
        print("Niestety wylosowana liczba jest mniejsza od twojej.")
    elif odp < los:
        print("Niestety wylosowana liczba jest większa od twojej.")
print("Brawo! Odgadłeś za", raz, "razem")

