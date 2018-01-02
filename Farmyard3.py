def solve2(numLegs, numHeads):
    solutionFound = False
    for numSpiders in range (0, numHeads + 1):
        for numChicks in range (0, numHeads + 1):
            numPigs = numHeads - numSpiders - numChicks
            if numPigs > 0:
                totLegs = numSpiders*8 + numChicks*2 + numPigs*4
                if totLegs == numLegs:
                    print "Number of pigs: " + str(numPigs) + ", ",
                    print "Number of chicken: " + str(numChicks) + ", ",
                    print "Number of spiders: " + str(numSpiders) + ", ",
                    solutionFound = True
    if not solutionFound: print "There is no solution."

solve2(256, 64)
