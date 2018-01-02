from string import find
import time
start_time = time.time()

def countSubStringMatchExact(stringA, stringB):
    indexFound =()
    counter = 0
    start = 0
    for x in stringA:
        if indexFound[-1] != find(stringA, stringB, counter):
            indexFound += (find(stringA, stringB, counter),)
        counter += 1
    return indexFound[2:len(indexFound)-1]
    print("--- %s seconds ---" % (time.time() - start_time))

print countSubStringMatchExact("atgaatgcatggatgtaaatgcag","a")
print("--- %s seconds ---" % (time.time() - start_time))
