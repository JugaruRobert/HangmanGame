import unittest
from Practic.Repository.Repo import *
from Practic.Controller.Controller import *
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self._a = repo("sentences.txt")
        self._c=controller(repo())

    def testSwap(self):
        pass
        #t=["swap","0","1","-","0","2"]
        #m=self._a.getInitialSentence()
        #print(m)

if __name__ == '__main__':
    unittest.main()
