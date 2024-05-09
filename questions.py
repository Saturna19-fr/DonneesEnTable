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

def CheckQuestion(question, ignoreList):
    for i in ignoreList:
        if question.find(i)>0:
            print(question.find(i))
            return False
    print(question.find(i))

    return True

def PoserQuestion(questionDict):
    print(questionDict)
    # 1- Définir une condition en fonction de la clé "type" de la question
    if (questionDict["type"] == "illicitProduct"):
        # On charge une ligne.
        ignored = ["State","Year" ,"Population.12-17" ,"Population.18-25" ,"Population.26+" ,"Alcohol" ,"Tobacco", "Marijuana"] # On estime que la Marijuana (Cannabis) est légale aux États Unis et qu'aucune distinction ne sera faite en fonction des Êtats.
        csv_dict = data[randint(0, len(data)-1)]

        # Maintenant, les valeurs
        ProduitIllicite = list(csv_dict.keys())[randint(0, len(csv_dict)-1)]
        while not CheckQuestion(ProduitIllicite, ignored):
            ProduitIllicite = list(csv_dict.keys())[randint(0, len(csv_dict)-1)]
        return True
def main():
    # print("Questions\nChoisissez la catégorie:e\n1) Alcool\n2) Tabac\n3) Cocaïne\n4) Cannabis")
    print(*(f"{v+1}) {list(Questions.keys())[v].capitalize()}\n" for v in range(len(Questions))), sep="\n")
    a = input("> ")
    try:
        a = int(a)
        PoserQuestion(Questions[list(Questions.keys())[a]][0])
    except Exception as e:
        print(e)
        print('\033[36mVous devez entrer un nombre uniquement (1 - 4).\033[0;0m')
        # main()
    else:
        pass

    
main()
# print(data)