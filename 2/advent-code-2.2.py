file = open("./input-2.txt")

#constants
lost = 0 #X
draw = 3 #Y
win = 6 #Z

rock = 1 #A 
paper = 2 #B
scissors = 3 #C

score = 0
for line in file:   
    split = line.split(" ")
    opponent = split[0]
    result = split[1].split("\n")[0]     

    #rock
    if opponent == "A":
        #lost
        if result == "X":
            score += lost + scissors
        #draw
        elif result == "Y":
            score += draw + rock
        #win
        elif result == "Z":
            score += win + paper
    #paper
    elif opponent == "B":
        #lost
        if result == "X":
            score += lost + rock
        #draw
        elif result == "Y":
            score += draw + paper
        #win
        elif result == "Z":
            score += win + scissors
    #scissors
    elif opponent == "C":
        #lost
        if result == "X":
            score += lost + paper
        #draw
        elif result == "Y":
            score += draw + scissors
        #win
        elif result == "Z":
            score += win + rock

print(score)
