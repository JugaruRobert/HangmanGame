import unittest
from Practic.Controller.Controller import *
from Practic.Repository.Repo import *
from Practic.UI.UI import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self._repo = repo()
        self._controller = controller(self._repo)

    def testSwap(self):
        t=["abc","def"]
        self._repo.setInitial(t)
        s = ["aec", "dbf"]
        self._repo.setScrambled(s)
        c = ["swap", "0", "0", "-", "0", "0"]
        assert self._controller.swap(c) == 2
        c=["swap","0","1","-","1","1"]
        assert self._controller.swap(c) == 1

if __name__ == '__main__':
    unittest.main()
