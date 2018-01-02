numSix = 0
numNine = 0
numTwenty = 0
nonDividable =(0,1,)
dividable = (0,)
solutionFound = False
testNumber = 1

##for testNumber in range(0, 55):
while nonDividable[-1] - nonDividable[-2] < 5:
    for numSix in range(0, 34):
        for numNine in range(0, 12):
            for numTwenty in range(0, 3):
                if testNumber == numSix*6 + numNine*9 + numTwenty*20:
                    dividable += (testNumber,)
                    testNumber += 1
    nonDividable += (testNumber,)
    testNumber += 1
print nonDividable
print dividable
            
