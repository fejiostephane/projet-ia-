#debut de notre projet
import random
from collections import Counter

nombre_aleatoire = random.randint(1, 10) #nombre aleatoire

def lire_fichier(chemin_fichier):  # fonction permetant la lecture du fichier.txt et renvoi des mots
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        texte = fichier.read()
        mots = texte.split()
    return mots