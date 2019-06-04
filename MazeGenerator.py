#import os
from maze_functions import *

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
        print(ways)
        # - If we only have one item or more in "ways", we choose one randomly
        # - If "ways" is empty, we have to stop there, and put that as the final cell
        #   of our incredible path

        if len(ways) > 0:
            # We randomly choose a cell from ways
            a = ways[randomInt(0, len(ways) - 1)]
            tab[a] = 1
            #print(a)

            # At the end, path contains the path to go out
            path.append(a)

        else:
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
                        #print(a)

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
    place = floor(gaussianRandom(len(path) * 0.25, len(path) * (1 - 0.25)))
    tab[path[place]] = 4
    return tab

# Algorithm

maze = mazeGenerator(10,1)
print(len(maze))
printMaze(maze)

#os.system("pause")
