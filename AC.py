__author__ = 'Coruzzi Nicolas'
__Filename__ = 'AC.py'
__Creationdate__ = '04/11/18'

#######################ALGORITHME AC#####################
from copy import *
import numpy as np


def WithoutSupport_AC(i, j, b, jeuDD):
    #i et j sont des entiers, b est une valeur. Renvoie un booleen
    #Si b dans Dj possède un support dans Di, la fonction renvoie False
    #Sinon elle renvoie True
    domaine_i = jeuDD[1][i]
    if len(domaine_i) == 0:
        return 'EmptyDomain', i
    a = domaine_i[0]
    while (a < domaine_i[-1]) and ((jeuDD[0])[i, j, a, b] == 0):
        a = domaine_i[domaine_i.index(a) + 1]
    return not(jeuDD[0][i, j, a, b] == 1)


def initialisation_AC(jeuDD):
    if isinstance(jeuDD, np.ndarray):
        liste = []
        liste2 = []
        for i in range(jeuDD.shape[2]):
            liste2 += [i]
        for i in range(jeuDD.shape[0]):
            liste += [copy(liste2)]
        jeuDD = tuple((jeuDD, liste))
    n = jeuDD[0].shape[0]
    List_AC = []
    Status_AC = [False]*n   
    for i in range(n): 
        for j in range(n):
            relation_ij = jeuDD[0][i, j]
            if not(np.array_equal(jeuDD[0][i, j], np.ones(relation_ij.shape))):
                Dj = jeuDD[1][j]
                if len(Dj) == 0:
                    return 'EmptyDomain', j
                for b in Dj:
                    if WithoutSupport_AC(i, j, b, jeuDD):
                        if isinstance(WithoutSupport_AC(i, j, b, jeuDD), tuple):
                            if WithoutSupport_AC(i, j, b, jeuDD)[0] == 'EmptyDomain':
                                return 'EmptyDomain', i
                        Dj.remove(b)
                        if not(Status_AC[j]):
                            List_AC += [j]
                            Status_AC[j] = True
    return jeuDD, List_AC, Status_AC


def propager_AC(i, List_AC, Status_AC, jeuDD):
    n = jeuDD[0].shape[0]
    for j in range(n): 
            relation_ij = jeuDD[0][i, j]
            if not(np.array_equal(jeuDD[0][i, j], np.ones(relation_ij.shape))):
                Dj = jeuDD[1][j]
                if len(Dj) == 0:
                   return 'EmptyDomain', j
                for b in Dj: 
                    if WithoutSupport_AC(i, j, b, jeuDD):
                        Dj.remove(b)
                        if not(Status_AC[j]):
                            List_AC += [j]
                            Status_AC[j] = True


def algo_AC8(jeuDD):
    init = initialisation_AC(jeuDD)
    if isinstance(init[0], str):
        return init
    elif isinstance(init, tuple):
        jeuDD = init[0]
        List_AC = init[1]
        Status_AC = init[2]
        while len(List_AC) > 0:
            i = List_AC[0]
            List_AC.remove(i)
            Status_AC[i] = False
            a = propager_AC(i, List_AC, Status_AC, jeuDD)
            if isinstance(a, tuple) and a[0] == 'EmptyDomain':
                return a
    return jeuDD
