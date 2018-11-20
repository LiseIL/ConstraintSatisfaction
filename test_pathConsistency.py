import unittest
from pathConsistency import *
from genererJeuDeDonnees import *
from copy import *



class testPC(unittest.TestCase):
    def setUp(self):
        R00 = [[0, 0], [0, 0]]
        R01 = [[1, 0], [0, 1]]
        R02 = [[0, 1], [1, 0]]
        R10 = [[1, 0], [0, 1]]
        R12 = [[1, 0], [1, 1]]
        R20 = [[0, 1], [1, 0]]
        R21 = [[1, 1], [0, 1]]

    def test_jeuExcours(self):
        jeu = np.array([[R00, R01, R02], [R10, R00, R12], [R20, R21, R00]])
        algorithmPC8(jeu)
        S00 = [[0, 0], [0, 0]]
        S01 = [[0, 0], [0, 1]]
        S02 = [[0, 0], [1, 0]]
        S10 = [[0, 0], [0, 1]]
        S12 = [[0, 0], [1, 0]]
        S20 = [[0, 1], [0, 0]]
        S21 = [[0, 1], [0, 0]]
        expected = np.array([[S00, S01, S02], [S10, S00, S12], [S20, S21, S00]])
        self.assertTrue(np.array_equal(jeu, expected))

    def test_jeuNul(self):
        S00 = [[0, 0], [0, 0]]
        jeu = np.array([[S00, S00, S00], [S00, S00, S00], [S00, S00, S00]])
        algorithmPC8(jeu)
        expected = np.array([[S00, S00, S00], [S00, S00, S00], [S00, S00, S00]])
        self.assertTrue(np.array_equal(jeu, expected))

    def test_jeuComplet(self):
        S00 = [[0, 0], [0, 0]]
        S11 = [[1, 1], [1, 1]]
        jeu = np.array([[S00, S11, S11], [S11, S00, S11], [S11, S11, S00]])
        algorithmPC8(jeu)
        expected = np.array([[S00, S11, S11], [S11, S00, S11], [S11, S11, S00]])
        self.assertTrue(np.array_equal(jeu, expected))

    def test_jeuReduit(self):
        S00 = [[0, 0], [0, 0]]
        S01 = [[1, 1], [0, 0]]
        S02 = [[1, 0], [0, 0]]
        S10 = [[1, 0], [1, 0]]
        S12 = [[1, 0], [1, 0]]
        S20 = [[1, 0], [0, 0]]
        S21 = [[1, 1], [0, 0]]
        jeu = np.array([[S00, S01, S02], [S10, S00, S12], [S20, S21, S00]])
        algorithmPC8(jeu)
        expected = np.array([[S00, S01, S02], [S10, S00, S12], [S20, S21, S00]])
        self.assertTrue(np.array_equal(jeu, expected))

    def test_jeuZeroSolution(self):
        S00 = [[0, 0], [0, 0]]
        S01 = [[1, 0], [0, 1]]
        S02 = [[1, 0], [0, 1]]
        S10 = [[1, 0], [0, 1]]
        S12 = [[0, 1], [1, 0]]
        S20 = [[1, 0], [0, 1]]
        S21 = [[0, 1], [1, 0]]
        jeu = np.array([[S00, S01, S02], [S10, S00, S12], [S20, S21, S00]])
        algorithmPC8(jeu)
        expected = np.array([[S00, S00, S00], [S00, S00, S00], [S00, S00, S00]])
        self.assertTrue(np.array_equal(jeu, expected))
