__author__ = 'Coruzzi Nicolas'
__Filename__ = 'Backtracking'
__Creationdate__ = '13/10/18'

##################fonctions déjà établies, mais nécessaires au Backtracking:
import numpy as np

def variables(n):#créer une liste de variable d'une longueur n
   l=[]
   for i in range(n):
       l += ['x'+str(i)]
   return l

#Attention: dans toute la suite du programme, les variables sont indexées de 0 à n-1

def domaine(n):
   l = []
   for i in range(n):
       l+= [i]
   return l

def ensembleContraintes(X):
   tableau = np.zeros([len(X),len(X)])
   for i in range(len(X)):
       for j in range(len(X)):
           if (i != j):
               tableau[i,j]=1
   return tableau

def relationContrainteXiXj(Di, Dj,a ,b):
   tableau = np.zeros([len(Di), len(Dj)])
   for i in range(len(Di)):
       for j in range(len(Dj)):
           #print((sqrt((Di[i] - Dj[j])**2)),(sqrt((a - b)**2)))
           x = abs(Di[i] - Dj[j])
           y = abs(a - b)

           if Di[i] == Dj[j]:
               tableau[i,j] = 0
           elif x == y:
               tableau[i,j] = 0
           else:
               tableau[i,j] = 1
   return tableau



def ndames(n):
   #Soit X l'ensemble des variables [X1, X2 ... Xn]
   #Soit D l'ensemble des valeurs pouvant être pris par une variable (ici D identique pour toutes les variables)
   X = variables(n)
   D = domaine(n)
   C = ensembleContraintes(X)
   m =[]
   F = np.zeros([len(X),len(X)])#tableau qui contient à chaque Xi, Xj le tableau des contraintes
   for i in range(len(X)):
       l = []
       for j in range(len(X)):
           if C[i,j] == 1:
               Cij = relationContrainteXiXj(D,D,i,j)

               #F[i,j] = Cij
           else:
               Cij = np.zeros([len(D), len(D)])
           l += [Cij]
       m += [l]
   F = np.array(m)
   return F
   #fin construction des différents ensembles et tableaux
   #Là F est une matrice qui représente les tableaux de contrainte pour chaque Xi - Xj,
   #On regarde les 2 première colonnes et ont regarde quels couples de valeurs sont possible et ainsi de suite pour chaque couple de colonnes.

##################Algorithmes du Backtracking:

#dans JeuDeDonne, les variables sont indexées de X0 à Xn, ces dernières peuvent prendre des valeurs entières à partir de 0
#Xappel est initialisé à 0 généralement
#solution est une liste de n 0

def BT(solution,Xappel,JeuDeDonnee):
#renvoie True et une liste contenant une solution si elle existe, et False sinon
    if Xappel>=JeuDeDonnee.shape[0]:
        print(solution)
        return True
#cas terminal
    for i in range (JeuDeDonnee[0.0].shape[0]):
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
n1=1
n2=2
n3=3
n4=4
n5=5
Xappel=0
print(BT([0]*ndames(n1).shape[0],Xappel,ndames(n1)))
print()
print(BT([0]*ndames(n2).shape[0],Xappel,ndames(n2)))
print()
print(BT([0]*ndames(n3).shape[0],Xappel,ndames(n3)))
print()
print(BT([0]*ndames(n4).shape[0],Xappel,ndames(n4)))
print()
print(BT([0]*ndames(n5).shape[0],Xappel,ndames(n5)))
