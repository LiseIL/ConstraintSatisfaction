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

def ensembleJeuDomaineVariable(minCardD, maxCardD, stepCardD, nbVar=5, nbContraintes=15, tauxSatisf=0.5):
    """Renvoie un ensemble de jeux de données stockés dans une liste. Les jeux de données ont tous
    le même nombre de variable, de contraintes et le même taux de satisfiabilité. On fait varier la taille des domaines"""
    ensembleJDD = []
    for cardD in range(minCardD, maxCardD, stepCardD):
        print("card",cardD)
        ensembleJDD += [genererJeuDeDonnees(nbVar,cardD, nbContraintes, tauxSatisf)] #nb max contraintes avec 50 variables: 1225
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
minCardD=2
maxCardD=44
stepCardD=4
nbVar=15
nbContraintes = 100
tauxSatisf = 0.5

l=[]
for i in range(minCardD,maxCardD,stepCardD):
    l=l+[i]
print(l)

ens = ensembleJeuDomaineVariable(minCardD, maxCardD, stepCardD, nbVar, nbContraintes, tauxSatisf)

#Pour le Backtracking
print("1")
testAllTimeNodesBT = takeAllTimeNodes(ens, compteNoeudBT)

#Pour BTAC
print("2")
testAllTimeNodesBTAC = takeAllTimeNodes(ens, compteNoeudBTAC)

#Pour Bigmac
print("3")
testAllTimeNodesBigMAC = takeAllTimeNodes(ens, compteNoeudBigmac)

#############Proprietes de la fenetre

plt.figure(figsize=(24,14), dpi=80)
plt.suptitle('Comparaison des algorithmes',fontsize=30)

#############Affichage du temps de calcul des methodes

axes1=plt.subplot(211)

plt.annotate(' nombre de variables :'+ str(nbVar)+' \n nombre de contraintes : '+ str(nbContraintes)+' \n taux de satisfiabilite : '+ str(tauxSatisf),fontsize=20, xy = (0.8,0.86),
             xycoords='figure fraction', xytext = (0.8,0.82),
             arrowprops = {'facecolor': 'white', 'edgecolor': 'white',
                           'width': 15, 'headwidth': 30},
             bbox=dict(boxstyle="round,pad=0.1", facecolor="white",
                       edgecolor="grey", lw=1,))

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
plt.xlabel('taille du domaine',fontsize=16)
axes1.set_xlim(left=None, right=None, emit=True, auto=False, xmin=2, xmax=None)

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
plt.xlabel('taille du domaine',fontsize=16)
axes2.set_xlim(left=None, right=None, emit=True, auto=False, xmin=2, xmax=None)

plt.subplots_adjust(left=0.09,right=0.88, wspace=0.1,hspace=0.5,
                    bottom=0.1, top=0.8)

plt.savefig("Comparaison des algorithmes_X"+ str(nbVar) +"-C"+ str(nbContraintes) +"-S0,1_min-"+ str(minCardD)+"-max-"+ str(maxCardD)+"-step-"+str(stepCardD))

plt.show()
