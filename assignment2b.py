from math import sqrt
from math import log
import time
start_time = time.time()

primeCandidate = 3
primeNumbers =(2,)
primeCounter = 1
n = int(raw_input(["Calculate primes up to this number"]))

while primeCandidate < n:
    for prime in primeNumbers:
        if prime > sqrt(primeCandidate) and primeCandidate % prime != 0:
##            print primeCandidate
            primeNumbers += (primeCandidate,)
            primeCounter += 1
            primeCandidate += 2         
            break
        if primeCandidate % prime == 0:
            primeCandidate += 2
            break
for prime in primeNumbers:
    sumOfLog = float(0.0)
    sumOfLog += float(log(prime))
    print float(sumOfLog)
print sumOfLog
print log(n)
print sumOfLog/log(n)
##print primeNumbers
print "My program took", time.time() - start_time, "to run"
