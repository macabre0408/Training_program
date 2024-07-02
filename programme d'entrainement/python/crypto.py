import string


#tu comprendras surmement
# string.ascii_lowercase toutes les minuscule
# string.ascii_uppercase toutes les majuscule
# renvoie les 2 : string.ascii_letters

def cesar(mot,operation=1,k=3):
    word=""
    liste_1=string.ascii_lowercase
    liste_2=string.ascii_uppercase

    for i in mot:
        if i in liste_1:
            word+=liste_1[(liste_1.index(i) + k*operation)%26]
        elif i in liste_2:
             word+=liste_2[(liste_2.index(i) + k*operation)%26]
        else:
            word+=i
    return word


# tc: renvoie True si il n y a pas 3 consonne consecutif dans la chaine
#permet d eliminer les mot où y a 3 consonnes consecutifs (cas du francais)
def tc(mot):
    voyelle=['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u',
             'y', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ý', 'À', 'È', 'Ì', 'Ò', 'Ù',
             'Â', 'Ê', 'Î', 'Ô', 'Û', 'Ä', 'Ë', 'Ï',
             'Ö', 'Ü', 'Ÿ', 'Æ', 'Œ', 'á', 'é', 'í', 'ó', 'ú', 'ý', 'à',
             'è', 'ì', 'ò', 'ù', 'â', 'ê', 'î', 'ô', 'û',
             'ä', 'ë', 'ï', 'ö', 'ü', 'ÿ', 'æ', 'œ']
    l=len(mot)
    k=0
    while(k<l):
        c=0
        for i in mot[k:k+3]:
            if i not in voyelle:
                c+=1
        if c==3:
            return False
        k+=3
    return True

# prend un mot en parametre , verifie si le mot de gauche a droite et dans l autre sens a pas 3 consonnes alignés et renvoie un dico avec clé le mot decodé et valeur la clé actuelle
def verif_cesar(mot):
 dic={}
 for i in range(26):
     if tc(cesar(mot,-1,i))==True and tc(cesar(reversed(mot),-1,i))==True:
        #  print(cesar(mot,-1,i),i)
         dic[cesar(mot,-1,i)]=i
 return dic


#peut prendre chaine ou mot en caractere fais la meme chose que verif_cesar mais juste a des fins  d affichage

def end_cesar(chaine):

    if chaine.isspace()==False: # isspace si la chaine contient des espaces renvoie false
         for i in chaine.split(" "): #prend les mot un à un
            print(verif_cesar(i))
            print("\n")
    else:print(verif_cesar(chaine))

# version evoluée de end_cesar
# elle retourne un dictionnaire sur lequel on peut travailler
# on peut lui appliqué print() pour renvoyer un dictionnaire avec pour clé les clés de chiffrement et pour valeur  leurs messages decodés
#elle renvoie un seul dictionnaire , les valeurs sont sous forme concatenés

def z_cesar(chaine):

    if chaine.isspace()==False:
            dico={}
            for a in range(26):
                l=[]
                for i in chaine.split(" "):
                    for j,k in verif_cesar(i).items():
                        if a==k:
                          l.append(j)
                if l:
                   dico[a]=" ".join(l)
            return dico
    else:return verif_cesar(chaine)
