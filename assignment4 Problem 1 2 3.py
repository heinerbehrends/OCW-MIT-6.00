# -*- coding: cp1252 -*-


def oneYear(salary, save):
    endOfYear = 0
    endOfYear = salary*save*0.01
    return endOfYear

##print oneYear(1000,10)

def nestEggFixed(salary, save, growthRate, years):
    savingsRecords = []
    savingsRecords.append(oneYear(salary, save))
    print savingsRecords
    for year in range(years):
        savingsRecords.append(savingsRecords[-1]*(1 + growthRate*0.01) + oneYear(salary, save))
##        print savingsRecords
    return savingsRecords

##nestEggFixed(1000, 10, 10, 10)
    
def nestEggVariable(salary, save, growthRates):
    savingsRecords = []
    savingsRecords.append(oneYear(salary, save))
    for annualGrowthRate in growthRates[1:]:
        savingsRecords.append(savingsRecords[-1] * (1 + annualGrowthRate*0.01) + oneYear(salary, save))
##        print savingsRecords
    return savingsRecords

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord

##testNestEggVariable()

def postRetirement(savings, growthRates, expenses):
    savingsRecords = []
    savingsRecords.append(savings * (1 + (0.01 * growthRates[0])) - expenses)
    for annualGrowthRate in growthRates[1:]:
        savingsRecords.append(savingsRecords[-1] * (1 + 0.01 * annualGrowthRate)-expenses)
##        print savingsRecords
    return savingsRecords
    
def testPostRetirement():
    savings     = 5266.26
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 1230  
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord

##testPostRetirement()


def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates, epsilon):
    low = 0
    high = nestEggVariable(salary, save, preRetireGrowthRates)[-1]
    savings = nestEggVariable(salary, save, preRetireGrowthRates)[-1]
    print high
    guess = (low + high)/2.0
    counter = 1
    print guess
    print postRetirement(savings, postRetireGrowthRates, guess)[-1]
    while postRetirement(savings, postRetireGrowthRates, guess)[-1] < 0 - epsilon or postRetirement(savings, postRetireGrowthRates, guess)[-1] > 0 + epsilon:
        if postRetirement(savings, postRetireGrowthRates, guess)[-1] < 0:
            print 'guess', guess
            print 'formula', postRetirement(savings, postRetireGrowthRates, guess)[-1]
            high = guess
            guess = (low + high)/2.0
        else:
            print 'formula else', postRetirement(savings, postRetireGrowthRates, guess)[-1]
            low = guess
            guess = (low + high)/2.0
            print 'low', low
        counter += 1
    return guess

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    
testFindMaxExpenses()
