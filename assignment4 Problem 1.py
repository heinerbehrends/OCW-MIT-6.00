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
        print savingsRecords
    return savingsRecords

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord

testNestEggVariable()

def postRetirement(savings, growthRates, expenses):
    savingsRecords = []
    savingsRecords.append(savings * (1 + (0.01 * growthRates[0])) - expenses)
    for annualGrowthRate in growthRates[1:]:
        savingsRecords.append(savingsRecords[-1] * (1 + 0.01 * annualGrowthRate)-expenses)
##        print savingsRecords
    return savingsRecords
    
def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord

testPostRetirement()
