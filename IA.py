#debut de notre projet
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
    return probabilites

def generer_mot(probabilites, longueur_mot):
    # Extraire les paires et les probabilités des dictionnaires
    paires = list(probabilites.keys())
    probs = list(probabilites.values())

    # Choisir la première paire aléatoirement selon les probabilités
    mot = random.choices(paires, probs)[0]
    # Continuer à ajouter des lettres jusqu'à atteindre la longueur souhaitée
    while len(mot) < longueur_mot:
        suivant = random.choices(paires, probs)[0][1]
        mot += suivant

    return mot[:longueur_mot]

chemin_fichier_txt = 'mots.txt'

mots = lire_fichier(chemin_fichier_txt)
tableau_occurrences = construire_tableau_occurrences(mots)
probabilites_paires = calculer_probabilites(tableau_occurrences)
mot_genere = generer_mot(probabilites_paires, nombre_aleatoire)  

print('Mot généré',mot_genere)