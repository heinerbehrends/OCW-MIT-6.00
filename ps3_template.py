from string import *

def subStringMatchExact(stringA, stringB):
    indexFound =(-1,0)
    counter = 0
    for x in stringA:
        if indexFound[-1] != find(stringA, stringB, counter):
            indexFound += (find(stringA, stringB, counter),)
        counter += 1
    return indexFound[2:len(indexFound)-1]
    print("--- %s seconds ---" % (time.time() - start_time))

def constrainedMatchPair(firstMatch, secondMatch, length):
    matches = ()
    for n in firstMatch:
        for k in secondMatch:
            if n + length + 1 == k:
                matches += (n,)
                print matches
    return matches
                


def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers

print subStringMatchOneSub("atgc", "atgaatgcatggatgtaaatgcag")



    







            



