def extrait_donnees(chemin, separator=';', is_in_quote=False):
    """ str -> list[dict]
    precondition: chemin mene a un fichier csv
    renvoie la liste de p-uplets nommes representant la table
    contenue dans le fichier csv"""
    source = open(chemin, "r")
    premiere_ligne = source.readline().strip()
    attributs = premiere_ligne.split(separator)
    if is_in_quote:
        attributs = [at.strip("'\"") for at in attributs]
    nbr_attributs = len(attributs)
    table = []
    for ligne in source:
        element = {}
        prop = ligne.strip().split(separator)
        for i in range(nbr_attributs):
            if is_in_quote:
                element[attributs[i]] = prop[i].strip("'\"")
            else:
                element[attributs[i]] = prop[i]
        table.append(element)
    source.close()
    return table


def stringToFloat(data):
    for element in data:
        for key in element:
            try:
                element[key] = float(element[key])
            except ValueError:
                pass
