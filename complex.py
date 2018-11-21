__Filename__ = 'complex.py'

from time import*
import matplotlib.pyplot as plt
from Backtracking import*
from octopus_PC import*
from genererJeuDeDonnees import*

jeu = genererJeuDeDonnees(4,4,6,0.24)

#############Calcul pour le Backtracking
l1 = []
l2=[]
tps=0
i=0
Xappel=0
while tps<10 and i<100:
    t0 = perf_counter()
    n1 = BT([0]*jeu.shape[0],Xappel,jeu)
    t1 = perf_counter()
    tps = t1 - t0
    l1 = l1 + [tps]
    l2=l2+[i]
    i = i + 1

#############Calcul pour Octopus
m1 = []
m2=[]
ts=0
p=0
while ts<10 and p<100:
    t00 = perf_counter()
    n2 = octopus(Xappel,[0]*jeu.shape[0],jeu)
    t11 = perf_counter()
    ts = t11 - t00
    m1 = m1 + [ts]
    m2=m2+[p]
    p = p + 1

#############Affichage du temps de calcul des méthodes

plt.figure()

plt.plot(l2,l1,label='Backtracking')
plt.plot(m2,m1,label='Octopus')
plt.legend()
plt.ylabel('temps de calcul')
plt.xlabel('n')
plt.savefig('temps de calcul Backtracking & Octopus')
plt.title('temps de calcul des algorithmes Backtracking et Octopus')

plt.show()
