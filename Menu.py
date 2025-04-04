print ("Bienvenu dans notre restaurant.")

print ("Pour un hamburger, tapez 1")

print("Pour une pizza, tapez 2")

print ("Pour une salade, tapez 3")

choix = input("Votre choix: ")

choix = int(choix)
while choix not in [1,2,3]:
  print("Veuillez choisir 1,2 et 3")
  choix = input("Votre choix: ")
  choix = int(choix)

if choix==1:
  print ("Vous avez choisi un hamburger.")

elif choix==2:
  print ("Vous avez choisi une pizza.")

elif choix==3:
  print ("Vous avez choisi une salade.")

else:
  pass

print ("Bonne appetit!!!")
