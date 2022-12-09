file = open("./input-2.txt")

#constants
lost = 0
draw = 3
win = 6

rock = 1 #A X 
paper = 2 #B Y
scissors = 3 #C Z

score = 0
for line in file:   
    split = line.split(" ")
    opponent = split[0]
    me = split[1].split("\n")[0]     

    #rock
    if opponent == "A":
        #rock
        if me == "X":
            score += draw + rock
        #paper
        elif me == "Y":
            score += win + paper
        #scissors
        elif me == "Z":
            score += lost + scissors
    #paper
    elif opponent == "B":
        #rock
        if me == "X":
            score += lost + rock
        #paper
        elif me == "Y":
            score += draw + paper
        #scissors
        elif me == "Z":
            score += win + scissors
    #scissors
    elif opponent == "C":
        #rock
        if me == "X":
            score += win + rock
        #paper
        elif me == "Y":
            score += lost + paper
        #scissors
        elif me == "Z":
            score += draw + scissors

print(score)
