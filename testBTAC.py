from BTAC import *
import unittest


class TestBTAC(unittest.TestCase):
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
        solution = [0, 0, 0]
        jeu2 = BTAC(solution, 0, jeu1)
        self.assertTrue(jeu2)

    def testEmptyDomainZero(self):
        jeu1 = np.zeros((3, 3, 4, 4))
        for i in range(3):
            jeu1[i, i] = np.identity(4)
        solution = [0, 0, 0, 0]
        jeu2 = BTAC(solution, 0, jeu1)
        self.assertTrue(not jeu2)

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
        solution = [0, 0, 0]
        jeu1 = BTAC(solution, 0, jeu1)
        self.assertTrue(not jeu1)

    def testIdentity(self):
        jeu1 = np.zeros((3, 3, 4, 4))
        for i in range(3):
            for j in range(3):
                jeu1[i, j] = np.identity(4)
        solution = [0, 0, 0, 0]
        jeu2 = BTAC(solution, 0, jeu1)
        self.assertTrue(jeu2)

    def testNDames4(self):
        jeu = ndames(4)
        solution = [0, 0, 0, 0]
        jeu2 = BTAC(solution, 0, jeu)
        self.assertTrue(jeu2)

    def testNDames5(self):
        jeu = ndames(5)
        solution = [0]*5
        jeu2 = BTAC(solution, 0, jeu)
        self.assertTrue(jeu2)

if __name__ == '__main__':
    unittest.main()
