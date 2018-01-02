from string import find
import time
start_time = time.time()

##def countSubStringMatchSimple(stringA, stringB, start):
##    indexFound = ()
##    if find(stringA, stringB, start) == -1:
##        return -1
##    else:       
##        indexFound += (find(stringA, stringB),countSubStringMatchSimple(stringA, stringB, start) + 1)
##        print indexFound
##    return indexFound
##    
##print countSubStringMatchSimple("atgacagcaatcatgccaatgcagtatgcatatgctcgagatatgc","atgc",0)

##firstOccurence = find("atgacagcaatcatgccaatgcagtatgcatatgctcgagatatgc", "atgc", 0)
##print firstOccurence
##def findFirstOccurence(target, key, start):
##    

def countSubStringMatchRecursiveSimple(target, key, start):
    start = find(target, key, start)
    indexFound = []
    if start == -1:
        return "-1 Done"
    else:
        print start
        countSubStringMatchRecursiveSimple(target, key, start + 1)
        return "Done"

print countSubStringMatchRecursiveSimple("atgacagcaatcatgccaatgcagtatgcatatgctcgagatatgc", "atgc", 0)
print("--- %s seconds ---" % (time.time() - start_time))


##def countSubStringMatchRecursiveCount(target, key, start):
##    indexFound = (0,)
##    if indexFound[-1] == -1:
##        return "Done"
##    else:
##        indexFound += countSubStringMatchRecursiveCount(target, key, indexFound[-1] + 1)
##        print indexFound
##        return "Done"

##print countSubStringMatchRecursiveCount("atgacagcaatcatgccaatgcagtatgcatatgctcgagatatgc", "atgc", 0)
