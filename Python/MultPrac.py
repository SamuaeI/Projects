import random
import time
import math

ChosenMultiple = input("Chose a multiple: ")
VeryStartTime = time.time()
Correct, Incorrect, LastMultiple, QuestionNum = 0, 0, 0, 0

while True:
    if not ChosenMultiple.isnumeric():
        ChosenMultiple = str(random.randrange(1, 12))
    QuestionStartTime = time.time()
    
    SecondMultiple = random.randrange(1, 12)
    if SecondMultiple != 0 and LastMultiple == SecondMultiple:
        SecondMultiple = random.randrange(1, 12)
        
    LastMultiple = SecondMultiple
    QuestionSolution = int(ChosenMultiple) * SecondMultiple
    QuestionNum += 1
    Answer = input("Q"+str(QuestionNum) +". " + str(ChosenMultiple) + " x " + str(SecondMultiple) + " = ")

    if Answer.lower() == "done":
        endTime = time.time()
        strCorrect = "You got "+  str(Correct) + " Correct"
        strIncorrect = "And you got "+  str(Incorrect) + " Incorrect"

        if Correct != 0 and Incorrect != 0:
            strScore = "Score: " + str(math.floor((Correct / (Correct + Incorrect)) * 100)) + "%"
        else:
            strScore = "Score: 0%"

        strSessionTime = "Session time: " + str(round((endTime - VeryStartTime), 1)) + " seconds"
        maxStrLen = max([len(strCorrect), len(strIncorrect), len(strScore), len(strSessionTime)])

        print("-"*maxStrLen)
        print(strCorrect + "\n" + strIncorrect + "\n" + strScore + "\n" + strSessionTime)
        print("-"*maxStrLen)

        ChosenMultiple = input("Chose a multiple: ")
        VeryStartTime = time.time()
        Correct, Incorrect, LastMultiple, QuestionNum = 0, 0, 0, 0
        continue
    elif Answer.lower() == "stop":
        break

    if Answer.isnumeric() and int(Answer) == QuestionSolution:
        stopTime = time.time()
        print("Correct. time: " + str(round((stopTime - QuestionStartTime), 1)) + " seconds")
        Correct += 1
    else:
        print("Incorrect")
        Incorrect += 1
