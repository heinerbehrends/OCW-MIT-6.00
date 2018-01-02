def mcNuggetPackage(x,y,z):
    """returns the largest number that does not divide by multiples of the three numbers that are input. Input integers > 1 ordered from smallest to largest."""
    nonDividable = (0,1)
    testNumber = 1
    while nonDividable[-1] - nonDividable[-2] <= y-x or nonDividable[-1] - nonDividable[-2] <= z-(x+y):
        solutionFound = False
        for numA in range (0,testNumber/x + 1):
            for numB in range (0,testNumber/y + 1):
                for numC in range (0,testNumber/z + 1):
                    if testNumber == numA*x + numB*y + numC*z:
                        solutionFound = True
        if solutionFound == False:
            nonDividable += (testNumber,)
        if testNumber < 200:
            testNumber += 1
        else:
            return (nonDividable[-1],x,y,z)
    return (nonDividable[-1],x,y,z)

ans = mcNuggetPackage(11,19,23)
if ans[0] != 200:
    print "Given package sizes %d, %d, and %d, the largest number of McNuggets that cannot be bought in exact quantity is: %d." % (ans[1],ans[2],ans[3],ans[0])
else: print "Given package sizes %d, %d, and %d, there is no number smaller than 200 of McNuggets that cannot be bought in exact quantity." % (ans[1],ans[2],ans[3])
