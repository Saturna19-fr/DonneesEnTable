def extrait_donnees(chemin, separator=';', is_in_quote=False, encoding = ""):
    """ str -> list[dict]
    precondition: chemin mene a un fichier csv
    renvoie la liste de p-uplets nommes representant la table
    contenue dans le fichier csv"""
    if encoding != "":
        source = open(chemin, "r", encoding=encoding)
    else:
        source = open(chemin, "r")
        
    premiere_ligne = source.readline().strip()
    attributs = premiere_ligne.split(separator)
    chars = ' '
    if is_in_quote:
        chars += '\'"'
    attributs = [at.strip(chars) for at in attributs]
    nbr_attributs = len(attributs)
    table = []
    for ligne in source:
        element = {}
        prop = ligne.strip().split(separator)
        for i in range(nbr_attributs):
            element[attributs[i]] = prop[i].strip(chars)
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
    return data