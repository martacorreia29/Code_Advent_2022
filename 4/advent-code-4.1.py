#file = open("./input-4-test.txt")
file = open("./input-4.txt")

sum = 0
for line in file:   
    line = line.split("\n")[0]
    firstElf = line.split(",")[0]
    secondElf = line.split(",")[1]

    firstStart = int(firstElf.split("-")[0])
    firstEnd = int(firstElf.split("-")[1])
    #firstRange = [*range(firstStart, firstEnd)]

    secondStart = int(secondElf.split("-")[0])
    secondEnd = int(secondElf.split("-")[1])
    #secondRange = [*range(secondStart, secondEnd)]
    
    if (firstStart <= secondStart and firstEnd >= secondEnd) or (secondStart <= firstStart and secondEnd >= firstEnd):
        sum += 1    

print(sum)