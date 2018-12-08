__Filename__ = 'Interface.py'

from time import*
import matplotlib.pyplot as plt
from calculeNbNoeudsVisitesBT import*
from calculeNbNoeudsVisitesBTAC import *
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
nbContraintesmax = 100
nbContraintesmin = 50
tauxSatisf = 0.5

l=[]
for i in range(minCardD,maxCardD,stepCardD):
    l=l+[i]
print(l)

ensmax = ensembleJeuDomaineVariable(minCardD, maxCardD, stepCardD, nbVar, nbContraintesmax, tauxSatisf)
ensmin = ensembleJeuDomaineVariable(minCardD, maxCardD, stepCardD, nbVar, nbContraintesmin, tauxSatisf)

#Pour le Backtracking
print("1")
testAllTimeNodesBTmax = takeAllTimeNodes(ensmax, compteNoeudBT)
testAllTimeNodesBTmin = takeAllTimeNodes(ensmin, compteNoeudBT)
#Pour BTAC
print("2")
testAllTimeNodesBTACmax = takeAllTimeNodes(ensmax, compteNoeudBTAC)
testAllTimeNodesBTACmin =  takeAllTimeNodes(ensmin, compteNoeudBTAC)
#Pour Bigmac
print("3")
testAllTimeNodesBigMACmax = takeAllTimeNodes(ensmax, compteNoeudBigmac)
testAllTimeNodesBigMACmin = takeAllTimeNodes(ensmin, compteNoeudBigmac)

#############Proprietes de la fenetre1

plt.figure(figsize=(24,14), dpi=80)
plt.suptitle('Comparaison des temps de calcul des algorithmes',fontsize=45)

#############Affichage du temps de calcul des methodes max

axes1=plt.subplot(211)

plt.annotate(' nombre de variables :'+ str(nbVar)+
             ' \n nombre de contraintes : '+ str(nbContraintesmax)+
             ' \n taux de satisfiabilite : '+ str(tauxSatisf),
             fontsize=22, xy = (0.1,0.82),
             xycoords='figure fraction', xytext = (0.1,0.82),
             arrowprops = {'facecolor': 'white', 'edgecolor': 'white',
                           'width': 15, 'headwidth': 30},
             bbox=dict(boxstyle="round,pad=0.5", facecolor="white",
                       edgecolor="forestgreen", lw=1,))

plt.plot(l,testAllTimeNodesBTmax[0],"o--",label='Backtracking',
         color="firebrick")
plt.plot(l,testAllTimeNodesBTACmax[0],"o--",
         label='Backtracking+AC',color="darkorange")
plt.plot(l,testAllTimeNodesBigMACmax[0],"o--",label='BigMAC',
         color="royalblue")
plt.ylabel('temps de calcul (en secondes)',fontsize=20)
plt.yscale('log')
plt.xlabel('taille du domaine',fontsize=20)

plt.xticks(np.arange(minCardD, maxCardD, step=stepCardD))

#############Affichage du temps de calcul des methodes min

axes2=plt.subplot(212)

plt.annotate(' nombre de variables :'+ str(nbVar)+
             ' \n nombre de contraintes : '+ str(nbContraintesmin)+
             ' \n taux de satisfiabilite : '+ str(tauxSatisf),
             fontsize=22, xy = (0.1,0.4),
             xycoords='figure fraction', xytext = (0.1,0.4),
             arrowprops = {'facecolor': 'white', 'edgecolor': 'white',
                           'width': 15, 'headwidth': 30},
             bbox=dict(boxstyle="round,pad=0.5", facecolor="white",
                       edgecolor="forestgreen", lw=1,))

plt.plot(l,testAllTimeNodesBTmin[0],"o--",label='Backtracking',
         color="firebrick")
plt.plot(l,testAllTimeNodesBTACmin[0],"o--",
         label='Backtracking+AC',color="darkorange")
plt.plot(l,testAllTimeNodesBigMACmin[0],"o--",label='BigMAC',
         color="royalblue")
plt.legend(bbox_to_anchor=(0.8, 1.07), loc='lower left',
           fontsize =20,borderaxespad=0.1)
plt.ylabel('temps de calcul (en secondes)',fontsize=20)
plt.yscale('log')
plt.xlabel('taille du domaine',fontsize=20)

plt.xticks(np.arange(minCardD, maxCardD, step=stepCardD))

plt.subplots_adjust(left=0.09,right=0.88, wspace=0.1,hspace=0.5,
                    bottom=0.1, top=0.8)
#############Proprietes de la fenetre2

plt.figure(figsize=(24,14), dpi=80)
plt.suptitle('Comparaison du nombre de noeuds visités par nos algorithmes',fontsize=45)

#############Affichage du nombre de noeuds des methodes max

axes3=plt.subplot(211)

plt.annotate(' nombre de variables :'+ str(nbVar)+
             ' \n nombre de contraintes : '+ str(nbContraintesmax)+
             ' \n taux de satisfiabilite : '+ str(tauxSatisf),
             fontsize=22, xy = (0.1,0.82),
             xycoords='figure fraction', xytext = (0.1,0.82),
             arrowprops = {'facecolor': 'white', 'edgecolor': 'white',
                           'width': 15, 'headwidth': 30},
             bbox=dict(boxstyle="round,pad=0.5", facecolor="white",
                       edgecolor="forestgreen", lw=1,))

plt.plot(l,testAllTimeNodesBTmax[1],"o--",label='Backtracking',
         color="firebrick")
plt.plot(l,testAllTimeNodesBTACmax[1],"o--",label='Backtracking+AC',
         color="darkorange")
plt.plot(l,testAllTimeNodesBigMACmax[1],"o--",label='BigMAC',
         color="royalblue")
plt.ylabel('nombre de noeuds',fontsize=20)
plt.xlabel('taille du domaine',fontsize=20)

plt.xticks(np.arange(minCardD, maxCardD, step=stepCardD))
plt.subplots_adjust(left=0.09,right=0.88, wspace=0.1,hspace=0.5,
                    bottom=0.1, top=0.8)

plt.savefig("Comparaison des algorithmes_X"+ str(nbVar) +
            "-C"+ str(nbContraintesmax) +"-S0,1_min-"+ str(minCardD)+
            "-max-"+ str(maxCardD)+"-step-"+str(stepCardD))


#############Affichage du nombre de noeuds des methodes min

axes4=plt.subplot(212)

plt.annotate(' nombre de variables :'+ str(nbVar)+
             ' \n nombre de contraintes : '+ str(nbContraintesmin)+
             ' \n taux de satisfiabilite : '+ str(tauxSatisf),
             fontsize=22, xy = (0.1,0.4),
             xycoords='figure fraction', xytext = (0.1,0.4),
             arrowprops = {'facecolor': 'white', 'edgecolor': 'white',
                           'width': 15, 'headwidth': 30},
             bbox=dict(boxstyle="round,pad=0.5", facecolor="white",
                       edgecolor="forestgreen", lw=1,))

plt.plot(l,testAllTimeNodesBTmin[1],"o--",label='Backtracking',
         color="firebrick")
plt.plot(l,testAllTimeNodesBTACmin[1],"o--",label='Backtracking+AC',
         color="darkorange")
plt.plot(l,testAllTimeNodesBigMACmin[1],"o--",label='BigMAC',
         color="royalblue")
plt.legend(bbox_to_anchor=(0.8, 1.07), loc='lower left',
           fontsize =20,borderaxespad=0.1)
plt.ylabel('nombre de noeuds',fontsize=20)
plt.xlabel('taille du domaine',fontsize=20)

plt.xticks(np.arange(minCardD, maxCardD, step=stepCardD))

plt.subplots_adjust(left=0.09,right=0.88, wspace=0.1,hspace=0.5,
                    bottom=0.1, top=0.8)

########################################################################

plt.savefig("Comparaison des algorithmes_X"+ str(nbVar) +
            "-Cmax"+ str(nbContraintesmax)+
            "-Cmin"+ str(nbContraintesmin) +"-S0,1_min-"+ str(minCardD)+
            "-max-"+ str(maxCardD)+"-step-"+str(stepCardD))


plt.show()
