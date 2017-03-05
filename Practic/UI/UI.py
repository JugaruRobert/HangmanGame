from Practic.Controller.Controller import *
from Practic.Repository.Repo import *
import sys
class UI:
    def __init__(self,controller):
        """
        initializator
        """
        self._controller=controller

    def printMenu(self,sentence,score):
        """
        Function used fro pretty printing on the console the current sentence and the current score
        Input:sentence-the current sentence,score-the current score
        Output:the message to be printed
        """
        msg=""
        for i in sentence:
            msg+=str(i)+" "
        msg+="[score is:"+str(score)+"]"
        return msg

    def verifySwap(self,t):
        """
        Function used for verifiying if the swap command is a valid command.All the possible cases are taken into consideration
        Input:t-the command
        Output:a list of errors
        """
        s = self._controller.getScrambled()
        err=""
        if len(t)!=6:
            err+="\nInvalid lenght!"
        else:
            if t[3]!="-":
                err += "\nInvalid command!"
            else:
                ok=0
                try:
                    a=int(t[1])
                    b = int(t[2])
                    c = int(t[4])
                    d = int(t[5])
                except:
                    ok=1
                    err += "\nSome elements are not natural numbers!"
                if ok==0:
                    a = int(t[1])
                    b = int(t[2])
                    c = int(t[4])
                    d = int(t[5])
                    if a < 0 or a > len(s):
                        err += "\nFirst word index is not valid!"
                    else:
                        if b < 0 or b > len(s[a]):
                            err += "\nFirst character index is not valid"
                    if c < 0 or c > len(s):
                        err += "\nSecond word index is not valid"
                    else:
                        if d < 0 or b > len(s[c]):
                            err += "\nSecond character index is not valid"
        return err

    def start(self):
        """
        Function used for reading the command for the console and calling the function that is in command.
        Return exception if the command is invalid.
        """
        a = self._controller.getScrambled()
        sc = self._controller.getScore()
        print(self.printMenu(a,sc))
        while True:
            try:
                command = input("\nEnter command: ")
                t=command.split()
                if len(command)==0:
                    print("\tInvalid command!")
                elif len(t)>6:
                    print("\tInvalid command!")
                elif t[0]=="swap":
                    err = self.verifySwap(t)
                    if len(err)==0:
                        finish=self._controller.swap(t)
                        if finish==0:
                            print("\nYou lose! :((((((")
                            sys.exit()
                        elif finish==1:
                            print("\nYou won! [score is: " + str(self._controller.getScore()) + "]")
                            sys.exit()
                        elif finish==2:
                            a = self._controller.getScrambled()
                            sc = self._controller.getScore()
                            print(self.printMenu(a, sc))
                    else:
                        print(err)
                else:
                    print("\tInvalid command!")

            except Exception as exc:
                print("Error encountered - " + str(exc))
