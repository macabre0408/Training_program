etudiants = {"etudiant_1" : 13, "etudiant_2" : 17, "etudiant_3" : 9 , "etudiant_4" : 15
,
"etudiant_5" : 8 , "etudiant_6" : 14 , "etudiant_7" : 16 , "etudiant_8" : 12 ,
"etudiant_9" : 13 , "etudiant_10" : 15 , "etudiant_11" : 14 , "etudiant_112" : 9 ,
"etudiant_13" : 10 , "etudiant_14" : 12 , "etudiant_15" : 13 , "etudiant_16" : 7
}
etudiantAdmis = {}
etudiantNonAdmis = {}
for cle in etudiants :
    if etudiants[cle]>= 10:
        etudiantAdmis[cle]= etudiants[cle]
    else:
        etudiantNonAdmis[cle]= etudiants[cle]
print(etudiantNonAdmis)
print(etudiantAdmis)