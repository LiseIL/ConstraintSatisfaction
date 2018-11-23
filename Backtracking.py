__Filename__ = 'Backtracking.py'

#from NDames import*
#from genererJeuDeDonnees import*

##################Algorithmes du Backtracking:

#dans JeuDeDonne, les variables sont indexées de X0 à Xn, ces dernières peuvent prendre des valeurs entières à partir de 0
#Xappel est initialisé à 0 généralement
#solution est une liste de n 0

def BT(solution,Xappel,JeuDeDonnee):
#renvoie True s'il existe une solution pour le CSP "JeuDeDonnee", et False sinon
#et affiche la solution sous forme de liste
    if Xappel>=JeuDeDonnee.shape[0]:
        print(solution)
        return True
#cas terminal
    for i in range (JeuDeDonnee[0,0].shape[0]):
      #dans le cas où le domaine de chaque variable est identique########################################################
        if compatibleAllBefore(Xappel,i,JeuDeDonnee,solution):
            solution[Xappel]=i
            if BT(solution,Xappel+1,JeuDeDonnee):
#appel recursif de la fonction BT
                return True
    return False

def compatibleAllBefore(Xi,i,JeuDeDonnee,solution):
#renvoie True si la valeur de Xi est compatible avec les contraintes du problème
    for Xk in range (0,Xi):
        if JeuDeDonnee[Xk,Xi][solution[Xk]][i]==0:
            return False
    return True

##################Quelques tests de la fonction BT() sur l'exemple des ndames:
#n1=1
#n2=2
#n3=3
#n4=4
#n5=5
#Xappel=0
#print(BT([0]*ndames(n1).shape[0],Xappel,ndames(n1)))
#print(BT([0]*ndames(n2).shape[0],Xappel,ndames(n2)))
#print()
#print(BT([0]*ndames(n3).shape[0],Xappel,ndames(n3)))
#print()
#print(BT([0]*ndames(n4).shape[0],Xappel,ndames(n4)))
#print()
#print(BT([0]*ndames(n5).shape[0],Xappel,ndames(n5)))
