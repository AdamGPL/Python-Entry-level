print("LEKCJA 2 - OPERATORY MATEMATYCZNE")
print("Kolejnosc:")
print((2 + 2) * 2)      #wychodzi 8 po zastosowaniu nawiasow
print("Dzielenie:")
print(5 / 2)      #zwraca float czyli liczby zmiennoprzecinkowe np. 2.5
print(5 // 2)     #zwraca int czyli liczba całkowita np. 2
print("Mnożenie:")
print(2 * 3)
print(2 ** 3)      #potegowanie
print("Skrocone operatory:")

x = 5
y = 0.5
x = x + 1    #przechowanie zmiennej
print(x)
x += y      #sposob skrocony na dzialania działa dla +-*/%
print(x)

print("Konwersja typów:")   #string - ciąg znaków
a = input("Podaj 1 liczbę:")  #input domyslnie przypisuje string
b = input("Podaj 2 liczbe:")
print(float(a) + float(b)) #float dla liczb zmienoprzecinkowych int dla calkowitych
b = 2
c = 5

print(str(b) + str(c))  #str - string ciag znakow
del c       #usuwanie zmiennej
#print(str(b) + str(c))   nie posługuj się zmienna po jej usunięciu