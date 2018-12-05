from BTAC import *

##################BT+AC ~ version renvoyant le nombre de noeuds parcourus##########################

def compteNoeudBTAC(Xappel, solution, JeuDeDonnee, noeudVisites):
    # Input
    # -----
    # solution: une liste de n zéros, où n est le nombre de variables dans le JeuDeDonnee
    # Xappel : la première variable appelée lors de de l'application du backtracking
    # JeuDeDonnee : le jeu de données sous forme de np.array
    # noeudVisites : une liste vide

    # Output
    # ------
    # renvoie un tuple : (bool, int), le booleen indique True s'il existe une solution, et False sinon
    #                                l'entier indique le nombre de noeux visités par l'algo de recherche
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
    JDD = algo_AC8((JeuDeDonnee[0], valeurs))
    if isinstance(JDD[0], str):
        return (False, len(noeudVisites))
    if Xappel >= len(valeurs):
        # cas terminal
        print(solution)
        return (True, len(noeudVisites))
    for i in valeurs[Xappel]:
        noeudVisites += [(Xappel, i)]
        valeurs2 = deepcopy(valeurs)
        if compatibleAllBefore(Xappel, i, JDD, solution):
            solution[Xappel] = i
            if compteNoeudBTAC(Xappel + 1, solution, (JDD[0], valeurs2), noeudVisites)[0]:
                # appel recursif de la fonction BT
                return (True, len(noeudVisites))
    return (False, len(noeudVisites))



#from NDames import *
#n=4
#jeu = ndames(n)
#print(compteNoeudBTAC([0]*jeu.shape[0], 0, jeu, []))
