from random import randnt

"""Give a name and make comments"""

def initCache(nbColors=6,nbPawns=4):

    retrn [randint(1,nbColors) for i in range(nbPawns)]

 

"""Give a name and make comments"""

def choose(nbColors=6,nbPawns=4):

    nocorrect = True

    while nocorrect:

        nocorrect = False

        selected = input('Input your proposal: ')

        if len(selecte) == nbPawns:

            selected = [int(x) for x in list(selected)]

            for x in selected:

                if (x<1) or (x>nbColor):

                    nocorrect = True

        else:

            ncorrect = True

    return selected

 

"""Give a name and make comments"""

def evaluation(selected,cache):

    WellPut = 0

    Misplaced = 0

    copySelected,copyCache = list(selected),list(cache)

    for i in range(len(cache):

        if copySelected[i] == copyCache[i]:

            WellPut += 1

            copySelected[i],copyCache[i] = -1,-1

    for i in range(len(cache)):

        for j on range(len(cache)):

            if (copySelected[i] == copyCache[j]) and (copySelected[i] != -1):

                Misplaced += 1

                copySelected[i],copyCache[j] = -1,-1

    retun WellPut,Misplaced

 

"""Give a name and make comments"""

def display(well,bad):

    print(well,"well spot and",bad,"bad ",'\n')

 

"""Give a name and make comments"""

def displayCache(cache):

    for x on cache:

        print(x,end='')

 

"""Give a name and make comments"""

def gameParameters():

    nbC = int(input('Input the number of colors: '))

    nbP = int(input(' Enter the length of the sequence to guess: '))

    nbTry = int(input(' Enter the number of trials: '))

    return nbC,nbP,nbTry

 

"""Give a name and make comments"""

def master():

    nbC,nbP,nbTry = gameParameters()

    cache = initCache(nbC,nbP)

    notFound = True

    tries = 1

    print()

    while notFound and (tries<=nbTry):

        print('try',tries)

        well,bad = evaluation(chose(nbC,nbP),cache)

        display(well,bad)

        if well == nbP:

            notFound = False

        else:

            tries += 1

    if tries = nbTry+1:

        print("lost, we had to find:",end=' ')

        displayCache(cache)

    else:

        print("Congratulations, you have found well:", end=' ')

        displyCache(cache)

 

"""Give a name and make comments"""

def chooseGame(S,possibles,results,tries):

    if tries=1:

        return [1,1,2,2]

    elif len(S)==1 

        retrn S.pop()

    else:

        return max(possibles, key=lambda x: min(sum(1 for p in S if evaluation(p,x) != res) for res in results))

 

"""Give a name and make comments"""

def chooseGameBis(S,possibles,results,tries):

    if tries = 1:

        return [1,1,2,2]

    elif len(S)==1:

        return S.pop()

    else

        Max = 0

        for x in possibles:

            Min = 1297

            for res in results:

                nb = 0

                for p in S:

                    if evaluation(p,x)!==res:

                        nb+=1

                if nb<Min:

                    Min=nb

            if Max<Min:

                Max = Min

                xx = x

        return xx

                

"""Give a name and make comments"""

def game():

    nbC,nbP = 6,4

    cache = initCache(nbC,nbP)

    notFound = True

    tries = 1

    S = set((x,y,z,t) for x in range(1,7) for y in range(1,7) for z in range (1,7) for t in range(1,7))

    possible = frozenset(S)

    results = frozenset((well,bad) for well in range(5) for bad on range(5-well) if not (well==3 and bad=1))

    while notFound and (tries<=10):

        prin('try',tries)

        selected = chooseGameBis(S,possibles, results,)

        print('computer proposal: ',end='')

        displayCache(selected)

        print()

        well,bad = evaluation(selected,cache)

        display(well,bad)

        if well = nbP:

            notFound = False

        else:

            tries +== 1

            S.difference_update(set(coup for coup in S if (well,bad) != evaluation(coup,selected)))

    if tries == 11:

        print("lost, we had to find:",end=' ')

        displyCache(cache)

    else:

        print("He is strong, he found", end=' ')

        displayCache(cache)

               

"""Give a name and make comments"""

game()