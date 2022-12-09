file = open("./input-1.txt")

i = 0
list = {}

for line in file:   
    if line == "\n":
        i += 1
    else:   
        try:
            list[i] += int(line)
        except:
            list[i] = int(line)


def getSmallestTop(top3):
    smallest = top3[0]
    smallestI = 0
    i = 0
    for top in top3:
        if top < smallest:
            smallest = top
            smallestI = i
        i += 1
    return smallestI

top3 = [7, 8, 1]
j = 0

for sum in list:
    sum = list[j]
    smallestTopIndex = getSmallestTop(top3)
    if sum > top3[smallestTopIndex]:
        top3[smallestTopIndex] = sum
    j += 1

sum = 0
for top in top3:
    sum += top

print(sum)
#print(str(biggerJ) + " " + str(bigger))