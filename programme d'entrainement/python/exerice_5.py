def pairOrImpair(liste):
    dico={}
    for entier in liste:
        if entier % 2 == 0:
            dico[entier]="pair"
        else:
            dico[entier]="impair"
    return dico
liste = [1,2,3,4,5,6,7,8,9,10]
print(pairOrImpair(liste))