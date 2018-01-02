def fact0(i):
    assert type(i) == int and i >= 0
    if i == 0 or i == 1:
        return 1
    else: print 'ieeh'
    return i * fact0(i-1)
    

##for i in range(1,9):
##    print fact0(i)
    
"""fact0(i) is linear. It takes i steps to finish"""

def fact1(i):
    assert type(i) == int and i >= 0
    res = 1
    while i > 1:
        res = res * i
        i -= 1
        print 'ieeh'
    return res

##for i in range(1,5):
##    print fact1(i)

"""fact1(i) is linear. It takes i steps to finish"""

def makeSet(s):
    assert type(s) == str
    res = ''
    for c in s:
        print 'ieh'
        if not c in res:
            res = res + c
    return res

##print makeSet('hallo')

"""makeSet(s) is linear. It takes len(s) steps to finish"""

def intersect(s1, s2):
    assert type(s1) == str and type(s2) == str
    s1 = makeSet(s1)
    s2 = makeSet(s2)
    res = ''
    for e in s1:
        print 'aaahh'
        if e in s2:
            print 'aah'
            res = res + e
    return res

print intersect('lowest', 'ggggggt')
