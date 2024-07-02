dico = {'A': 0, 'B': 1, 'C':2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H':7, 'I':8, 'J':9, 'K': 10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
cle = int(input("veuillez entrer la clé de chiffrement : "))
print("le message à coder ou à decoder : (1: coder) (2: decoder) ")
choix = int(input("entrer votre choix : "))
list = []
code = []
if choix == 1:
    message_coder = input("entrer le message à coder: ")
    message_decoder=""
else:
    message_decoder = input("entrer le message à decoder: ")
if message_decoder == "":
    for char in message_coder.upper():
        list.append((dico[char]+ cle)%26)
    for i in list:
        for key in  dico.keys():
            if dico[key]==i:
                code.append(key)    
    print("Le message codé est : ")
    for i in code:
        print(i, end='')
else:
    for char in message_decoder.upper():
        list.append((dico[char]- cle)%26)
    for i in list:
        for key in  dico.keys():
            if dico[key]==i:
                code.append(key)    
    print("Le message décodé est : ")
    for i in code:
        print(i, end='')
    