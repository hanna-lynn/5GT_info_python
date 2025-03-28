nombre = input("Bonjour, bienvenu dans ce programme de multiplication. De quel nombre voulez vous la table de multiplication ?")

nombre = int(nombre)

for i in range(1,11):
  print (i, "x", nombre, "=", i*nombre)
