# Created by isnel at 29/10/18

# Pour PC, vous pourrez simplifier la problématique
# en considérant que dans le cas de son application
# pour le projet, il n'y aura au plus que 2 valeurs par domaine.
# Ainsi, comme ce sera très spécifique, vous pourriez en
# tirer profit pour renforcer l'efficacité de l'algo implémenté
# contrairement au cas général où la taille des domaine
# est  a priori quelconque.

from genererJeuDeDonnees import calculNbCouplesAutorises, creerRelationContrainte, genererJeuDeDonnees
import time

def withoutSupportPC(i,j,k,a,b, jeuDD):
    """s'il existe un support c du couple (a,b) appartenant au domaine de
    la kième variable, retourne False ;
    sinon, retourne True"""

    R_ik = jeuDD[i,k]
    cardinald_k = (R_ik.shape)[1]
    assert(cardinald_k <= 2)
    c = 0

    if (not (jeuDD[i,k,a,c]==1 and jeuDD[j,k,b,c]==1)) and cardinald_k==2:
        c=+1
        return not (jeuDD[i, k, a, c]==1 and jeuDD[j, k, b, c]==1)

    else:
        return not (jeuDD[i,k,a,c]==1 and jeuDD[j,k,b,c]==1)
    #CAS OU D > 2
    #While (c < (cardinald_k - 1)) and not (jeuDD[i, k, a, c] == 1 and jeuDD[j, k, b, c] == 1)
     #      c += 1
    #return not (jeuDD[i, k, a, c] == 1 and jeuDD[j, k, b, c] == 1) """



def initializationPC(jeuDD):
    listPC = []
    nbVar = jeuDD.shape[0]
    listeDeZeros = [None] * nbVar
    statusPC = [[listeDeZeros for k in range(0,2)] for i in range(0,nbVar)]
    #!!!range de k -> à modifier

    for i in range(0,nbVar): #!!!Nos variables sont indexées à partir de 0
        for j in range(0, nbVar):
            if i!=j:
                domaine_i = (jeuDD[i,j].shape)[0]
                for a in range(0,domaine_i):
                    statusPC[i][a][j] = False

    for i in range(0,nbVar):
        for j in range(0, nbVar):
            for k in range(0, 2):
                if i<j and k!=i and k!=j:
                    relationContrainte = jeuDD[i,j]#.tolist()
                    domaine_a = relationContrainte.shape[0]
                    domaine_b = relationContrainte.shape[1]
                    for a in range(0,domaine_a):
                        for b in range(0,domaine_b):
                            #print("(i,j,k,a,b) =",(i,j,k,a,b))
                            #print(withoutSupportPC(i,j,k,a,b, jeuDD))
                            if withoutSupportPC(i,j,k,a,b, jeuDD):
                                jeuDD[a,b]=0
                                jeuDD[b,a]=0

                                if not statusPC[i][a][j]:
                                    listPC.append((i,a,j))
                                    statusPC[i][a][j]=True

                                if not statusPC[j][b][i]:
                                    listPC.append((j, b ,i))
                                    statusPC[j][b][i]=True
    return (listPC, statusPC) #!!!A vérifier

def propagatePC(i,k,a, jeuDD, listPC, statusPC): #!!!A vérifier
    assert(isinstance(i, int))
    assert (isinstance(k, int))
    #assert(isinstance(a, float)) #!!!A discuter

    nbVar = jeuDD.shape[0]
    relationContrainte = jeuDD[i, k]
    domaine_b = relationContrainte.shape[1]

    for j in range(0, nbVar):
        if j!=i and j!=k:
            for b in range(0,domaine_b):
                if jeuDD[i, j, a ,b]==1:
                    if withoutSupportPC(i, j, k, a, b, jeuDD):
                        jeuDD[a, b] = 0
                        jeuDD[b, a] = 0

                    if not statusPC[i][a][j]:
                        listPC.append((i, a, j))
                        statusPC[i][a][j] = True

                    if not statusPC[j][b][i]:
                        listPC.append((j, b, i))
                        statusPC[j][b][i] = True

def algorithmPC8(jeuDD):
    init = initializationPC(jeuDD)
    listPC = init[0]
    statusPC = init[1]

    while listPC != []:
        threeTuple = listPC[0]
        listPC.remove(threeTuple)

        i = threeTuple[0]
        a = threeTuple[1]
        k = threeTuple[2]

        statusPC[i][a][k] =False
        propagatePC(i,k,a, jeuDD, listPC, statusPC)



debut = time.time()
print(debut)
jeu = genererJeuDeDonnees(4,2,6,0.8)
#print("i=0 et k=2 \n",jeu[0,2])
#print("j=1 et k=2 \n",jeu[1,2])
#print(withoutSupportPC(0,1,2,0,0,jeu))
print(algorithmPC8(jeu))
fin = time.time()
print("Durée d'exécution: ",fin-debut)
