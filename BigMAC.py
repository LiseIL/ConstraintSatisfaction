__Filename__ = 'octopus_PC.py'

from copy import *
import numpy as np
from pathConsistency import *
from Backtracking import *
from genererJeuDeDonnees import*
from AC import *

def bigmac(Xappel, domaineSolution, jeuDD):
    if Xappel >= jeuDD.shape[0] :
        return True
    domainetuple = transformeDomaineTuple(jeuDD[Xappel, 0].shape[0])
    for tuple in domainetuple:
        domaineSolution[Xappel] = tuple
        sousJeuDD = sousJeu(domaineSolution, Xappel, jeuDD)
        if compatibleAllBeforeOctopus(sousJeuDD, Xappel, domaineSolution):
            if bigmac(Xappel+1, domaineSolution, deepcopy(jeuDD)):
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

def compatibleAllBeforeOctopus(sousJeuDD, Xappel, domaineSolution):

    if sousJeuDD.shape[0] == 1:
        return True
    else:
        algorithmPC8(sousJeuDD)
        sousJeuDD = (algo_AC8(sousJeuDD))[0]
        if isinstance(sousJeuDD, str): # cas où un des domaines est vide
            return False
        for variable in range(sousJeuDD.shape[0]-1):
            if variable != Xappel:
                if np.array_equal(sousJeuDD[Xappel, variable] , np.zeros([sousJeuDD[Xappel, variable].shape[0], sousJeuDD[Xappel, variable].shape[0]])) or np.array_equal(sousJeuDD[variable, Xappel], np.zeros([sousJeuDD[Xappel, variable].shape[0], sousJeuDD[Xappel, variable].shape[0]])):
                    return False

    return True


def sousJeu(domaineSolution, Xappel, jeuDD):
    new = np.zeros([Xappel+1, Xappel+1, 2,2])
    for X in range(Xappel+1):
        for variable in range(Xappel+1):
            new[variable, X] = deepcopy(jeuDD[variable, X, domaineSolution[variable][0]:domaineSolution[variable][1]+1, domaineSolution[X][0]:domaineSolution[X][1]+1])
            new[X, variable] = deepcopy(jeuDD[X, variable, domaineSolution[X][0]:domaineSolution[X][1]+1, domaineSolution[variable][0]:domaineSolution[variable][1]+1])
    return new
