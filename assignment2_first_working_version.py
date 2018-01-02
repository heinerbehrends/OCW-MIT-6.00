from math import sqrt
import time
start_time = time.time()

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
            primeCandidate += 2
            break
print primeNumbers[-1]
print "My program took", time.time() - start_time, "to run"
