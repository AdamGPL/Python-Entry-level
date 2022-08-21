print("Lekcja 12 - obsługa wyjątków (try, except)")

x = 12
y = 2 # 0

try:
    lista = [1]
    print(lista[0])
    print(x + 2)
    print(x / y)
    print("Linijka po")
#except ZeroDivisionError:
 #   print("Nie dziel cholero przez zero")
#except TypeError:
 #   print("Nie wykonuj działań na liczbach i znakach.")
except (ZeroDivisionError, TypeError):
    print("Wystąpił 1 z 2 błędów.")

except:
    print("Wystąpił nie spodziewany błąd")
finally:
    print("FINALLY i tak sie wykonam")

print("Dalsze instrukcje...")