__Filename__ = 'testAC.py'

import unittest
from AC import *


class TestAC(unittest.TestCase):
    def testOneSolution(self):
        jeu1 = np.zeros((3, 3, 3, 3))
        for i in range(3):
            jeu1[i, i] = np.identity(3)
        jeu1[0, 1] = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        jeu1[1, 0] = np.transpose(copy(jeu1[0, 1]))
        jeu1[0, 2] = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
        jeu1[2, 0] = np.transpose(copy(jeu1[0, 2]))
        jeu1[1, 2] = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
        jeu1[2, 1] = np.transpose(copy(jeu1[1, 2]))
        jeu2 = algo_AC8(jeu1)
        expected = [[1], [1], [0]]
        self.assertTrue(isinstance(jeu2, tuple) and jeu2[1] == expected and np.array_equal(jeu1, jeu2[0]))

    def testEmptyDomainZero(self):
        jeu1 = np.zeros((3, 3, 4, 4))
        for i in range(3):
            jeu1[i, i] = np.identity(4)
        jeu2 = algo_AC8(jeu1)
        expected = 'EmptyDomain'
        self.assertTrue(jeu2[0] == expected)

    def testEmptyDomainTwo(self):
        jeu1 = np.zeros((3, 3, 3, 3))
        for i in range(3):
            jeu1[i, i] = np.identity(3)
        jeu1[0, 1] = np.array([[1, 0, 0], [0, 0, 0], [0, 1, 1]])
        jeu1[1, 0] = np.transpose(copy(jeu1[0, 1]))
        jeu1[0, 2] = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        jeu1[2, 0] = np.transpose(copy(jeu1[0, 2]))
        jeu1[1, 2] = np.array([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
        jeu1[2, 1] = np.transpose(copy(jeu1[1, 2]))
        jeu1 = algo_AC8(jeu1)
        expected = 'EmptyDomain'
        self.assertTrue(jeu1[0] == expected)

    def testIdentity(self):
        jeu1 = np.zeros((3, 3, 4, 4))
        for i in range(3):
            for j in range(3):
                jeu1[i, j] = np.identity(4)
        jeu2 = algo_AC8(jeu1)
        expected = [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
        self.assertTrue(np.array_equal(jeu1, jeu2[0]) and jeu2[1] == expected)


