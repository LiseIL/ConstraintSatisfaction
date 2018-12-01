###################Backtracking ~ version renvoyant le nombre de noeuds parcourus##########################

def nbNoeudVisitesBT(solution,Xappel,JeuDeDonnee, noeudVisites):
#input:
#------
#solution: une liste de n zéros, où n est le nombre de variables dans le JeuDeDonnee
#Xappel : la première variable appelée lors de de l'application du backtracking
#JeuDeDonnee : le jeu de données sous forme de np.array
#noeudVisites : une liste vide

#renvoie un tuple : (bool, int), le booleen indique True s'il existe une solution, et False sinon
#                                l'entier indique le nombre de noeux visités par l'algo de recherche

    if Xappel>=JeuDeDonnee.shape[0]:
        print(solution)
        return (True, len(noeudVisites))
        #cas terminal
    for i in range (JeuDeDonnee[0,0].shape[0]):
      #dans le cas où le domaine de chaque variable est identique########################################################
        noeudVisites += [(Xappel, i)]
        if compatibleAllBefore(Xappel,i,JeuDeDonnee,solution):
            solution[Xappel]=i
            if noeudVisitesBT(solution,Xappel+1,JeuDeDonnee, noeudVisites)[0]:
                #appel recursif de la fonction BT
                return (True, len(noeudVisites))
    return (False, len(noeudVisites))

def compatibleAllBefore(Xi,i,JeuDeDonnee,solution):
#renvoie True si la valeur de Xi est compatible avec toutes les variables précédentes : {X0, X1,...,X(i-1)}
    for Xk in range (0,Xi):
        if JeuDeDonnee[Xk,Xi][solution[Xk]][i]==0:
            return False
    return True
