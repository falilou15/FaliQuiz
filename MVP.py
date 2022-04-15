#Minimum Viable Product pour le quiz

Q0 = {"énoncé" : "Quel est le vrai nom de Spider-Man ?" ,
      "réponses" : ["1 - Cristiano Ronaldo","2 - Tony Strak","3 - Rebeu Deter","4 - Peter Parker"] ,
      "bonne-réponse" : 4}


Q1 = {"énoncé" : "Quel arme utilise Thor pour se battre ?" ,
      "réponses" : ["1 - un marteau","2 - une fourchette","3 - un trident","4 - un pistolet"] ,
      "bonne-réponse" : 1}

Q2 = {"énoncé" : "Quel est le nom du village ou vit Naruto ?" ,
      "réponses" : ["1 - Grigny","2 - Konoha","3 - Sarcelles","4 - Kumo"] ,
      "bonne-réponse" : 2}

Q3 = {"énoncé" : "Quel est le titre du premier Star Wars ?" ,
      "réponses" : ["1 - La Menace fantôme","2 - L'Attaque des clones","3 - Le Retour du Jedi","4 - L'Empire contre-attaque"] ,
      "bonne-réponse" : 1}

Q4 = {"énoncé" : "Quel est premier membre de l'équipage de Luffy dans One Piece ?" ,
      "réponses" : ["1 - Usopp","2 - Nami","3 - Zoro","4 - Sanji"] ,
      "bonne-réponse" : 3}

# Proposition: Mettre les dictionnaires de questions sans un fichier JSOn ou txt
# Lire ce fichier pour alimenter la liste des questions
# Faire une interface graphique ?
# Mémoriser les pseudos/score dans un fichier externe voire un base de données (NSIT_12e)


questions = [Q0,Q1,Q2,Q3,Q4]

#question 0

score = 0

for q in range(len(questions)):
    SC = print ("Votre Score est de", score)
    print(questions[q]["énoncé"])
    for r in questions[q]["réponses"]:
        print(r)   
    réponse_joueur = int(input("Quel est votre réponse ? (répondez en écrivant 1 , 2 , 3 ou 4) "))
    if réponse_joueur == questions[q]["bonne-réponse"]:
        score += 1
        print()
        print("Bonne Réponse ! Votre Score est de", score)
        print()
    else:
        print()
        print("Mauvaise réponse")
        print()
   
print("Votre score final est de",score, "Merci d'avoir joué !")
