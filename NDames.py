# NDames created by isnel at 30/09/18

#from csp import *
import numpy as np
from random import *

def variables(n):#créer une liste de variable d'une longueur n
   l=[]
   for i in range(n):
       l += ['x'+str(i)]
   return l

def domaine(n):
   l = []
   for i in range(n):
       l+= [i]
   return l

def ensemble_contrainte(X):
   tableau = np.zeros([len(X),len(X)])
   for i in range(len(X)):
       for j in range(len(X)):
           if (i != j):
               tableau[i,j]=1
   return tableau

def XiXjContraintes(Di, Dj,a ,b):
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
   C = ensemble_contrainte(X)
   m =[]
   F = np.zeros([len(X),len(X)])#tableau qui contient à chaque Xi, Xj le tableau des contraintes
   for i in range(len(X)):
       l = []
       for j in range(len(X)):
           if C[i,j] == 1:
               Cij = XiXjContraintes(D,D,i,j)

               #F[i,j] = Cij
           else:
               Cij = np.zeros([len(D), len(D)])
           l += [Cij]
       m += [l]
   F = np.array(m)

   return F
   #fin construction des différents ensembles et tableaux
   #donc là F est une matrice qui représente les tableaux de contrainte pour chaque Xi - Xj,
   #en gros : on regarde les 2 première colonnes et ont regarde quels couples de valeurs sont possible et ainsi de suite
   #pour chaque couple de colonnes.

A = ndames(5)
#D = domaine(4)
#A = XiXjContraintes(D,D,0,2)
print(A[0,0])

M=[[0]*3]*3
N=[[1,2],[3,4]]

print(N[1][0])

N[1][0]=0
print(N)

N[1]=[3,5]
print(N)

print("\n")
P=[[[[0, 1], [2, 3]], [[4, 5], [6, 7]]], [[[0, 1], [2, 3]], [[12, 13], [14, 15]]]]
P[0][1] = [[0,-1],[-2,-3]]
print(P[0])
P[1][0] = [[0,-1],[-2,-3]]
print(P)

O=[[[[0, 0], [0, 0]], [[0, 0], [0, 0]]], [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]]
(O[0])[1]= [[0,-1],[-2,-3]]
print(O)
print("\n Test")
Test=[[[0,0] for _ in range(2)] for _ in range(2)]
print(Test)
Test1 = [[[[0]*2 for _ in range(2)] for _ in range(2)]for _ in range(2)]
print(Test1)
Test1[0][0] = [[1,2],[3,4]]
print(Test1)
