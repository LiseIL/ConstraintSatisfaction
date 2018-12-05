#Created by isnel at 05/12/18

from calculeNbNoeudsVisitesBT import *
from calculeNbNoeudVisitesBigMAC import *
from calculeNbNoeudVisitesBTAC import *
from time import *

#(solution,Xappel,JeuDeDonnee, noeudVisites) BT
#compteNoeudBigmac(Xappel, domaineSolution, jeuDD, noeudVisites)
#genererJeuDeDonnees(nbVariables, cardinalD, nbContraintes, tauxSatisf):

def takeTimeNodes(jeuDD, algorithme, Xappel=0):
    """renvoie un tuple donnant le temps de calcul et le nombre de noeuds développés
    lors de l'aplication de l'algorithme 'algorithme' au jeu de données 'jeuDD'

    'algorithme' peut être : compteNoeudBT, compteNouedBicmac, compteNoeudBTAC"""

    solution = [0]*jeuDD.shape[0]
    noeudVisites = []
    tInit = perf_counter()
    res = algorithme(Xappel, solution,jeuDD, noeudVisites)
    tFin = perf_counter()

    tTotal = tFin - tInit

    return (tTotal, res[1])

def ensembleJeuDomaineVariable(minCardD, maxCardD, stepCardD):
    """Renvoie un ensemble de jeux de données stockés dans une liste. Les jeux de données ont tous
    le même nombre de variable, de contraintes et le même taux de satisfiabilité. On fait varier la taille des domaines"""
    ensembleJDD = []
    for cardD in range(minCardD, maxCardD, stepCardD):
        ensembleJDD += [genererJeuDeDonnees(50,cardD, 612, 0.5)] #nb max contraintes avec 50 variables: 1225
    return ensembleJDD

def takeAllTimeNodes(ensembleJDD, algorithme):
    """Input
       -----
       ensembleJDD : une liste contenant des jeux de données
       algorithme : un des algorithmes suivant ~ compteNoeudBT, compteNouedBicmac, compteNoeudBTAC

       Output
       ------
       time : une liste des temps d'exécution telle que
              time[i] représente le temps d'exécution de 'agorithme' appliqué au jeu = ensembleJDD[i]
       nbNoeud : une liste des nombres de noeuds développés telle que
              nbNoeud[i] représente le nombre de noeud développé quand 'agorithme' est appliqué au jeu = ensembleJDD[i]"""
    time = []
    nbNoeud = []

    for jeu in ensembleJDD:
        results = takeTimeNodes(jeu, algorithme)
        time += [results[0]]
        nbNoeud += [results[1]]

    return time, nbNoeud


from NDames import *
jeuDD = ndames(4)
res0 = takeTimeNodes(jeuDD, compteNoeudBT)
print(res0)

res1 = takeTimeNodes(jeuDD, compteNoeudBigmac)
print(res1)

res2 = takeTimeNodes(jeuDD, compteNoeudBTAC)
print(res2)


M = [ndames(2), ndames(3), ndames(4), ndames(5)]
testAllTimeNodes = takeAllTimeNodes(M, compteNoeudBT)
print(testAllTimeNodes)

#ens = ensembleJeuDomaineVariable(20, 101, 20)
#print(ens[0])
