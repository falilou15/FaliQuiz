#Minimum Viable Product pour le quiz

Q0 = {"énoncé" : "Quel est le vrai nom de Spider-Man ?" ,
      "réponses" : ["1 - Bruce Wayne","2 - Tony Strak","3 - Rebeu Deter","4 - Peter Parker"] ,
      "bonne-réponse" : 4}


Q1 = {"énoncé" : "Quel arme utilise Thor pour se battre ?" ,
      "réponses" : ["1 - un marteau","2 - une fourchette","3 - un trident","4 - un pistolet"] ,
      "bonne-réponse" : 1}

Q2 = {"énoncé" : "Quel est le nom du village ou vit Naruto ?" ,
      "réponses" : ["1 - Kiri","2 - Konoha","3 - Kumo","4 - Suna"] ,
      "bonne-réponse" : 2}

Q3 = {"énoncé" : "Quel est le titre du premier Star Wars ?" ,
      "réponses" : ["1 - La Menace fantôme","2 - L'Attaque des clones","3 - Le Retour du Jedi","4 - L'Empire contre-attaque"] ,
      "bonne-réponse" : 1}

Q4 = {"énoncé" : "Quel est premier membre de l'équipage de Luffy dans One Piece ?" ,
      "réponses" : ["1 - Usopp","2 - Nami","3 - Zoro","4 - Sanji"] ,
      "bonne-réponse" : 3}


questions = [Q0,Q1,Q2,Q3,Q4]

#question 0

score = 0
SC = print ("Votre Score est de", score)
print(questions[0]["énoncé"])
for r in questions[0]["réponses"]:
    print(r)   
réponse_joueur = int(input("Quel est votre réponse ? (répondez en écrivant 1 , 2 , 3 ou 4) "))
if réponse_joueur == questions[0]["bonne-réponse"]:
    score += 1
    print()
    print("Bonne Réponse ! Votre Score est de", score)
    print()
else:
    print()
    print("Mauvaise réponse")
    print()

#question 1

print(questions[1]["énoncé"])
for r in questions[1]["réponses"]:
    print(r)
réponse_joueur = int(input("Quel est votre réponse ? (répondez en écrivant 1 , 2 , 3 ou 4) "))
if réponse_joueur == questions[1]["bonne-réponse"]:
    score += 1
    print()
    print("Bonne Réponse ! Votre Score est de", score)
    print()
else:
    print()
    print("Mauvaise réponse")
    print()
  
#question 2
      
print(questions[2]["énoncé"])
for r in questions[2]["réponses"]:
    print(r)
réponse_joueur = int(input("Quel est votre réponse ? (répondez en écrivant 1 , 2 , 3 ou 4) "))
if réponse_joueur == questions[2]["bonne-réponse"]:
    score += 1
    print()
    print("Bonne Réponse ! Votre Score est de", score)
    print()
else:
    print()
    print("Mauvaise réponse")
    print()
    
#question 3
      
print(questions[3]["énoncé"])
for r in questions[3]["réponses"]:
    print(r)
réponse_joueur = int(input("Quel est votre réponse ? (répondez en écrivant 1 , 2 , 3 ou 4) "))
if réponse_joueur == questions[3]["bonne-réponse"]:
    score += 1
    print()
    print("Bonne Réponse ! Votre Score est de", score)
    print()
else:
    print()
    print("Mauvaise réponse")
    print()
    
#question 3
      
print(questions[4]["énoncé"])
for r in questions[4]["réponses"]:
    print(r)
réponse_joueur = int(input("Quel est votre réponse ? (répondez en écrivant 1 , 2 , 3 ou 4) "))
if réponse_joueur == questions[4]["bonne-réponse"]:
    score += 1
    print()
    print("Bonne Réponse ! Votre Score est de", score)
    print()
else:
    print()
    print("Mauvaise réponse")
    print()
    
print("Votre score final est de",score, "Merci d'avoir joué !")
