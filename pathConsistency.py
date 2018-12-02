__Filename__ = 'pathConsistency.py'

# Pour PC, vous pourrez simplifier la problématique
# en considérant que dans le cas de son application
# pour le projet, il n'y aura au plus que 2 valeurs par domaine.
# Ainsi, comme ce sera très spécifique, vous pourriez en
# tirer profit pour renforcer l'efficacité de l'algo implémenté
# contrairement au cas général où la taille des domaine
# est  a priori quelconque.

from genererJeuDeDonnees import*
import time
import numpy as np


def withoutSupportPC(i, j, k, a, b, jeuDD):
    """s'il existe un support c du couple (a,b) appartenant au domaine de
    la kième variable, retourne False ;
    sinon, retourne True"""

    R_ik = jeuDD[i, k]
    cardinald_k = R_ik.shape[1]
    assert(cardinald_k <= 2)
    c = 0  # !!!Travailler avec domaine de Xk

    if (not(jeuDD[i, k, a, c] == 1 and jeuDD[j, k, b, c] == 1)) and cardinald_k == 2:
        c = 1

    return not(jeuDD[i, k, a, c] == 1 and jeuDD[j, k, b, c] == 1)


def initializationPC(jeuDD):
    listPC = []
    nbVar = jeuDD.shape[0]
    listeDeNone = [None] * nbVar
    # statusPC = [copy([copy(listeDeNone) for k in range(2)]) for i in range(nbVar)]
    statusPC = [[[False]*nbVar]*2]*nbVar
    # !!!range de k -> à modifier

    for i in range(nbVar):  # nos variables sont indexées à partir de 0
        for j in range(nbVar):
            if i != j:
                domaine_i = jeuDD[i,j].shape[0]
                for a in range(domaine_i):
                    statusPC[i][a][j] = False

    for i in range(nbVar):
        for j in range(i + 1, nbVar):
            for k in range(nbVar):
                if k != i and k != j:
                    relationContrainte = jeuDD[i, j]
                    domaine_a = relationContrainte.shape[0]
                    domaine_b = relationContrainte.shape[1]
                    for a in range(domaine_a):
                        for b in range(domaine_b):
                            if jeuDD[i, j, a, b] == 1:  # !!!A verifier

                                if withoutSupportPC(i,j,k,a,b, jeuDD):
                                    jeuDD[i, j, a, b] = 0
                                    jeuDD[j, i, b, a] = 0

                                    if not(statusPC[i][a][j]):  # !!!A vérifier
                                        listPC.append((i, a, j))
                                        statusPC[i][a][j] = True

                                    if not(statusPC[j][b][i]):
                                        listPC.append((j, b, i))
                                        statusPC[j][b][i] = True
    return (listPC, statusPC)


def propagatePC(i, k, a, jeuDD, listPC, statusPC):
    assert(isinstance(i, int))
    assert (isinstance(k, int))
    #assert(isinstance(a, float)) #!!!A discuter

    nbVar = jeuDD.shape[0]
    relationContrainte = jeuDD[i, k]
    domaine_b = relationContrainte.shape[1]

    for j in range(nbVar):
        if j != i and j != k:
            for b in range(domaine_b):
                if jeuDD[i, j, a, b] == 1:
                    if withoutSupportPC(i, j, k, a, b, jeuDD):
                        jeuDD[i, j, a, b] = 0
                        jeuDD[j, i, b, a] = 0

                        if not(statusPC[i][a][j]):
                            listPC.append((i, a, j))
                            statusPC[i][a][j] = True

                        if not(statusPC[j][b][i]):
                            listPC.append((j, b, i))
                            statusPC[j][b][i] = True


def algorithmPC8(jeuDD):
    init = initializationPC(jeuDD)
    listPC = init[0]
    statusPC = init[1]

    while len(listPC) > 0:
        threeTuple = listPC[0]
        listPC.remove(threeTuple)

        i = threeTuple[0]
        a = threeTuple[1]
        k = threeTuple[2]

        statusPC[i][a][k] = False
        propagatePC(i,k,a, jeuDD, listPC, statusPC)



###########################################################################################
#Exemples d'application

##Exemple 1
#jeu = genererJeuDeDonnees(3,2,2,0.5)
#print(jeu)
# print(algorithmPC8(jeu))

##Exemple 2
#R00 = [[0,0], [0,0]]
#R01 = [[1,0],[0,1]]
#R02 = [[0, 1], [1,0]]
#R10 = [[1,0],[0,1]]
#R12 = [[1,0], [1,1]]
#R20 = [[0, 1], [1, 0]]
#R21 = [[1,1],[0,1]]
#jeuExCours = np.array([[R00, R01, R02], [R10, R00, R12], [R20, R21, R00]])
#print("jeu original :\n",jeuExCours)

#debut = time.time()
#algorithmPC8(jeuExCours)
#fin = time.time()

#print("\njeu après filtration :\n",jeuExCours)


#print("Durée d'exécution: ",fin-debut)
