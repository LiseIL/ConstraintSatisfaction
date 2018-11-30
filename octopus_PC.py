__Filename__ = 'octopus_PC.py'

from copy import *
import numpy as np
from pathConsistency import *
from Backtracking import *
from genererJeuDeDonnees import*

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
        algorithmPC8(jeu) #est-ce que ça ne rajoute pas une complexcité importante ?
        for variable in range(sousJeuDD.shape[0]-1):
            if variable != Xappel:
                if np.array_equal(jeu[Xappel, variable] , np.zeros([sousJeuDD[Xappel, variable].shape[0], sousJeuDD[Xappel, variable].shape[0]])) or np.array_equal(jeu[variable, Xappel], np.zeros([sousJeuDD[Xappel, variable].shape[0], sousJeuDD[Xappel, variable].shape[0]])):
                    return False

    return True


def sousJeu(domaineSolution, Xappel, jeuDD):
    new = np.zeros([Xappel+1, Xappel+1, 2,2])
    for i in range(Xappel+1):
        for j in range(Xappel+1):
            new[i,j] = np.identity(2)
            new[j,i] = np.identity(2)
    for variable in range(Xappel):
        new[variable, Xappel] = deepcopy(jeuDD[variable, Xappel, domaineSolution[variable][0]:domaineSolution[variable][1]+1, domaineSolution[Xappel][0]:domaineSolution[Xappel][1]+1])
        new[Xappel, variable] = deepcopy(jeuDD[Xappel, variable, domaineSolution[Xappel][0]:domaineSolution[Xappel][1]+1, domaineSolution[variable][0]:domaineSolution[variable][1]+1])

    return new
