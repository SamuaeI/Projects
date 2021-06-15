import random

ChosenMultiple = input("Choose a multiple: ")

while True:
    if not ChosenMultiple.isnumeric():
        ChosenMultiple = str(random.randrange(0, 12))

    SecondMultiple = random.randrange(0, 12)
    QuestionSolution = int(ChosenMultiple) * SecondMultiple
    Answer = input(str(ChosenMultiple) + " x " + str(SecondMultiple) + " = ")

    if int(Answer) == QuestionSolution:
        print("Correct")
    else:
        print("Incorrect")
