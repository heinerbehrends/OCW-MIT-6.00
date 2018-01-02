# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
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

    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    rearrange_dict = {}
    list_of_keys = []
    list_of_tuples = []
    for line in inputFile:
        list_of_keys.append(line.split(',')[0].strip())
        list_of_tuples.append((int(line.split(',')[1].strip()), int(line.split(',')[2].strip())))
    for n in range(len(list_of_keys)):
            rearrange_dict[list_of_keys[n]] = list_of_tuples[n]
    return rearrange_dict
    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).


##rearrange_dict = loadSubjects('subjects.txt')
rearrange_dict = {'6.00': (16, 8),'1.00': (7, 7),'6.01': (5, 3),'15.01': (9, 6)}
##print rearrange_dict




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
##def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
def chooseBestValue(subjects, maxWork, comparator):
    """returns a list of the tuple with the best value, the key and True if
    it fits in maxWork"""
    keys = []
    temp = []
##    value = []
    index = 0
    ans = []
    fits_or_not = False
    for key in subjects:
        keys.append(key)
    
    print keys
    temp = rearrange_dict[keys[0]]
    print temp
    for i in range(1,len(keys)):
        if not comparator(temp, rearrange_dict[keys[i]]) == True:
            temp = rearrange_dict[keys[i]]
            index = i
            print temp, keys[index]
            print rearrange_dict[keys[i]]
        else: print temp, keys[index], index
    fits_or_not = temp[1] <= maxWork
    ans.append(temp)
    ans.append(keys[index])
    ans.append(fits_or_not)
    return ans
    
    

def greedyAdvisor(chooseBestValue, maxWork):
    ans = []
    work_left = maxWork
    res = {}
    subjects = dict(rearrange_dict)
    ans = chooseBestValue
    if ans[2] == True:
        print ans
        print ans[0][1]
        print subjects[ans[1]]
        res[ans[1]] = ans[0]
        print res
        work_left -= ans[0][1]
        print work_left
        del subjects[ans[1]]
    else: del subjects[ans[1]]
    return res
    
            
##    if comparator(rearrange_dict[keys[0]], rearrange_dict[keys[1]]) == True:
##        temp = (rearrange_dict[keys[0]],)
##        print 'temp is here', temp
##    else: temp = rearrange_dict[keys[1]]
##    for i in range(2, len(keys) - 1):
##        print 'value of key[i]', rearrange_dict[keys[i]]
##        if comparator(rearrange_dict[keys[i]], temp[0]) == True:
##            temp = (rearrange_dict[keys[i]],)
##        print temp
##            
##    return temp

##print chooseBestValue(rearrange_dict, 15, cmpValue)
print greedyAdvisor(chooseBestValue(rearrange_dict, 15, cmpValue), 15)

    # TODO...

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
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
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...

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
