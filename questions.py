from utils.data import extrait_donnees

data = extrait_donnees('data/drugs.csv', separator=',', is_in_quote=True)

print(data)