__Filename__ = 'BTAC.py'

from NDames import*
from copy import *
import numpy as np

##################Algorithmes du Backtracking################

# dans JeuDeDonne, les variables sont indexées de X0 à Xn, ces dernières peuvent prendre des valeurs entières à partir
#  de 0
# Xappel est initialisé à 0 généralement
# solution est une liste de n 0


def BT(solution, Xappel, JeuDeDonnee):
    # renvoie True et une liste contenant une solution si elle existe, et False sinon
    if isinstance(JeuDeDonnee, np.ndarray):
        liste = []
        liste2 = []
        for i in range(JeuDeDonnee.shape[2]):
            liste2 += [i]
        for i in range(JeuDeDonnee.shape[0]):
            liste += [copy(liste2)]
        JeuDeDonnee = tuple((JeuDeDonnee, liste))
    valeurs = []
    for i in range(Xappel):
        valeurs += [[solution[i]]]
    valeurs += JeuDeDonnee[1][Xappel:]
    print(valeurs)
    JDD = algo_AC8((JeuDeDonnee[0], valeurs))
    print(JDD)
    if isinstance(JDD[0], str):
        return False
    if Xappel >= len(valeurs):
        # cas terminal
        print(solution)
        return True
    for i in valeurs[Xappel]:
        valeurs2 = deepcopy(valeurs)
        if compatibleAllBefore(Xappel, i, JDD, solution):
            solution[Xappel] = i
            if BT(solution, Xappel + 1, (JDD[0], valeurs2)):
                # appel recursif de la fonction BT
                return True
    return False


def compatibleAllBefore(Xi, i, JeuDeDonnee, solution):
    # renvoie True si la valeur de Xi est compatible avec les contraintes du problème
    for Xk in range(0, Xi):
        if JeuDeDonnee[0][Xk, Xi][solution[Xk]][i] == 0:
            return False
    return True

####################### ALGORITHME AC #####################


def WithoutSupport_AC(i, j, b, jeuDD):
    # i et j sont des entiers, b est une valeur. Renvoie un booleen
    # Si b dans Dj possède un support dans Di, la fonction renvoie False
    # Sinon elle renvoie True
    domaine_i = jeuDD[1][i]
    if len(domaine_i) == 0:
        return 'EmptyDomain', i
    a = domaine_i[0]
    while (a < domaine_i[-1]) and ((jeuDD[0])[i, j, a, b] == 0):
        a = domaine_i[domaine_i.index(a) + 1]
    return not(jeuDD[0][i, j, a, b] == 1)


def initialisation_AC(jeuDD):
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


