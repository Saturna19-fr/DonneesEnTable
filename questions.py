from utils.data import extrait_donnees
from random import randint


data = extrait_donnees('data/drugs.csv', separator=',', is_in_quote=True)

ProductsRelative = {
    "Alcool": ["Totals.Alcohol.Use Disorder Past Year.12-17", "Totals.Alcohol.Use Disorder Past Year.18-25", "Totals.Alcohol.Use Disorder Past Year.26+"]
}

Questions = {
    'drogue': [
        {"q": "En quelle année le taux de {illicitProduct} a été atteint dans l'êtat de/du (l') {state} ?", "type": "illicitProduct", "answers": "nbGuess", "proposedAnswers": 3}
    ]
}

def askQuestion(category, questionNumber):
    SelectedQuestion = Questions[category][questionNumber]

    if SelectedQuestion["answers"] == "nbGuess":
        print('nbGuess.')



    print(SelectedQuestion["q"].format(year = data[5]["Year"], state = data[5]["State"], bababo = "test", illicitProduct = "Alcool"))


askQuestion('drogue', 0)


# print(data)