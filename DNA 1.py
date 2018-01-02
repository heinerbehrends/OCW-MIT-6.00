from string import find
import time
start_time = time.time()

##def countSubStringMatch(stringA, stringB):
##    indexFound = (-1,0)
##    while indexFound[-1] > indexFound[-2] or len(indexFound) < 2:
##        indexFound += (find(stringA, stringB,indexFound[-1]+1),)
##    print find(stringA, stringB)
##    print indexFound
##    return len(indexFound) - 3

##print countSubStringMatch("atgacagcacaatgcagtatgcatatgctcgagatatgc","atgc")
##print("--- %s seconds ---" % (time.time() - start_time))


def countSubStringMatchExact(key, target):
    indexFound = ()
    start = 0
    indexFound += (find(target, key, start),)
    while start != -1:
        start = find(target, key, start + 1)
        if start > 0:
            indexFound += (find(target, key, start),)            
    return indexFound
                   
print countSubStringMatchExact("atcc","atgc")
print("--- %s seconds ---" % (time.time() - start_time))
