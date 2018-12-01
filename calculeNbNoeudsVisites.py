###################Backtracking ~ version renvoyant le nombre de noeuds parcourus##########################
def compteNoeudBT(solution,Xappel,JeuDeDonnee, nbNoeudVisites):
#input:
#------
#solution: une liste de n zéros, où n est le nombre de variables dans le JeuDeDonnee
#Xappel : la première variable appelée lors de de l'application du backtracking
#JeuDeDonnee : le jeu de données sous forme de np.array
#noeudVisites : une liste vide

#renvoie un tuple : (bool, int), le booleen indique True s'il existe une solution, et False sinon
#  

    if Xappel>=JeuDeDonnee.shape[0]:
        print(solution)
        return (True, len(nbNoeudVisites))
        #cas terminal
    for i in range (JeuDeDonnee[0,0].shape[0]):
      #dans le cas où le domaine de chaque variable est identique########################################################
        nbNoeudVisites += [(Xappel, i)]
        if compatibleAllBefore(Xappel,i,JeuDeDonnee,solution):
            solution[Xappel]=i
            if compteNoeudBT(solution,Xappel+1,JeuDeDonnee, nbNoeudVisites)[0]:
                #appel recursif de la fonction BT
                return (True, len(nbNoeudVisites))
    return (False, len(nbNoeudVisites))


def compatibleAllBefore(Xi,i,JeuDeDonnee,solution):
#renvoie True si la valeur de Xi est compatible avec toutes les variables précédentes : {X0, X1,...,X(i-1)}
    for Xk in range (0,Xi):
        if JeuDeDonnee[Xk,Xi][solution[Xk]][i]==0:
            return False
    return True

##################BT+AC ~ version renvoyant le nombre de noeuds parcourus##########################
from BTAC import *

def compteNoeudBTAC(solution, Xappel, JeuDeDonnee, noeudVisites):
    #Input
    #-----
    #solution: une liste de n zéros, où n est le nombre de variables dans le JeuDeDonnee
    #Xappel : la première variable appelée lors de de l'application du backtracking
    #JeuDeDonnee : le jeu de données sous forme de np.array
    #noeudVisites : une liste vide
    
    #Output
    #------
    #renvoie un tuple : (bool, int), le booleen indique True s'il existe une solution, et False sinon
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
            if compteNoeudBTAC(solution, Xappel + 1, (JDD[0], valeurs2), noeudVisites)[0]:
                # appel recursif de la fonction BT
                return (True, len(noeudVisites))
    return (False, len(noeudVisites))
