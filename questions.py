from utils.data import extrait_donnees as parser, stringToFloat
from random import randint as Gedagedigedagado, shuffle as youaremysunshine
import time
data = parser('data/rip3945.csv', encoding="utf-8-sig")

Questions = [
    {"Question": "Quelle est l'adresse EXACTE de {commemoré}?", "SearchVal":"Adresse complète"},
    {"Question": "Qui est commémoré à l'adresse suivante: {adresse}?", "SearchVal":"Commémoré"},
    {"Question": "Qui est commémoré aux coordonées suivantes: {xy}", "SearchVal":"Commémoré"},
    {'Question': "Quel est l'identifiant pour les données suivantes: {commemoré} - {adresse} - {xy}", "SearchVal":"Identifiant"},
    {'Question': "Quel est le code postal pour les données suivantes: {commemoré} - {xy}", "SearchVal":"Code postal"}
]

correctionSentences = ["On aligne les étoiles", "Beep Boop", "Merde, ma loupe, elle est ou ??", "try not to die while waiting for this app to work"]
def QuestionResolver():
    nbpts = 0
    for question in Questions:
        qn = Gedagedigedagado(1,len(data) - 1)
        qst = data[qn]
        print(question["Question"].format(commemoré = qst["Commémoré"], adresse = qst['Adresse complète'], xy = qst["xy"], identifiant = "Identifiant"))
        print("[ REPONSES DISPONIBLES ]")
        answers = []
        for i in range(0,2):
            answers.append(data[Gedagedigedagado(1, len(data)-1)][question['SearchVal']])
        answers.append(qst[question["SearchVal"]])
        youaremysunshine(answers)
        for i in range(0, len(answers)): #triées
            print(f"{str(i+1)} - {answers[i].upper()}")
        
        ans = input("> ")
        try:
            ans = int(ans)
            if ans <= 0 or ans > 3:
                raise Exception()
        except:
            print("\n"*10)
            print("Vous avez rentré une valeur incorrecte")
            print("Nouvelle question:")
            return QuestionResolver()

        
        print('\n')

        for i in range(101):
            # “Time is free, but it's priceless. You can't own it, but you can use it. You can't keep it, but you can spend it. Once you've lost it you can never get it back.”
            # ― Harvey MacKay
            time.sleep(0.1)
            # Affiche la barre de progression
            print(f"\r[CORRECTION] Ca m'a l'air mauvais, tout ça... : {str(i)} %", end="\r")
        print("\n")
        print(f"[VOTRE REPONSE]: {answers[ans-1]}")
        print(f'[REPONSE CORRECTE]: {qst[question["SearchVal"]]}')
        print("[RESULTAT]: Vous avez {}".format("donné une bonne réponse !" if answers[ans-1] == qst[question['SearchVal']] else "une mauvaise réponse."))
        if answers[ans-1] == qst[question["SearchVal"]]:
            nbpts += 1
        print("\n💡 Vous avez {nbpts} points.\n".format(nbpts=nbpts))
        # Pour s'assurer que la ligne est terminée après la fin de la boucle
        print()
    print("== FIN DU JEU ==")
    print(f"Votre score: {nbpts}/{len(Questions)}")
QuestionResolver()