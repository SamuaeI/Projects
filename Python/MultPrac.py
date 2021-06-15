import random
import time
import math

ChosenMultiple = input("Chose a multiple: ")
VeryStartTime = time.time()
Correct, Incorrect = 0, 0

while True:
    if not ChosenMultiple.isnumeric():
        ChosenMultiple = str(random.randrange(1, 12))
    QuestionStartTime = time.time()
    
    SecondMultiple = random.randrange(1, 12)
    QuestionSolution = int(ChosenMultiple) * SecondMultiple
    Answer = input(str(ChosenMultiple) + " x " + str(SecondMultiple) + " = ")

    if Answer.lower() == "end":
        endTime = time.time()
        strCorrect = "You got "+  str(Correct) + " Correct"
        strIncorrect = "And you got "+  str(Incorrect) + " Incorrect"
        strScore = "Score: " + str(math.floor((Correct / (Correct + Incorrect)) * 100)) + "%"
        strSessionTime = "Session time: " + str(round((endTime - VeryStartTime), 1)) + " seconds"
        maxStrLen = max([len(strCorrect), len(strIncorrect), len(strScore), len(strSessionTime)])

        print("-"*maxStrLen)
        print(strCorrect + "\n" + strIncorrect + "\n" + strScore + "\n" + strSessionTime)
        print("-"*maxStrLen)
        break

    if Answer.isnumeric() and int(Answer) == QuestionSolution:
        stopTime = time.time()
        print("Correct, it took you, " + str(round((stopTime - QuestionStartTime), 1)) + " seconds")
        Correct += 1
    else:
        print("Incorrect")
        Incorrect += 1
