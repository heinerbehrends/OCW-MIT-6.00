def solve1(numLegs, numHeads):
    for numSpiders in range(0, numHeads + 1):
        for numChicks in range(0, numHeads + 1):
            numPigs = numHeads - numSpiders - numChicks
            totLegs = 8*numSpiders + 2*numChicks + 4*numPigs
            if totLegs == numLegs:
                return (numPigs, numChicks, numSpiders)
    return (None, None, None)

def barnYard1():
    heads = int(raw_input("Enter number of heads: "))
    legs = int(raw_input("Enter number of legs: "))
    pigs, chicks, spiders = solve1(legs, heads)
    if pigs == None:
        print "There is no solution"
    else:
        print "Number of pigs: ", pigs
        print "Number of chickens: ", chicks
        print "Number of spiders: ", spiders


