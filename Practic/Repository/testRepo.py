import unittest
from Practic.Repository.Repo import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self._a=repo()

    def testScore(self):
        s=self._a.getInitialSentence()
        assert self._a.Score() == 9
        assert self._a.getScore() == 9

    def testFindLenght(self):
        assert self._a.findLenght()==1
        assert self._a.findLenght() != 0

    def testLoadFromFile(self):
        t=["abcde","ghij"]
        assert self._a.loadFromFile() == t

    def decreaseScore(self):
        a=self._a.getScore()
        self._a.decreaseScore()
        assert self._a.getScore()!=a

    def testScramble(self):
        m=self._a.loadFromFile()
        n = self._a.scramble()
        assert (m==n) == False

if __name__ == '__main__':
    unittest.main()
