poly =  (-13.39, 0.0, 17.5, 3.0, 1.0)
def evaluatePoly(poly, x):
    res = 0.0
    for i in range(len(poly)):
        if i == 0:
            res += poly[i]
        else:
##            print 'poly[i] is now ', poly[i]
            res += poly[i] * x**i
##            print 'res is now ', res
    return res

##print evaluatePoly((0.0, 0.0, 5.0, 9.3, 7.0), -13) ##  x^3

def computeDeriv(poly):
    '''
    Create a new tuple without the first element.
    '''
    poly_trans = poly[1:]
    
    '''
    Create a new tuple and add the values after multiplying by the power
    represented by the index plus one.
    '''
    poly_result = ()
    for i in range(len(poly_trans)):
        poly_result += (poly_trans[i] * (i + 1),)
        
    '''
    return the result tuple
    '''
    return poly_result

##print computeDeriv((-13.39, 0.0, 17.5, 3.0, 1.0))


def computeRoot(poly, guess, epsilon):
    res = evaluatePoly(poly, guess)
    poly_deriv = computeDeriv(poly)
    res_deriv = evaluatePoly(poly_deriv, guess)
    counter = 1
    
    while res > epsilon or res < -epsilon:
        counter += 1
        guess = guess - res/res_deriv   
        res = evaluatePoly(poly, guess)
        res_deriv = evaluatePoly(poly_deriv, guess)
        
    return guess, counter

        
print computeRoot((-13.39, 0.0, 17.5, 3.0, 1.0), 0.1, 0.0001)
    
