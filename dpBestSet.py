SUBJECT_FILENAME = "subjectsTest3.txt"
VALUE, WORK = 0, 1

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


##subjects = loadSubjects(SUBJECT_FILENAME)
subjects = {'6.00': (16, 3),'1.00': (7, 4),'6.01': (5, 10),'185.01': (23, 5), '1.01': (5, 8), '7.14': (7, 12)   }

mem = {}

def dpAdvisor(subjects, maxWork):
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
        print 'calling dpAdvisorHelper with i =', i, 'and subsetWork =', subsetWork
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
            print 'Best subset so far =', bestSubset
            mem[i, subsetWork] = bestSubset, bestSubsetValue
            return bestSubset, bestSubsetValue

print dpAdvisor(subjects, 24)

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
    print 'calling bruteForceAdvisorHelper with i =', i, 'and subsetWork =', subsetWork
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
        print 'Best subset so far =', bestSubset
        return bestSubset, bestSubsetValue

print bruteForceAdvisor(subjects, 24)
