print("Lekcja 9 - funkcje")

def nazwa_funkcji():
    print("Funkcja")


nazwa_funkcji()


def dodaj():
    print(x * 1)



#v = 10
#a = int(input("Wpisz cyfre..."))
#def dodaj():
 #   print(v * a)

#dodaj()


def ddodaj(x, y = 1, z = 0):
    print("Czy ja istnieje?")
    return x + y + z
    #print("Czy ja istnieje?")

print(ddodaj(2, 2))
print(ddodaj(2))
wynik = ddodaj(2, 2, 5)

print(wynik)