#######################################################################
##################### Random Path Generator ###########################
#######################################################################

def mazeGenerator(size, level) {
  # We fill the grid with zeros
  tab = [];
  for i in range(size*size):
    tab[i] = 0;

  # We then select the starting square
  # Start (st) is an index
  var st = randomStart(size);

  tab[st] = 2;

  # Then we keep moving on randomly into the maze until we are stuck.
/*
         0
      3 [ ] 1  This is how a cell is surrounded
         2
    */
  var a = st;
  var ways = [];
  path = [a];

  do {
    # We check which ways are possible by eliminating impossible ways
    ways = surroundings(tab, size, a);

/*  - If we only have one item or more in "ways", we choose one randomly
            - If "ways" is empty, we have to stop there, and put that as the final cell
            of our incredible path
        */
    if (Taille(ways) > 0) {
      # We randomly choose a cell from ways
      a = ways[randomInt(0, Taille(ways) - 1)];
      tab[a] = 1;
      Ecrire(a);
    }
    # At the end, path contains the path to go out
    path.push(a);

  } while (Taille(ways) > 0);

  tab[a] = 3;

  if (level == 1) {

    for (i = 0; i < Taille(path); i++) {
      if (randomInt(0, 1) == 0) {
        do {
          # We recreate some other paths without exits.
          ways = surroundings(tab, size, path[i]);
          #Ecrire('Ways = ' + ways);
          if (Taille(ways) > 0) {
            # We randomly choose a cell from ways
            a = ways[randomInt(0, Taille(ways) - 1)];
            tab[a] = 1;
            Ecrire(a);
          }
        } while (Taille(ways) > 0);
      }
    }
  } else if (level == 2) {

    # We completely fill the grid with false ways
    for (i = 0; i < Taille(path); i++) {
      do {
        # We recreate some other paths without exits.
        ways = surroundings(tab, size, path[i]);
        #Ecrire('Ways = ' + ways);
        if (Taille(ways) > 0) {
          # We randomly choose a cell from ways
          a = ways[randomInt(0, Taille(ways) - 1)];
          tab[a] = 1;
          Ecrire(a);
        }

      } while (Taille(ways) > 0);
    }
  }
  Ecrire('Path = ' + path);
  # Now we add the item on the maze :
  # First the item 1 : the candle
  var place = Math.floor(gaussianRandom(Taille(path) * 0.25, Taille(path) * (1 - 0.25)));
  tab[path[place]] = 4;
  return tab;
}


#######################################
### Functions helping the generator ##
#######################################

function randomInt(a, b) {
  var c;
  if (a > 0) {
    c = Math.floor(Math.random() * b) + a;
  } else {
    c = Math.floor(Math.random() * (b + 1));
  }
  return c;
}

# Function checked

function randomStart(length) {
  # indicates the line chosen or the column depending on lc
  var line = randomInt(1, length - 2);
  # lc indicates the side
  var lc = randomInt(1, 4);

  switch (lc) {
  case 1:
    # left side
    indice = length * line;
    break;
  case 2:
    # upper side
    indice = line;
    break;
  case 3:
    # right side
    indice = length * line + length - 1;
    break;
  default:
    # bottom side
    indice = line + length * (length - 1);
    break;
  }
  return indice;
}

# function checked

function removeItem(array1, item) {
  var array2 = [];
  var a = 0;
  for (var i = 0; i < Taille(array1); i++) {
    if (array1[i] != item) {
      array2[a] = array1[i];
      a++;
    }
  }
  #Ecrire(array2);
  return array2;
}

function checkIfExists(tabl, condition, pos, bool) {
  # condition la conditions d'existence ; pos = position de la case a checker
  # We check the surroundings of the cell around n
  if (condition) { # We check that it exists
    if (tabl[pos] != 0) {
      bool = false;
    }
  }
  return bool;
}

function surroundings(t, length, n) {
  # We check all the surroundings of the given cell, and we return them in an array:
  # 0 if we can't go there, and 1 if we can.
  ######## STEP 1 ########
  # First, we check the immediate surroundings (A (condititon) to B (zeros and ones))
  # Then, the others (B to D)
  var A = [n - length, n + 1, n + length, n - 1];
  var B = [1, 1, 1, 1];
  var C = [n - length - 1, n - 2 * length, n - length + 1, n + 2, n + length + 1, n + 2 * length, n + length - 1, n - 2];
  var D = [1, 1, 1, 1, 1, 1, 1, 1];

  # Checking the immediate surroundings :
  for (var i = 0; i < Taille(A); i++) {
    if (t[A[i]] != undefined) {
      if (t[A[i]] != 0) {
        B[i] = 0;
      }
    } else {
      B[i] = 0;
    }
  }

  # Checking the other surroundings :
  for (i = 0; i < Taille(C); i++) {
    if (t[C[i]] != undefined) {
      if (t[C[i]] != 0) {
        D[i] = 0;
      }
    } else {
      D[i] = 1;
    }
  }

  # Then we delete the cases where the cells aren't actually next to the main one.
  var column = n % length;

  if (column == 1) {
    D[7] = 1;
  } else if (column == 0) {
    B[3] = 0;
  } else if (column == length - 2) {
    D[3] = 1;
  } else if (column == length - 1) {
    B[1] = 0;
  }

  ######## STEP 2 ########
  # We construct an array "possible" in which we sort out which cell we can go to
  # according to what we have done before
  var possible = [n - length, n + 1, n + length, n - 1];

  if (B[0] == 1) {
    if (D[0] == 0 || D[1] == 0 || D[2] == 0) {
      possible = removeItem(possible, n - length);
    }
  } else {
    possible = removeItem(possible, n - length);
  }

  if (B[1] == 1) {
    if (D[2] == 0 || D[3] == 0 || D[4] == 0) {
      possible = removeItem(possible, n + 1);
    }
  } else {
    possible = removeItem(possible, n + 1);
  }

  if (B[2] == 1) {
    if (D[4] == 0 || D[5] == 0 || D[6] == 0) {
      possible = removeItem(possible, n + length);
    }
  } else {
    possible = removeItem(possible, n + length);
  }

  if (B[3] == 1) {
    if (D[6] == 0 || D[7] == 0 || D[0] == 0) {
      possible = removeItem(possible, n - 1);
    }
  } else {
    possible = removeItem(possible, n - 1);
  }
  # "possible" now contains the ways to go
  return possible;
}

function gaussianRandom(start, end) {
  return Math.floor(start + gaussianRand() * (end - start + 1));
}

function gaussianRand() {
  var rand = 0;
  for (var i = 0; i < 6; i += 1) {
    rand += Math.random();
  }
  return rand / 6;
}
