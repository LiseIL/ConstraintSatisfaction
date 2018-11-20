__author__ = 'Coruzzi Nicolas'
__Filename__ = 'testgJDD.py'
__Creationdate__ = '17/11/18'

import unittest
from genererJeuDeDonnees import *

class testgJDD(unittest.TestCase):

    def test_gJDDidentite(self):

        nbVariables = 4
        cardinalD = 4
        nbContraintes = 6
        tauxSatisf = 0.24

        jeu = genererJeuDeDonnees(nbVariables, cardinalD, nbContraintes, tauxSatisf)
        value = np.identity(nbVariables)
        expected=True

        for i in range(nbVariables):
            self.assertTrue(np.array_equal(value, jeu[i, i])==expected)

    def test_gJDDtranspose(self):

        nbVariables = 4
        cardinalD = 4
        nbContraintes = 6
        tauxSatisf = 0.24

        expected = True

        jeu = genererJeuDeDonnees(nbVariables, cardinalD, nbContraintes, tauxSatisf)

        for i in range(nbVariables):
            for j in range(nbVariables):
                self.assertTrue(np.array_equal(jeu[i,j], np.transpose(jeu[j,i])) == expected)

