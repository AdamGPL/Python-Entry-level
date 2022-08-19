print("Listy")

lista = [1, 2.5, "c", "d"]
print(lista)
print(lista[3])
lista[2]= 3
print(lista)

tekst = "Hello World"
print(tekst[0])

print(lista + ["f","g"])
print(lista * 3)
print("Ilość elementów: ", len(lista))

lista.append("f")
print(lista)
lista.append(["3", "u"])
print(lista)
print(lista[5][0])
lista.insert(3, 0)
print(lista)
print("Ilość: ", lista.count(3))
print("Index: ", lista.index("f"))
lista.remove("f")
print(lista)


lista2 = [1, 20, 35, -5, 0]
print("min: ", min(lista2))
print("max: ", max(lista2))
print(lista2)
lista2.sort()
print(lista2)
lista2.reverse()
print(lista2)
lista2.clear()
print(lista2)
#i = 0
#while i <= len(lista):
 #   print(lista[i])
  #  i += 1