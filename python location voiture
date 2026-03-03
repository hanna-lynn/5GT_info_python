from datetime import datetime
def prod_list_voiture():
    """Lecture du fichier contenant les informations et production d'une liste où chaque élément est un dict contenant les informations d'un véhicule"""
    list_voitures=[]
    with open('voitures_location.tsv', 'r', encoding='utf8') as f: #pour ouvrir un fichier en python
        for ligne in f:
           dict_datas={} #on peut aussi mettre dict() {} a la place de {}
           datas=ligne.strip().split('\t')
           dict_datas['id']=int(datas[0])
           dict_datas['moteur']=datas[1].lower()
           dict_datas['kilometrage']=int(datas[2])
           dict_datas['marque']=datas[3]
           dict_datas['place']=int(datas[4])
           dict_datas['annee']=int(datas[5])
           list_voitures.append(dict_datas)
    return list_voitures
def old_cars():
    """crée une liste des voitures trop vielles, cad les voitures de plus de 10ans et de plus de 5000km"""
    list_old_cars=[]
    now=datetime.now()
    current_year=now.year
    for voiture in list_voitures :
        age=current_year-voiture['annee']
        if (age>10) & (voiture['kilometrage']>5000):
            list_old_cars.append(voiture['id'])
    return list_old_cars
def sport_cars():
    """crée une liste des voitures trop sportives, cad les voitures de plus de 2 ou 4 ans et fonctionnant à l'essence"""
    list_sport_cars=[]
    list_old_cars=old_cars()
    for voiture in list_voitures :
        if (voiture['place']<5) & (voiture['moteur']=='essence'):
            if voiture['id'] not in list_old_cars:
                list_sport_cars.append(voiture['id'])
    return list_sport_cars
def print_list_cars(list_selected_cars,list_name):
    print(f"voici la liste des voitures {list_name} :") 
    
    for car in list_selected_cars:
        print(car)
        
        def print_engine_type():
      dict_carburant={}
    
    for voiture in list_voitures:
        moteur=voiture['moteur']
       if moteur not in dict_carburant.keys():
           dict_carburant['moteur']=[]
       dict_carburant[moteur].append(voiture['id'])
    print (dict_carburant)
   
   max_lenght=len(dict_carburant)['diesel'],len(dict_carburant['essence']),len(dict_carburant['électrique']
            
    print(40*'=')
    print("|   essence   |   diesel   | électrique |")
    print(40*'-')
    
    for i in range (max_lenght):
        print("|",end="")
        try:
            car_id=dict_carburant['diesel'][i]
            blanks=12-len(str(car_id))                                                                   
            print(car_id,end="")                                                                         
        except:
            print("            ",end="")
        print(("|",end="")                                                                       
        print()                                                                       
        
        try:                                                                    
            car_id=dict_carburant['essence'][i]
            blanks=12-len(str(car_id))                                                                   
            print(car_id,end="")                                                                    
        except:
            print("            ",end="")
        print(("|",end="")
        print()
              
              
        try:                                                                    
            car_id=dict_carburant['électrique'][i]
            blanks=12-len(str(car_id))                                                                   
            print(car_id,end="")                                                                         
        except:
            print("            ",end="")
        print(("|",end="")
        print()
          
def menu():
    print("pour afficher les véhicules trop anciens, tapez 1")
    print("pour afficher une liste des véhicules par type de carburant, tapez 2")
    print("pour afficher une liste des voitures de sport, tapez 3")
    print("pour enregistrer un nouveau véhicule de la liste, tapez 4")
    print("pour supprimer un véhicule de la liste, tapez 5")
    print("pour enregistrer la liste dans un fichier, tapez 6")
    choix=input("votre choix: ")
    try :
        choix=int(choix)
    except:
        menu()
    while choix not in [1,2,3,4,5,6]:
        print("veuillez choisir un nombre entre 1 et 6")
        choix=input("votre choix: ")
        choix=int(choix)
        try :
            choix=int(choix)
        except:
            menu()
    
    if choix==1:
        list_old_cars=old_cars()
        print_list_cars(list_old_cars,"trop vielles")
    
    elif choix==3:
         list_sport_cars=sport_cars()
         print_list_cars(list_sport_cars,"sportives")
            
if __name__=="__main__":
    list_voitures=prod_list_voiture()
    menu()
    
     # for voiture in list_voitures : # 'voiture' est le nom d'une variable temporaire défini par 'for in liste', pourrait avoir n'import quel nom
        #si on met juste print(voiture) il affiche une list structuré.
        #si on met print(voiture ['marque']) il affiche just la marque.
        #si on met print(voiture.values())= list des valeurs pour chaque voiture.
        #si on met print(voiture.keys())= juste les nom des 'list'
