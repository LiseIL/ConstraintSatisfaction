# genererJeuDeDonnees created by isnel at 01/10/18

import numpy as np
from random import *
from copy import *

#Dans le jeu de données, les variables sont indexées de X0 à Xn
#Ces variables peuvent prendre des valeurs entières à partir de 0


def calculNbCouplesAutorises(cardinalD, tauxSatisf):
    #Renvoie le nombre de couple de valeur autorisé entre deux variables (noté N),
    #i.e. le nombre de 1 figurant dans la matrice représentant
    #la relation de contrainte entre ces deux variables

    #Par définition, tauxSatisf est égal à N divisé par
    #le nombre total de possibilité de satisfaire la contrainte.
    #Dans notre cas, tauxSatisf = N/(cardinalD**2)
    #car on considère que le domaine est le même pour toutes les variables

    N=tauxSatisf * (cardinalD**2)

    #Comme N doit être entier, on renvoie l'entier
    #le plus proche de N
    #!décision à confirmer!

    return int(round(N))


def creerRelationContrainte(cardinalD, tauxSatisf):
    #Créer une matrice repésentant la relation de contrainte
    #entre deux variables Xi et Xj
    #caractérisée par le taux de satisfiabilité ('tauxSatisf') entré.
    #Les variables Xi et Xj peuvent prendre les valeurs entières
    #appartenant à l'ensemble [0, cardinalD -1].

    relationContrainte = np.zeros((cardinalD,cardinalD), dtype=np.int)
    nbDe1Final = calculNbCouplesAutorises(cardinalD, tauxSatisf)
    nbDe1Cree = 0


    while nbDe1Cree < nbDe1Final: #!à vérifier!
        a = randint(0, cardinalD-1)
        b = randint(0, cardinalD-1)

        if relationContrainte[a,b]==1:
            continue
        else:
            #cas où relationContrainte[a,b]==0
            relationContrainte[a, b]=1
            nbDe1Cree+=1

    return relationContrainte.tolist()

def genererJeuDeDonnees(nbVariables, cardinalD, nbContraintes, tauxSatisf):
    #Génère une matrice contenant 'nbContraintes' relations de contraintes entre 'nbVariables' variables.
    #Les variables sont les valeurs entières appartenant à l'ensemble [0, cardinalD -1]
    #Chaque matrice relation de contrainte a le même taux de satisfiabilité égal à 'tauxSatisf'

    ListeDeUns = [1]*cardinalD
    matriceDeUns = [ListeDeUns for i in range(cardinalD)]
    jeuDeDonnees = [[matriceDeUns for i in range(nbVariables)] for i in range(nbVariables)]
    listeContraintesCrees = []
    nbContraintesCrees = 0

    for i in range(0, nbVariables):
        jeuDeDonnees[i][i] = np.identity(cardinalD)

    while nbContraintesCrees < nbContraintes :
        i = randint(0,nbVariables-1)
        j = randint(0, nbVariables-1)

        #verifier qu'une relation de contrainte entre Xi et Xj n'existe pas déjà
        if ((i,j) in listeContraintesCrees) or ((j,i) in listeContraintesCrees) or i==j:
            continue

        else:
            listeContraintesCrees += [(i,j)]
            listeContraintesCrees += [(j,i)]

            relationContrainte = creerRelationContrainte(cardinalD,tauxSatisf)
            jeuDeDonnees[i][j] = deepcopy(relationContrainte)

            #jeuDeDonnees[j][i] = transposée(jeuDeDonnees[i][j])
            npRelationContrainte = np.array(deepcopy(relationContrainte))
            npRelationContrainteTransposee = npRelationContrainte.transpose()
            jeuDeDonnees[j][i] = npRelationContrainteTransposee.tolist()

            nbContraintesCrees +=1

    return np.array(jeuDeDonnees)

#########################################################################
#Quelques tests
jeu = genererJeuDeDonnees(4,4,10,0.24)
print(len(jeu[1]))
print(jeu[0,0])
print(jeu[1,0])
print(jeu[2,0])
print(jeu[1,1])
print(jeu[1,2])
