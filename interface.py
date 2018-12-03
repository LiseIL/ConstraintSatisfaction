
__Filename__ = 'interface.py'


from time import*
import matplotlib.pyplot as plt
from calculeNbNoeudsVisitesBT import*
from calculeNbNoeudVisitesBTAC import *
from Backtracking import*
from BTAC import*
from BigMAC import*
from NDames import*
from genererJeuDeDonnees import*

#jeu = genererJeuDeDonnees(5,5,6,0.24)
jeu = ndames(10)

#############Calcul pour le Backtracking (temps)
l1 = []
l2=[0.2,0.2]
tps=0
l1 =l1+[tps]
Xappel=0

t0 = perf_counter()
n1 = BT([0]*jeu.shape[0],Xappel,jeu)
t1 = perf_counter()
tps = t1 - t0
l1 = l1 + [tps]

#############Calcul pour BTAC (temps)
m1 = []
m2=[0.5,0.5]
ts=0
m1 =m1+[ts]
Xappel=0

t00 = perf_counter()
n2 = BTAC([0]*jeu.shape[0],Xappel,jeu)
t11 = perf_counter()
ts = t11 - t00
m1 = m1 + [ts]

#############Calcul pour Bigmac (temps)
s1 = []
s2=[0.8,0.8]
t=0
s1 =s1+[t]
Xappel=0

t000 = perf_counter()
n3 = bigmac(Xappel,[0]*jeu.shape[0],jeu)
t111 = perf_counter()
t = t111 - t000
s1 = s1 + [t]

#############Calcul pour le Backtracking (noeuds)
l1n = [0]
l2n=[0.2,0.2]
Xappel=0

n1n= compteNoeudBT([0]*jeu.shape[0],Xappel,jeu,[])[1]
l1n = l1n + [n1n]

#############Calcul pour BTAC (noeuds)
m1n = [0]
m2n=[0.5,0.5]
Xappel=0

n2n = compteNoeudBTAC([0]*jeu.shape[0], Xappel, jeu, [])[1]
m1n = m1n + [n2n]

#############Calcul pour Bigmac (noeuds)
s1n = [0]
s2n=[0.8,0.8]
Xappel=0

n3n = compteNoeudBT([0]*jeu.shape[0],Xappel,jeu,[])[1]
s1n = s1n + [n3n]

#############Propriétés de la fenêtre

plt.figure(figsize=(24,14), dpi=80)
plt.suptitle('Comparaison des algorithmes',fontsize=30)

#############Affichage du temps de calcul des méthodes

plt.subplot(121)

plt.annotate('Complexité en temps de calcul',fontsize=20, xy = (0.06,0.82),
             xycoords='figure fraction', xytext = (0.06,0.82),
             arrowprops = {'facecolor': 'white', 'edgecolor': 'white',
                           'width': 15, 'headwidth': 30},
             bbox=dict(boxstyle="round,pad=0.5", facecolor="white",
                       edgecolor="forestgreen", lw=1,))

plt.plot(l2,l1,linewidth=50,color="firebrick")
plt.plot(m2,m1,linewidth=50,color="darkorange")
plt.plot(s2,s1,linewidth=50,color="royalblue")
#Fake juste pour la légende, mais on trace pas vraiment
plt.plot(l2,l1,linewidth=10,label='Backtracking',color="firebrick")
plt.plot(m2,m1,linewidth=10,label='Backtracking+AC',color="darkorange")
plt.plot(s2,s1,linewidth=10,label='BigMAC',color="royalblue")
plt.legend(bbox_to_anchor=(1.01, 0), loc='upper right', borderaxespad=0.1)
plt.ylabel('temps de calcul (en secondes)',fontsize=16)
plt.xticks([], [])

#############Affichage du nombre de noeuds des méthodes

plt.subplot(122)

plt.annotate('Complexité en nombre de noeuds visités',fontsize=20, xy = (0.57,0.82),
             xycoords='figure fraction', xytext = (0.57,0.82),
             arrowprops = {'facecolor': 'white', 'edgecolor': 'white',
                           'width': 15, 'headwidth': 30},
             bbox=dict(boxstyle="round,pad=0.5", facecolor="white",
                       edgecolor="forestgreen", lw=1,))

plt.plot(l2n,l1n,linewidth=50,color="firebrick")
plt.plot(m2n,m1n,linewidth=50,color="darkorange")
plt.plot(s2n,s1n,linewidth=50,color="royalblue")
#Fake juste pour la légende, mais on trace pas vraiment
plt.plot(l2n,l1n,linewidth=10,label='Backtracking',color="firebrick")
plt.plot(m2n,m1n,linewidth=10,label='Backtracking+AC',color="darkorange")
plt.plot(s2n,s1n,linewidth=10,label='BigMAC',color="royalblue")
plt.legend(bbox_to_anchor=(1.01, 0), loc='upper right', borderaxespad=0.1)
plt.ylabel('nombre de noeuds',fontsize=16)
plt.xticks([], [])


plt.subplots_adjust(left=0.05,right=0.95, wspace=0.3,hspace=1,
                    bottom=0.1, top=0.8)

plt.savefig('Comparaison des algorithmes')

plt.show()
