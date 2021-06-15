import random
import math

ChosenMultiple = input("Chose a multiple: ")
Correct, Incorrect = 0, 0

while True:
    if not ChosenMultiple.isnumeric():
        ChosenMultiple = str(random.randrange(1, 12))

    SecondMultiple = random.randrange(1, 12)
    QuestionSolution = int(ChosenMultiple) * SecondMultiple
    Answer = input(str(ChosenMultiple) + " x " + str(SecondMultiple) + " = ")

    if Answer.lower() == "end":
        strCorrect = "You got "+  str(Correct) + " Correct"
        strIncorrect = "And you got "+  str(Incorrect) + " Incorrect"
        strScore = "Score: " + str(math.floor((Correct / (Correct + Incorrect)) * 100)) + "%"
        maxStrLen = max([len(strCorrect), len(strIncorrect), len(strScore)])

        print("-"*maxStrLen)
        print(strCorrect + "\n" + strIncorrect + "\n" + strScore)
        print("-"*maxStrLen)
        break
        
    if Answer.isnumeric() and int(Answer) == QuestionSolution:
        print("Correct")
        Correct += 1
    else:
        print("Incorrect")
        Incorrect += 1
