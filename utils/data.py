def extrait_donnees(chemin, separator=';'):
    """ str -> list[dict]
    precondition: chemin mene a un fichier csv
    renvoie la liste de p-uplets nommes representant la table
    contenue dans le fichier csv"""
    source = open(chemin, "r")
    premiere_ligne = source.readline().strip()
    attributs = premiere_ligne.split(separator)
    nbr_attributs = len(attributs)
    table = []
    for ligne in source:
        element = {}
        prop = ligne.strip().split(separator)
        for i in range(nbr_attributs):
            element[attributs[i]] = prop[i]
        table.append(element)
    source.close()
    return table

