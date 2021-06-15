local ChosenMultiple

io.write("Choose a multiple: ")
ChosenMultiple = io.read()

while true do
    if not tonumber(ChosenMultiple) then
        ChosenMultiple = math.random(0, 12)
    end
    
    SecondMultiple = math.random(0, 12)
    QuestionSolution = ChosenMultiple * SecondMultiple
    io.write(ChosenMultiple.." x "..SecondMultiple.." = ")
    Answer = io.read()

    if tonumber(Answer) == QuestionSolution then
        print("Correct")
    else
        print("Incorrect")
    end
end
