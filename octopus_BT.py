from copy import *
import numpy as np
from pathConsistency import *
from csp import *


def octopus(Xappel, domaineSolution, jeuDD):
    if Xappel >= jeuDD.shape[0] :
        return True
    domainetuple = transformeDomaineTuple(jeuDD[Xappel, 0].shape[0])
    for tuple in domainetuple:
        domaineSolution[Xappel] = tuple
        sousJeuDD = copy(jeuDD[0:Xappel+1,0:Xappel+1, tuple[0]:tuple[1]+1, tuple[0]:tuple[1]+1])
        if compatibleAllBeforeOctopus(sousJeuDD, Xappel):
            if octopus(Xappel+1, domaineSolution, deepcopy(jeuDD)):
                return True
    return False

def transformeDomaineTuple(n):
    domaine = []
    for i in range(n):
        domaine += [i]
    if (len(domaine) == 0): #cas particulier domaine vide
        return []
    elif (len(domaine) == 1): #cas particulier domaine ne contenant qu'une seule valeur
        return domaine
    list = []
    for i in range(0, len(domaine), 2): #pour tout domaine de taille superieur à 2
        if (i == len(domaine)-1) and (i%2 == 0):
            list += [[domaine[i-1], domaine[i]]]
        else:
            list += [[domaine[i], domaine[i+1]]]
    return list

def compatibleAllBeforeOctopus(sousJeuDD, Xappel):

    if sousJeuDD.shape[0] == 1:
        return True
    else:
        jeu = deepcopy(sousJeuDD)
        print(Xappel, jeu)
        value = BT([0]*jeu.shape[0],0,jeu)
        print(value)
        if value == True:
            return True
        else:
            return False
