#debut de notre projet
import random
from collections import Counter

nombre_aleatoire = random.randint(1, 10) #nombre aleatoire

def lire_fichier(chemin_fichier):  # fonction permetant la lecture du fichier.txt et renvoi des mots
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        texte = fichier.read()
        mots = texte.split()
    return mots

def construire_tableau_occurrences(mots): # fonction qui calcul l'occurence 
    paires = Counter()
    for mot in mots:
        for i in range(len(mot) - 1):
            paire = mot[i:i+2]
            paires[paire] += 1
    return paires

def calculer_probabilites(paires): #fonction qui calcul la probabilité
    total_paires = sum(paires.values())
    probabilites = {}
    for paire in paires:
        probabilites[paire] = paires[paire] / total_paires
    return probabilite