import math
import random

#######################################################################
##################### Random Path Generator ###########################
#######################################################################

def mazeGenerator(size, level):
    # We fill the grid with zeros
    tab = []
    for i in range(size*size):
        tab.append(0)

    # We then select the starting square
    # Start (st) is an index
    st = randomStart(size)

    tab[st] = 2

    # Then we keep moving on randomly into the maze until we are stuck.
    #    0
    # 3 [ ] 1  This is how a cell is surrounded
    #    2
    a = st
    ways = []
    path = [a]

    while "As long as len(ways) > 0":
        # We check which ways are possible by eliminating impossible ways
        ways = surroundings(tab, size, a)

        # - If we only have one item or more in "ways", we choose one randomly
        #           - If "ways" is empty, we have to stop there, and put that as the final cell
        #           of our incredible path

        if len(ways) > 0:
            # We randomly choose a cell from ways
            a = ways[randomInt(0, len(ways) - 1)]
            tab[a] = 1
            #print(a)

        # At the end, path contains the path to go out
        path.append(a)

        if len(ways) > 0:
            break

    tab[a] = 3

    if level == 1:
        for i in range(len(path)):
            if randomInt(0, 1) == 0:
                while "len(ways) > 0":
                    # We recreate some other paths without exits.
                    ways = surroundings(tab, size, path[i])

                    if len(ways) > 0:
                        # We randomly choose a cell from ways
                        a = ways[randomInt(0, len(ways) - 1)]
                        tab[a] = 1
                        print(a)

                    if len(ways) > 0:
                        break

    elif level == 2:
        # We completely fill the grid with false ways
        for i in range(len(path)):
            while "len(ways) > 0":
                # We recreate some other paths without exits.
                ways = surroundings(tab, size, path[i])
                #print('Ways = ' + ways)
                if len(ways) > 0:
                    # We randomly choose a cell from ways
                    a = ways[randomInt(0, len(ways) - 1)]
                    tab[a] = 1
                    #print(a)

                if len(ways) > 0:
                    break


    print('Path = ', path)
    # Now we add the item on the maze :
    # First the item 1 : the candle
    place = math.floor(gaussianRandom(len(path) * 0.25, len(path) * (1 - 0.25)))
    tab[path[place]] = 4
    return tab

#######################################
### Functions helping the generator ##
#######################################

def randomInt(a, b):
    c = 0
    if a > 0:
        c = math.floor(random.random() * b) + a
    else:
        c = math.floor(random.random() * (b + 1))

    return c

def randomStart(length):
    # indicates the line chosen or the column depending on lc
    line = randomInt(1, length - 2)
    # lc indicates the side
    lc = randomInt(1, 4)

    if lc == 1:
        # left side
        indice = length * line
    elif lc == 2:
        # upper side
        indice = line

    elif lc == 3:
        # right side
        indice = length * line + length - 1

    else:
        # bottom side
        indice = line + length * (length - 1)

    return indice

def removeItem(array1, item):
    array2 = []

    for i in range(len(array1)):
        array2.append(array1[i])

    for i in range(len(array1)):
        if (array1[i] != item):
            array2.append(array1[i])

    #print(array2)
    return array2

def checkIfExists(tabl, condition, pos, bool):
    # condition la conditions d'existence  pos = position de la case a checker
    # We check the surroundings of the cell around n
    if condition: # We check that it exists
        if tabl[pos] != 0:
            bool = false
    return bool

def surroundings(t, length, n):
    # We check all the surroundings of the given cell, and we return them in an array:
    # 0 if we can't go there, and 1 if we can.
    ######## STEP 1 ########
    # First, we check the immediate surroundings (A (condititon) to B (zeros and ones))
    # Then, the others (B to D)
    A = [n - length, n + 1, n + length, n - 1]
    B = [1, 1, 1, 1]
    C = [n - length - 1, n - 2 * length, n - length + 1, n + 2, n + length + 1, n + 2 * length, n + length - 1, n - 2]
    D = [1, 1, 1, 1, 1, 1, 1, 1]

    # Checking the immediate surroundings :
    for i in range(len(A)):
        try:
            if t[A[i]] != 0:
                B[i] = 0
        except IndexError:
            B[i] = 0

    # Checking the other surroundings :
    for i in range(len(C)):
        try:
            if t[C[i]] != 0:
                D[i] = 0
        except IndexError:
            D[i] = 1

    # Then we delete the cases where the cells aren't actually next to the main one.
    column = n % length

    if column == 1:
        D[7] = 1
    elif column == 0:
        B[3] = 0
    elif column == length - 2:
        D[3] = 1
    elif column == length - 1:
        B[1] = 0

    ######## STEP 2 ########
    # We construct an array "possible" in which we sort out which cell we can go to
    # according to what we have done before
    possible = [n - length, n + 1, n + length, n - 1]

    if B[0] == 1:
        if D[0] == 0 or D[1] == 0 or D[2] == 0:
            possible = removeItem(possible, n - length)
    else:
        possible = removeItem(possible, n - length)

    if B[1] == 1:
        if D[2] == 0 or D[3] == 0 or D[4] == 0:
            possible = removeItem(possible, n + 1)
    else:
        possible = removeItem(possible, n + 1)

    if B[2] == 1:
        if D[4] == 0 or D[5] == 0 or D[6] == 0:
            possible = removeItem(possible, n + length)
    else:
        possible = removeItem(possible, n + length)

    if B[3] == 1:
        if D[6] == 0 or D[7] == 0 or D[0] == 0:
            possible = removeItem(possible, n - 1)
    else:
        possible = removeItem(possible, n - 1)
    # "possible" now contains the ways to go
    return possible

def gaussianRandom(start, end):
    return math.floor(start + gaussianRand() * (end - start + 1))

def gaussianRand():
    rand = 0
    for i in range(6):
        rand += random.random()
    return rand / 6

#######################
### Other functions ###
#######################

def printMaze(list):
