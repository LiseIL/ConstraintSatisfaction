__Filename__ = 'Interface.py'

from time import*
import matplotlib.pyplot as plt
from calculeNbNoeudsVisitesBT import*
from calculeNbNoeudVisitesBTAC import *
from calculeNbNoeudsVisitesBigMAC import*
from Backtracking import*
from BTAC import*
from BigMAC import*
from genererJeuDeDonnees import*

#############Algortihmes de calculs

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
        print("card",cardD)
        ensembleJDD += [genererJeuDeDonnees(20,cardD, 70, 0.5)] #nb max contraintes avec 50 variables: 1225
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

#############Initialisation
minCardD=6
maxCardD=20
stepCardD=2

l=[]
j=0
for i in range(minCardD,maxCardD,stepCardD):
    l=l+[j]
    j+=1
print(l)

ens = ensembleJeuDomaineVariable(minCardD, maxCardD, stepCardD)

#Pour le Backtracking
print("1")
testAllTimeNodesBT = takeAllTimeNodes(ens, compteNoeudBT)

#Pour BTAC
print("2")
testAllTimeNodesBTAC = takeAllTimeNodes(ens, compteNoeudBTAC)

#Pour Bigmac
print("2")
testAllTimeNodesBigMAC = takeAllTimeNodes(ens, compteNoeudBigmac)

#############Proprietes de la fenetre

plt.figure(figsize=(24,14), dpi=80)
plt.suptitle('Comparaison des algorithmes',fontsize=30)

#############Affichage du temps de calcul des methodes

axes1=plt.subplot(211)

plt.annotate('Etude du temps de calcul',fontsize=20, xy = (0.1,0.82),
             xycoords='figure fraction', xytext = (0.1,0.82),
             arrowprops = {'facecolor': 'white', 'edgecolor': 'white',
                           'width': 15, 'headwidth': 30},
             bbox=dict(boxstyle="round,pad=0.5", facecolor="white",
                       edgecolor="forestgreen", lw=1,))

plt.plot(l,testAllTimeNodesBT[0],"o--",label='Backtracking',color="firebrick")
plt.plot(l,testAllTimeNodesBTAC[0],"o--",label='Backtracking+AC',color="darkorange")
plt.plot(l,testAllTimeNodesBigMAC[0],"o--",label='BigMAC',color="royalblue")
plt.legend(bbox_to_anchor=(1.01, 0), loc='lower left', fontsize =14,borderaxespad=0.1)
plt.ylabel('temps de calcul (en secondes)',fontsize=16)
plt.yscale('log')
plt.xlabel('Jeu de donnees',fontsize=16)
axes1.xaxis.set_ticks(range(len(l)))

#############Affichage du nombre de noeuds des methodes

axes2=plt.subplot(212)

plt.annotate('Etude du nombre de noeuds visites',fontsize=20, xy = (0.1,0.4),
             xycoords='figure fraction', xytext = (0.1,0.4),
             arrowprops = {'facecolor': 'white', 'edgecolor': 'white',
                           'width': 15, 'headwidth': 30},
             bbox=dict(boxstyle="round,pad=0.5", facecolor="white",
                       edgecolor="forestgreen", lw=1,))

plt.plot(l,testAllTimeNodesBT[1],"o--",label='Backtracking',color="firebrick")
plt.plot(l,testAllTimeNodesBTAC[1],"o--",label='Backtracking+AC',color="darkorange")
plt.plot(l,testAllTimeNodesBigMAC[1],"o--",label='BigMAC',color="royalblue")
plt.legend(bbox_to_anchor=(1.01, 0), loc='lower left', fontsize =14,borderaxespad=0.1)
plt.ylabel('nombre de noeuds',fontsize=16)
plt.xlabel('Jeu de donnees',fontsize=16)
axes2.xaxis.set_ticks(range(len(l)))

plt.subplots_adjust(left=0.09,right=0.88, wspace=0.1,hspace=0.5,
                    bottom=0.1, top=0.8)

plt.savefig('Comparaison des algorithmes_min-'+ str(minCardD)+"-max-"+ str(maxCardD)+"-step-"+str(stepCardD))

plt.show()
