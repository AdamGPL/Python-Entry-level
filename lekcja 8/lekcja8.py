print("Lekcja 8 pętla obiektowa FOR, funkcja range")

lista = ["Siemanko", "witam", "w", "python"]


i = 0

while i < len(lista):
    print(lista[i])
    i += 1          #petla  nieobietkowa

#for - przez

for x in lista:
    print(x)           #petla obiektowa


print(list(range(10)))      #range to
print("--------------------------")
for y in range(1,20, 4):
    print(y)
