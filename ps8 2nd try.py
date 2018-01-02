# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjectsEvenShorter.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    inputFile = open(filename)
    subjects = {}
    list_of_keys = []
    list_of_tuples = []
    for line in inputFile:
        list_of_keys.append(line.split(',')[0].strip())
        list_of_tuples.append((int(line.split(',')[1].strip()), int(line.split(',')[2].strip())))
    for n in range(len(list_of_keys)):
            subjects[list_of_keys[n]] = list_of_tuples[n]
    return subjects

subjects = loadSubjects(SUBJECT_FILENAME)
##subjects = {'6.00': (16, 3),'1.00': (7, 4),'6.01': (5, 10),'185.01': (23, 5)}

##print subjects

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

##printSubjects(subjects)

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def stopOrContinue(dictionary, maxWork):
    """returns True if there is a work value in dict <= maxWork"""
    work_list = []
    for items in dictionary:
        work_list.append(dictionary[items][WORK])
    if len(work_list) < 1:
        return False
    return min(work_list) <= maxWork

##print stopOrContinue(subjects, 1)

def findBest(dictionary, comparator):
    """returns a list containing the best name and corresponding
    value-work tuple. The choice depends on the comparator function."""
    keyList = []
    keyIndex = 0
    res = []
    for key in dictionary:
        keyList.append(key)
    compareTemp = dictionary[keyList[0]]
    for i in range(1 ,len(keyList)):
        if not comparator(compareTemp, dictionary[keyList[i]]) == True:
            compareTemp = dictionary[keyList[i]]
            keyIndex = i
    res.append(keyList[keyIndex])
    res.append(compareTemp)
    return res
                                     


##print findBest(subjects, cmpRatio)

res ={}

def greedyAdvisor(dictionary, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    relies on res = {} outside of the function
    """
    dictCopy = dict(dictionary)
    bestKey, bestValueWork = findBest(dictCopy, comparator)
    res[bestKey] = bestValueWork
    del dictCopy[bestKey]
    maxWork -= bestValueWork[1]
    if not stopOrContinue(dictCopy, maxWork) == True:
        return 
    else:
        greedyAdvisor(dictCopy, maxWork, comparator)
        
##greedyAdvisor(subjects, 15, cmpWork)

        
def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, len(subjects)-1, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
##    print 'calling bruteForceAdvisorHelper with i =', i, 'and subsetWork =', subsetWork
    if i == 0:
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
##            print 'New bestSubsetValue =', subset
            return subset[:], subsetValue
##            print 'New bestSubsetValue =', subset
##            print 'New bestSubset =', subsetValue
        else:
            # Keep the current best.
##            print 'The best subset is still', subset
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
##            print 'i fits so Subset =', subset
##            print 'Changing i to', i-1,'and subsetWork to ', subsetWork + s[WORK],' and call recursive.'
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i-1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
##            print 'None of the items that are not in the set fit. Removing', subset[-1],'from subset.'
            subset.pop()
##            print 'After .pop Subset =', subset
##        print 'i does not fit so subset =', subset
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i-1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
##        print 'Best subset so far =', bestSubset
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#

    

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance

#
# Problem 4: Subject Selection By Dynamic Programming
#


def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    mem = {}
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            dpAdvisorHelper(tupleList, maxWork, len(subjects)-1, None, None, [], 0, 0, mem)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects


def dpAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork, mem):
    #check if computation is in mem and return the value
    try:
        return mem[i, subsetWork]
    #if calculation is not in mem compute it.
    except KeyError:
        # Hit the end of the list.
##        print 'calling bruteForceAdvisorHelper with i =', i, 'and subsetWork =', subsetWork
        if i == 0:
            if bestSubset == None or subsetValue > bestSubsetValue:
                # Found a new best.
##                print 'New bestSubsetValue =', subset
                mem[i, subsetWork] = subset[:], subsetValue
                return subset[:], subsetValue
##                print 'New bestSubsetValue =', subset
##                print 'New bestSubset =', subsetValue
            else:
                # Keep the current best.
##                print 'The best subset is still', subset
                mem[i, subsetWork] = bestSubset, bestSubsetValue
                return bestSubset, bestSubsetValue
        else:
            s = subjects[i]
            # Try including subjects[i] in the current working subset.
            if subsetWork + s[WORK] <= maxWork:
                subset.append(i)
##                print 'i fits so Subset =', subset
##                print 'Changing i to', i-1,'and subsetWork to ', subsetWork + s[WORK],' and call recursive.'
                bestSubset, bestSubsetValue = dpAdvisorHelper(subjects,
                        maxWork, i-1, bestSubset, bestSubsetValue, subset,
                        subsetValue + s[VALUE], subsetWork + s[WORK], mem)
##                print 'None of the items that are not in the set fit. Removing', subset[-1],'from subset.'
                subset.pop()
##                print 'After .pop Subset =', subset
##            print 'i does not fit so subset =', subset
            bestSubset, bestSubsetValue = dpAdvisorHelper(subjects,
                    maxWork, i-1, bestSubset, bestSubsetValue, subset,
                    subsetValue, subsetWork, mem)
##            print 'Best subset so far =', bestSubset
            mem[i, subsetWork] = bestSubset, bestSubsetValue
            return bestSubset, bestSubsetValue

##print dpAdvisor(subjects, 18)

def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...
    res = {}
    length = len(subjects)
    start_time = time.time()
    res = bruteForceAdvisor(subjects, 24)
    end_time = time.time()
    total_time = end_time - start_time
    print 'It took', total_time, 'to compute an answer. The length of the list was ',length,'.'
    return res


print bruteForceTime()

def dpAdvisorTime():
    """
    runs dpAdvisor and measures the time required to compute an answer.
    """
    res = {}
    length = len(subjects)
    start_time = time.time()
    res = dpAdvisor(subjects, 24)
    end_time = time.time()
    total_time = end_time - start_time
    print 'It took', total_time, 'to compute an answer. The length of the list was ',length,'.'
    return res
    
##print dpAdvisorTime()


####def dpAdvisor(subjects, maxWork):
####    """
####    Returns a dictionary mapping subject name to (value, work) that contains a
####    set of subjects that provides the maximum value without exceeding maxWork.
####
####    subjects: dictionary mapping subject name to (value, work)
####    maxWork: int >= 0
####    returns: dictionary mapping subject name to (value, work)
####    """
####    mem = {}
####    nameList = subjects.keys()
####    tupleList = subjects.values()
######    print tupleList
####    aW = maxWork
####    i = len(nameList) - 1
####    return dpAdvisorHelper(tupleList[i][WORK], tupleList[i][VALUE], i, aW, mem), mem
######    outputSubjects = {}
######    for i in bestSubset:
######        outputSubjects[nameList[i]] = tupleList[i]
######    return outputSubjects# TODO...
####
####def dpAdvisorHelper(w, v, i, aW, m):
####    tupleList = subjects.values()
####    #Check whether this has been computed before
####    #and return it
####    try:
####        return m[(i, aW)]
####    #if it has not been computed yet...
####    except KeyError:
####        # ...and we look at the last item we come to the base case
####        if i == 0:
####            # ...and its weight is less or equal than the available weight
####            if tupleList[i][WORK] <= aW:
####                #we either include it and save its value to the matrix
####                m[(i, aW)] = tupleList[i][VALUE]
####                #and return the value
####                return tupleList[i][VALUE]
####            #if it does not fit...
####            else:
####                #or we can't include it and save 0 to the matrix
####                m[(i, aW)] = 0
####                #and return 0
####                return 0
####        #the highest possible value for the amount of weight and looking at item up to i
####        #has not been computed yet and we are not looking at the last item
####        #If we don't take it the highest possible value will be f(i-1, aW)
####        #Variable without_i holds the highest value if we don't include i
####        without_i = dpAdvisorHelper(w, v, i-1, aW, m)
####        #if the item i weights too much, save and return without_i
####        if tupleList[i][WORK] > aW:
####            m[i, aW] = without_i
####            return without_i
####        #if the item does fit, add the value and substract the weight
####        #and compute f(i-1, aW - w[i])
####        else:
####            with_i = tupleList[i][VALUE] + dpAdvisorHelper(w, v, i-1, aW - tupleList[i][WORK], m)
####        #Variable res holds the max of without_i (not including i)
####        #and with_i (including i). Save that value to the matrix and return it
####        res = max(with_i, without_i)
####        m[(i, aW)] = res
####    return res
            
##print dpAdvisor(subjects, 8)

####
####def dpAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
####                            subset, subsetValue, subsetWork, mem):
####    print 'calling dpAdvisorHelper with', i, 'and maxWork =', maxWork
####    try:
####        print 'mem[i,maxWork] = ',mem[i,maxWork]
####        return mem[i, maxWork]
####    except KeyError:
####        print 'KeyError'
####        print i
####        s = subjects[i]
####        print subjects[i]
####        if i == 0:
####            print bestSubset
####            if bestSubset == None or subsetValue > bestSubsetValue:
####                print 'newBest'# Found a new best.
####                mem[i, maxWork] = dpAdvisorHelper(subjects,
####                    maxWork, i, bestSubset, bestSubsetValue, subset,
####                    subsetValue + s[VALUE], subsetWork + s[WORK])
####                return subset[:], subsetValue
####            else:
####                # Keep the current best.
####                return bestSubset, bestSubsetValue
####        else:
####            s = subjects[i]
####            # Try including subjects[i] in the current working subset.
####            if subsetWork + s[WORK] <= maxWork:
####                subset.append(i)
####                print 'Subset =', subset
####                mem[i, maxWork] = bruteForceAdvisorHelper(subjects,
####                        maxWork, i-1, bestSubset, bestSubsetValue, subset,
####                        subsetValue + s[VALUE], subsetWork + s[WORK])
####                print mem
####                bestSubset, bestSubsetValue = mem[i, maxWork]
####                subset.pop()
####            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
####                    maxWork, i-1, bestSubset, bestSubsetValue, subset,
####                    subsetValue, subsetWork)
####            print mem
####            return bestSubset, bestSubsetValue
####        
##print dpAdvisor(subjects, 8)
##
##mem = {}
##tupleList = subjects.values()
##print 'mem = ',mem







#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
