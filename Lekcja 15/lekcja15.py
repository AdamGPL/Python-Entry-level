print("Lekcja 15 - słownik (kolekcja) - dictionary")

slownik = {1: "Poniedziałek", 2: "Wtorek", 7: "Niedziela"}


print(slownik[7])
print(slownik[1])
slownik[3] = "Środa"
slownik[4] = False
slownik[5] = 4.3
print(slownik)

slownik["a"] = 1
print(slownik["a"])
print(slownik)

#print(slownik[8])
print(slownik.get(7, "Inny dzien."))

print("\nPetla:")
for linia in slownik.values():
    print(linia)


print("===============")
print(slownik.pop(1))
print(slownik)
