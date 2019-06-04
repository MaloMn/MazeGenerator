from math import floor, sqrt
from random import random

#######################################
### Functions helping the generator ##
#######################################

def randomInt(a, b):
    c = 0
    if a > 0:
        c = floor(random() * b) + a
    else:
        c = floor(random() * (b + 1))

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

def surroundings(t, n):
    
    """We check all the surroundings of the given cell, and we return them in an array:
    0 if we can't go there, and 1 if we can."""
    
    length = sqrt(len(t))

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
    return floor(start + gaussianRand() * (end - start + 1))

def gaussianRand():
    rand = 0
    for i in range(6):
        rand += random()
    return rand / 6

#######################
### Other functions ###
#######################

def printMaze(array):
    """Used to print the maze in a square
    so it is easily readable"""
    other = []
    for i in range(len(array)):
        other.append('[' + str(array[i]) + ']')
    l = floor(sqrt(len(array)))
    for i in range(l):
        line = ''
        for j in range(l):
            line += str(other[i*l + j])
        print(line)