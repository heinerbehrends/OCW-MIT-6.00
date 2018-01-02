from math import sqrt

primeCandidate = 3
primeNumbers =(2,)
primeCounter = 1

while primeCounter < 1000:
    for prime in primeNumbers:
            if primeCandidate % prime == 0:
                primeCandidate += 2
                break
            if prime == primeNumbers[-1] and primeCandidate % prime != 0:
                primeNumbers += (primeCandidate,)
                primeCounter += 1
print primeNumbers[-1]
print sqrt(11)
