nonDividable = (0,1)
testNumber = 1

while nonDividable[-1] - nonDividable[-2] <= 5:
    solutionFound = False
    for numSix in range (0,testNumber/6 + 1):
        for numNine in range (0,testNumber/9 + 1):
            for numTwenty in range (0,testNumber/20 + 1):
                if testNumber == numSix*6 + numNine*9 + numTwenty*20:
                  ##  print testNumber
                    solutionFound = True
    if solutionFound == False:
        nonDividable += (testNumber,)
    testNumber += 1
print "Largest number of McNuggets that cannot be bought in exact quantity: ",nonDividable[-1]
    
