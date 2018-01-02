def fastMaxVal(w, v, i, aW, m): 
    global numCalls 
    numCalls += 1 
    print 'calling fuction with i =', i,'and aW =', aW,'.'
    try:
        return m[(i, aW)]
    except KeyError:
        print 'no dictionary value for i =', i, 'and aW =', aW,'checking if i == 0'
        if i == 0:
            print 'i is zero'
            if w[i] <= aW:
                print 'i == 0 fits. returns value of only the last item:', v[i]
                m[(i, aW)] = v[i]
                print 'm looks like this now', m
                print 'i =', i
                return v[i] 
            else: 
                m[(i, aW)] = 0
                print 'm looks like this now', m
                print 'Last item does not fit. Returning 0.'
                return 0
        print 'i is not 0. Calling function recursively for i-1'
        without_i = fastMaxVal(w, v, i-1, aW, m)
        print 'recursive function of i-1 is now', without_i
        if w[i] > aW:
            print 'i =', i, 'does not fit. without_i is now', without_i
            m[(i, aW)] = without_i
            print 'm looks like this now', m
            return without_i 
        else:
            print 'i =',i ,'does fit'
            with_i = v[i] + fastMaxVal(w, v, i-1, aW - w[i], m)
            print 'subtracted 1 from i and', w[i], 'from aW.'
            print 'i is now', i, 'aW is now', aW
            print 'with i is now the result of v[i]', v[i],'plus the function of i-1.'
        res = max(with_i, without_i) 
        m[(i, aW)] = res 
        print 'added the max of with_i and without_i to m', m
    return (i, aW)



def maxVal0(w, v, i, aW): 
    m = {} 
    return fastMaxVal(w, v, i, aW, m)

w = [3,4,5]
v = [1,12,3]
i = len(w)-1
aW = 8
numCalls = 0

print maxVal0(w, v, i, aW)
