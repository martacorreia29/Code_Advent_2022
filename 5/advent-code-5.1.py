#inicialFile = "./input-5-test.txt"
#auxiliarFileAppend = "-test"
inicialFile = "./input-5.txt"
auxiliarFileAppend = ""

def getProcedures():
    file = open(inicialFile)
    inProcedure = False
    procedures = []
    for line in file:           
        if line == "\n":
            inProcedure = True
        elif inProcedure:
            line = line.split("\n")[0]
            procedures.append(line)
    return procedures

def processProcedure(procedure):
    characters = procedure.split(" ")
    num = characters[1]
    moveFrom = characters[3]
    moveTo = characters[5]
    print(num, moveFrom, moveTo)
    return [num, moveFrom, moveTo]

def getCrateLine(line):
    count = 0
    lineCrates = []
    for character in line:
        if count == 0 or count == 2:
            count += 1
        elif count == 1:
            lineCrates.append(character) 
            count += 1
        elif count == 3:
            count = 0
    return lineCrates

def getCrates(file):
    inProcedure = False
    crates = []
    for line in file:
        if " 1   2   3" in line:
            inProcedure = True
        elif not inProcedure:
            line = line.split("\n")[0]
            crates += [getCrateLine(line)]
    return crates

def moveCrates(crates, procedure):
    numCrates = int(procedure[1])
    moveFrom = int(procedure[3]) - 1
    moveTo = int(procedure[5]) - 1

    for num in range(0, numCrates):
        placed = False
        for line in crates:
            crate = line[moveFrom]
            if crate != " " and not placed:
                #remove crate from original spot
                line[moveFrom] = " "

                #add crate to destination spot
                reverseCrates = crates[::-1]
                ##find an empty spot
                for line in reverseCrates:
                    if line[moveTo] == " " and not placed:
                        line[moveTo] = crate
                        placed = True
                ##new top line             
                if placed == False:
                    newLine = []
                    for i in range(0, len(crates[0])):
                        if i == moveTo:
                            newLine.append(crate)
                        else:
                            newLine.append(" ")
                    reverseCrates += [newLine]
                    placed = True
                crates = reverseCrates[::-1]
    return crates

def writeCrates(crates, fileIndex):
    crateFile = open("./input-5." + str(fileIndex) + auxiliarFileAppend +".txt", "w+")
    fileIndex += 1

    #crates
    for lineCrates in crates:
        i = 0
        for character in lineCrates:
            if i != 0:
                crateFile.write(" ")
            if character == " ":
                crateFile.write("   ")
            else:
                crateFile.write("[" + character + "]")
            i += 1
        crateFile.write("\n")

    #numbers
    for j in range(1, len(crates[0]) + 1):
        crateFile.write(" " + str(j) + "  ")
    crateFile.write("\n")



def main():
    fileIndex = 0
    procedures = getProcedures()
    for procedure in procedures:
        procedure = procedure.split(" ")
        #read file
        if fileIndex == 0:
            file = open(inicialFile)
        else:
            file = open("./input-5." + str(fileIndex) + auxiliarFileAppend + ".txt")
        crates = getCrates(file)

        #move crates
        crates =  moveCrates(crates, procedure)

        #write
        fileIndex += 1
        writeCrates(crates, fileIndex)

main()