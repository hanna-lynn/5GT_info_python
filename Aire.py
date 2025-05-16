from math import pi

def menu():
  print("Bienvenu dans ce programme permettant de claculer l'aire de certaines formes.")
  print("Pour calculer l'aire d'un triangle, taper(1).")
  print("Pour calculer l'aire d'un carré, tapez(2).")
  print("Pour calculer l'aire d'un cercle, tapez(3).")
  print("Pour quitter, tapez (4)")

  choix=input ("Quel est votre choix?")
  choix=int(choix)

  if choix==1:
    aire_triangle()

  elif choix==2:
    aire_carré()

  elif choix==3:
    aire_cercle()

  elif choix==4:
    quitt()

  else:
    print ("Je n'ai rien compris.")

def aire_triangle():
  base=input ("Que vaut la base?")
  base=float (base)
  hauteur=input ("Que vaut sa hauteur?")
  hauteur=float (hauteur)
  aire= (base*hauteur)/2
  print()
  print("L'aire du triangle est de", aire, "m2.")
  menu()
  

def aire_carré():
  côté=input ("Que vaut le côté?")
  côté=float (côté)
  aire= (côté*côté)
  print()
  print("L'aire du carré est de", aire, "m2")
  menu()

def aire_cercle():
  rayon=input("Que vaut le rayon?")
  rayon=float(rayon)
  aire=round(rayon**2*pi,3)
  print()
  print("L'aire du cercle est de", aire,"m2")
  menu()

def quitt():
  print("Au revoir.")

if  __name__=="__main__":
    menu()
