import random
class repo:
    def __init__(self):
        """
        initializator
        """
        self._fileName="sentences.txt"
        self._sentence = self.loadFromFile()
        self._scramble=[]
        self._scramble=self.scramble()
        while self._scramble==self._sentence:
            self._scramble = self.scramble()
        self._score=int(self.Score())

    def Score(self):
        """
        Function used for computing the lenght of the initial sentence
        """
        l=0
        for i in self._sentence:
            l+=len(i)
        return l

    def getScore(self):
        """
        @getter - get score
        """
        return self._score

    def getInitialSentence(self):
        """
        @getter - get initial sentence
        """
        return self._sentence

    def getScrambledSentence(self):
        """
        @getter - get scrambled sentence
        """
        return self._scramble

    def findLenght(self):
        """
        Function used for finidng the lenght of the file.Numer of lines in the file
        Input:-
        Output:-the number of lines in the file
        """
        try:
            f=open(self._fileName,"r")
        except IOError:
            return
        fileLenght=0
        for line in f:
            fileLenght=fileLenght+1
        f.close()
        return fileLenght

    def loadFromFile(self):
        """
        Function used for reading a random line from the file.
        The number of lines is computed using the findLenght() method.
        A natural number is chosen randomly( between 1 and the lenght of the file) and that line is chosen for the program.
        It is written from the file and splitted.
        Input:-
        Output:A list that contains all the words form a specific line in the file.
        """
        try:
            f=open(self._fileName,"r")
        except IOError:
            return
        a=self.findLenght()
        r=random.randint(1,a)
        ok=1
        line=f.readline().strip()
        if ok!=r:
            while line!="":
                ok=ok+1
                line=f.readline().strip()
                if ok==r:
                    break
        t=line.split()
        f.close()
        return t

    def setScrambled(self,x):
        """
        @setter - set scrambled list
        """
        self._scramble=x

    def setInitial(self,x):
        """
        @setter - set initial list
        """
        self._sentence=x

    def decreaseScore(self):
        """
        Function used for decreasing the score by 1
        Input:-
        Output:the score after modifications
        """
        self._score=self._score - 1
        return self._score

    def scramble(self):
        """
        Function used to scramble the words in the current sentence.
        All the characters in the sentence despite the dirst character and the last one of each word are placed in a list.
        From there , a random character is taken and placed on other position, and removed from the list.
        The sentence is scrambled.
        Input:-
        Output:The scrabmbled sentence
        """
        char=[]
        a=self._sentence
        self._scramble=[0]*len(self._sentence)
        for i in range(0,len(a)):
            for j in range(1,len(a[i])-1):
                char.append(a[i][j])

        for i in range(0,len(a)):
            l=[self._sentence[i][0]]
            for j in range(1,len(a[i])-1):
                c=random.randint(0,len(char)-1)
                l=l+[char[c]]
                char.remove(char[c])
            l =l+ [a[i][-1]]
            msg=""
            for item in l:
                msg+=item
            self._scramble[i]=msg
        return self._scramble

