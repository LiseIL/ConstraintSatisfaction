__Filename__ = 'complex.py'

from time import*
import matplotlib.pyplot as plt
from Backtracking import*
from octopus_PC import*
from genererJeuDeDonnees import*

jeu = genererJeuDeDonnees(4,4,6,0.24)

#############Calcul pour le Backtracking
l1 = []
l2=[0,0]
tps=0
l1 =l1+[tps]
Xappel=0

t0 = perf_counter()
n1 = BT([0]*jeu.shape[0],Xappel,jeu)
t1 = perf_counter()
tps = t1 - t0
l1 = l1 + [tps]

#############Calcul pour Octopus
m1 = []
m2=[1,1]
ts=0
m1 =m1+[ts]

t00 = perf_counter()
n2 = octopus(Xappel,[0]*jeu.shape[0],jeu)
t11 = perf_counter()
ts = t11 - t00
m1 = m1 + [ts]

#############Affichage du temps de calcul des méthodes

plt.figure()

plt.plot(l2,l1,linewidth=10,label='Backtracking')
plt.plot(m2,m1,linewidth=10,label='Octopus')
plt.legend()
plt.ylabel('temps de calcul (en secondes)')
plt.xlabel('espace arbitraire')
plt.savefig('temps de calcul Backtracking & Octopus')
plt.title('temps de calcul des algorithmes Backtracking et Octopus')

plt.show()
