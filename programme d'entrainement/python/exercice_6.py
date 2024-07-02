liste =[]
count = 1
while count <= 10:
    liste.append(int(input(f"Veuillez entrer l'entier numero {count} : ")))
    
    count+=1
dico={}
for entier in liste :
    diviseur = []
    j = 1
    while j<= entier:
        if entier%j==0:
            diviseur.append(j)
        j+=1
    dico[entier]=diviseur
print(dico)
        