

def compteNoeudBigmac(Xappel, domaineSolution, jeuDD, noeudVisites):
    if Xappel >= jeuDD.shape[0] :
        return (True, len(noeudVisites))
    domainetuple = transformeDomaineTuple(jeuDD[Xappel, 0].shape[0])
    for tuple in domainetuple:
        noeudVisites += [(Xappel, tuple)]
        domaineSolution[Xappel] = tuple
        sousJeuDD = sousJeu(domaineSolution, Xappel, jeuDD)
        if compatibleAllBeforeOctopus(sousJeuDD):
            if compteNoeudBigmac(Xappel+1, domaineSolution, deepcopy(jeuDD), noeudVisites)[0]:
                return (True, len(noeudVisites))
    return (False, len(noeudVisites))
