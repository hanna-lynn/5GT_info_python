print("Bonjour et bienvenu dans ce programme qui vous dit bonjour.")

choix="o"

while choix=="o":
  print ("Bonjour!")
  choix = input("Voulez vous continuer ?")
  while choix not in ["o","n"]:
    choix = input("Veuillez répondre par oui (o) ou non (n) ")

print ("Au revoir!")
