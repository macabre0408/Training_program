"""
liste = []
for i in range(20):
    print("Veuillez saisir le numero ",i + 1,": ")
    liste.append(int(input('')))
max = 0
for i in range(len(liste)):
    if max < liste[i]:
        max = liste[i]
print("le nombre le plus grand est : ",max,"\n")
print("il s'agit du numéro : ", liste.index(max) + 1)

def divide(a, b):
    assert b != 0
    return a / b
print(divide(10,1))
"""
bjr = "john-Doe-70000"
liste = bjr.split("-");
print("employee",tuple(liste))