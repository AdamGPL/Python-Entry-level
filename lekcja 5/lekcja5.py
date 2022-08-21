print("Lekcja 5 - petla while, instrukcje skoku (break, continue)")

i = 0

# while - wykonuj dopuki

while i <= 5:
    print(i)
    i += 1
print("koniec")


a = 0
while True:
    print(a)
    a += 1
    if a > 10:
        break
print("koniec")

b = 0
while True:
    b += 1
    if b % 2 == 1:      #liczba nieparzysta == 1 / parzysta == 0
        continue
    print(b)
    if b >= 10:
        break
print("koniec")
