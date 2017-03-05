from Practic.Repository.Repo import *

class controller:
    def __init__(self,repository):
        """
        inoitializator
        :param repository:
        """
        self._repo=repository

    def getSentence(self):
        """
        Function used for calling the function in the repository for getting the initial sentence
        """
        return self._repo.getInitialSentence()

    def getScrambled(self):
        """
        Function used for calling the function in the repository for getting the scrambled sentence
        """
        return self._repo.getScrambledSentence()

    def getScore(self):
        """
        Function used for calling the function in the repository for getting the score
        """
        return self._repo.getScore()

    def swap(self,t):
        """
        Function used for swapping two characters from the scrambled sentence
        Score is decreased by 1 with each swap.
        Input: t- the initial sentence
        Output:
            0-if the player lost (score is 0)
            1-if the player won ( scrambled sentence == initial sentence)
            2-if neither happened( just swapping)
        """
        l=self._repo.getScrambledSentence()
        cuv1=int(t[1])
        l1=int(t[2])
        cuv2=int(t[4])
        l2=int(t[5])
        aux=l[cuv1][l1]
        msg=""
        for i in range(0,len(l[cuv1])):
            if i == l1:
                msg = msg + str(l[cuv2][l2])
            else:
                msg=msg+str(l[cuv1][i])
        l[cuv1]=msg

        msg=""
        for i in range(0, len(l[cuv2])):
            if i == l2:
                msg = msg + aux
            else:
                msg=msg+str(l[cuv2][i])
        l[cuv2] = msg
        self._repo.decreaseScore()
        if self._repo.getScore()==0 and (self._repo.getScrambledSentence() != self._repo.getInitialSentence()):
            return 0
        else:
            if self._repo.getScrambledSentence() == self._repo.getInitialSentence():
                return 1
            else:
                return 2



