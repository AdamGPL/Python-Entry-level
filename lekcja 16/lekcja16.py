print("Lekcja 16 - KROTKA (kolekcja), wycinki")



krotka = (2, 4, 8, 16, 32, 64, 128, "abc")


print(krotka[0])
print(krotka[6])
print(krotka)

print("Elementów:", krotka.count(2))
print("Index:", krotka.index(64))

print("\nWycinki:")
print(krotka[0])
print(krotka[3:5])
print(krotka[0:15])
print(krotka[-4:-1])
print(krotka[0:8:2])
print(krotka[0:])
print(krotka[:4:2])
print(krotka[::-1])
print(krotka[::-2])