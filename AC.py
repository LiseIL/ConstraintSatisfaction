__author__ = 'Coruzzi Nicolas'
__Filename__ = 'AC.py'
__Creationdate__ = '04/11/18'

#######################ALGORYTHME AC#####################
from genererJeuDeDonnees import*

def WithoutSupport_AC(i,j,b):
    #i et j sont des entiers, b est une valeur. Renvoie un booleen
    #Si b dans Dj possède un support dans Di, la fonction renvoie False
    #Sinon elle renvoie True
    nbVariables=4
    cardinalD=4
    nbContraintes=10
    tauxSatisf=0.24

    jeu=genererJeuDeDonnees(nbVariables, cardinalD, nbContraintes, tauxSatisf)

    Di=[]
    for z in range(cardinalD):
        Di+=[z]
        #Je ne savais pas comment récupérer les relations et les domaines dans le cas 
        #général donc j’ai fait ça; est-ce faux?


    a=Di[0]
    while a<Di[-1] and jeu[i,j][a][b]==0:
        a=Di[Di.index(a)+1]
    return not(jeu[i,j][a][b])

def initialisation_AC():

    nbVariables = 4
    cardinalD = 4
    nbContraintes = 10
    tauxSatisf = 0.24
    jeu = genererJeuDeDonnees(nbVariables, cardinalD, nbContraintes, tauxSatisf)
    n=cardinalD

    List_AC=[]
    Status_AC=[False]*n
    ###je ne comprend qui est n ici? Est-ce bien 'n=cardinalD'?###

    Dj = []
    for z in range(cardinalD):
        Dj += [z]
#je ne comprend pas ce que ça signifie lorsqu’on dit ‘pour j tel que Cij existe’

    for i in range(1,n+1):
        for j in range(1,n+1):
            for b in Dj:
                if WithoutSupport_AC(i,j,b):
                    Dj=Dj.remove(b)
                    if not(Status_AC[j]):
                        List_AC+=[j]
                        Status_AC[j]=True

def propager_AC(i,List_AC,Status_AC):
    #i entier
    nbVariables = 4
    cardinalD = 4
    nbContraintes = 10
    tauxSatisf = 0.24
    jeu = genererJeuDeDonnees(nbVariables, cardinalD, nbContraintes, tauxSatisf)
    n = cardinalD
    Dj = []
    for z in range(cardinalD):
        Dj += [z]

    for j in range(1,n+1):
        for b in Dj:
            if WithoutSupport_AC(i,j,b):
                Dj = Dj.remove(b)
                if not (Status_AC[j]):
                    List_AC += [j]
                    Status_AC[j] = True
    return Status_AC

def algo_AC8():
    initialisation_AC()
    while List_AC!=[]:
        for i in List_AC:
            List_AC=List_AC.remove(i)
            Status_AC[i]=False
            propager_AC(i,List_AC,Status_AC)


