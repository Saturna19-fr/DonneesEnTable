from utils.data import extrait_donnees
from random import randint


data = extrait_donnees('data/drugs.csv', separator=',', is_in_quote=True)



Questions = {
    'drogue': [
        {"q": "Dans la tranche d'âge {age}, dans combien d'êtats le produit {illicitProduct} a t'il causé le plus de troubles en {year} ?", "type": "illicitProduct", "answers": "nbGuess", "proposedAnswers": 3}
    ],
    'test': [
        {"q": "Dans la tranche d'âge {age}, dans combien d'êtats le produit {illicitProduct} a t'il causé le plus de troubles en {year} ?", "type": "illicitProduct", "answers": "nbGuess", "proposedAnswers": 3}
    ]
}

def askQuestion(category, questionNumber):
    SelectedQuestions = Questions[category][questionNumber]
    # On choisit la ligne du tableau qu'on va interroger
    LS = randint(0, len(data)-1)
    dels = data[LS]
    print(dels)
    print("   "*200)
    # On choisit les valeurs qui seront interrogées.
    nbs = list(dels.keys())
    print(nbs)
    nbk = nbs[randint(4, len(nbs)-1)]
    print(nbk)

    d = [i[nbk] for i in data]
    print(d)
    if SelectedQuestions["answers"] == "nbGuess":
        print('nbGuess.')
        choices = []
        for i in range(2):
            choices.append(data[randint(0, len(data)-1)])
        print(SelectedQuestions["q"].format(year = dels["Year"], state = dels["State"], illicitProduct = illicitPDFromData(nbk), age = periodFromData(nbk)))
        k = input("Entrez votre réponse:\n> ")
        print(d)
        #if k == 

def periodFromData(item: str):
     return item.split(".")[len(item.split("."))-1]

def illicitPDFromData(item: str):
     return item.split(".")[1]

def main():
    # print("Questions\nChoisissez la catégorie:e\n1) Alcool\n2) Tabac\n3) Cocaïne\n4) Cannabis")
    print(*(f"{v+1}) {list(Questions.keys())[v].capitalize()}\n" for v in range(len(Questions))))
    a = input("> ")
    try:
        a = int(a)
    except:
        print('\033[36mVous devez entrer un nombre uniquement (1 - 4).\033[0;0m')
        main()
    else:
        pass

    
main()
# print(data)