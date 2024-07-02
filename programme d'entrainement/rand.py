from random import randint
 
girl_power = [3, 8, 9, 12,14, 19, 23, 32, 36, 39 ]
j=0
groupe = []
while(j<15):
    n_1 = randint(1, 45)
    if(n_1 in girl_power):
        n_2=randint(1,45)
        n_3=randint(1,45)
        while(n_2 in girl_power or n_3 in girl_power):
            n_2 =randint(1,45)
            n_3=randint(1,45)
    n_2 = randint(1,45)
    if(n_2 in girl_power):
        n_3 =randint(1,45)
        while(n_3 in girl_power):
            n_3 =randint(1,45)
    n_3 = randint(1,45)
    groupe.append((n_1, n_2, n_3))
    j+=1      
print(groupe)