__author__ = 'Coruzzi Nicolas'
__Filename__ = 'AC.py'
__Creationdate__ = '04/11/18'

#######################ALGORYTHME AC#####################
from genererJeuDeDonnees import*

def WithoutSupport_AC(i,j,b, jeuDD):
    #i et j sont des entiers, b est une valeur. Renvoie un booleen
    #Si b dans Dj possède un support dans Di, la fonction renvoie False
    #Sinon elle renvoie True
    
    #nbVariables=4
    #cardinalD=4
    #nbContraintes=10
    #tauxSatisf=0.24

    #jeu=genererJeuDeDonnees(nbVariables, cardinalD, nbContraintes, tauxSatisf)

    domaine_i=[]
    for z in range(cardinalD):
        domaine_i+=[z]
        #Je ne savais pas comment récupérer les relations et les domaines dans le cas 
        #général donc j’ai fait ça; est-ce faux?
        
    #Ce sera plus simple de cette façon:    
    #relation_ij = jeuDD[i,j]
    #domaine_i = (relation_ij.shape)[0]
    a=domaine_i[0]
    while a<domaine_i[-1] and jeuDD[i,j,a,b]==0:
        a=domaine_i[domaine_i.index(a)+1]
    return not(jeuDD[i,j,a,b])

def initialisation_AC(jeuDD):

    #nbVariables = 4
    #cardinalD = 4
    #nbContraintes = 10
    #tauxSatisf = 0.24
    #jeu = genererJeuDeDonnees(nbVariables, cardinalD, nbContraintes, tauxSatisf)
    #n=cardinalD
    
    n= jeuDD.shape[0]
    List_AC=[]
    Status_AC=[False]*n 
    
    ###je ne comprend qui est n ici? Est-ce bien 'n=cardinalD'?###n coorespond au nombre de variables présentent dans le jeu de données
    
    Dj = []
    for z in range(cardinalD): #voir proposition initialisation de Dj ligne 60
        Dj += [z]
#je ne comprend pas ce que ça signifie lorsqu’on dit ‘pour j tel que Cij existe’

   

    for i in range(1,n+1): #Il faut partir de 0 car nos variables sont indexées de 0 à n
        for j in range(1,n+1): #Il faut partir de 0 car nos variables sont indexées de 0 à n
            #if Cij is in C:
            
             #Ce sera plus simple de cette façon:    
            #relation_ij = jeuDD[i,j]
            #Dj = (relation_ij.shape)[1]
            for b in Dj: #[Indentation] après ajout du if ligne 58
                if WithoutSupport_AC(i,j,b, jeuDD):
                    Dj=Dj.remove(b)
                    if not(Status_AC[j]):
                        List_AC+=[j]
                        Status_AC[j]=True
                        
 #return(list_AC, Status_AC)

def propager_AC(i,List_AC,Status_AC,jeuDD):
    #i entier
    #nbVariables = 4
    #cardinalD = 4
    #nbContraintes = 10
    #tauxSatisf = 0.24
    #jeu = genererJeuDeDonnees(nbVariables, cardinalD, nbContraintes, tauxSatisf)
    #n = cardinalD
    Dj = []
    for z in range(cardinalD):
        Dj += [z]

    for j in range(1,n+1): #0 à n
        #if Cij is in C:
        for b in Dj: #Indentation après jout du if ligne 85
            if WithoutSupport_AC(i,j,b, jeuDD):
                Dj = Dj.remove(b)
                if not (Status_AC[j]):
                    List_AC += [j]
                    Status_AC[j] = True
    return Status_AC

def algo_AC8(jeuDD):
    init = initialisation_AC(jeuDD)
    list_AC = init[0]
    status_AC = init[1]          
    while List_AC!=[]:
        for i in List_AC:
            List_AC=List_AC.remove(i)
            Status_AC[i]=False
            propager_AC(i,List_AC,Status_AC, jeuDD)


