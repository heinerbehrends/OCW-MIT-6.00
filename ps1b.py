initial_balance = 999999  #float(raw_input('Enter the balance in dollars.cent\n'))
annual_interest = 0.18 #float(raw_input('Enter the annual interest rate in decimal\n'))
##min_monthly_payment = float(raw_input('Enter the minimum monthly payment in decimal\n'))
monthly_interest = annual_interest/12.0
##print monthly_interest


def getMinMonthlyPayment(balance):
    return min_monthly_payment * balance

def getInterestPaid(balance):
    return annual_interest / 12 * balance

def getPrincipalPaid(balance):
    return getMinMonthlyPayment(balance) - getInterestPaid(balance)

def printYear(balance):
    remaining_balance = balance
    total_amount_paid = 0
    for i in range(1, 13):
        min_monthly_payment = getMinMonthlyPayment(remaining_balance)
        total_amount_paid += min_monthly_payment
        principal_paid = getPrincipalPaid(remaining_balance)
        remaining_balance -= getPrincipalPaid(remaining_balance)
        print 'Months: %i \nMinimum monthly payment: %.2f \nPrinciple paid: %.2f \nRemaining balance: %.2f' \
                    %(i, min_monthly_payment, principal_paid, remaining_balance)
    print 'RESULT \nTOTAL AMOUNT PAID: %.2f \nREMAINING BALANCE: %.2f' \
                      %(total_amount_paid, remaining_balance)

##printYear(initial_balance)

def payingOffDebtInAYear():
    remaining_balance = initial_balance    
    monthly_payment = 10
    for monthly_payment in range(10, int(initial_balance / 2),10):
        for i in range(1,13):
            remaining_balance = remaining_balance * (1 + monthly_interest) - monthly_payment
            if remaining_balance < 0:
                print "It took %i month and a monthly payment of %i dollars to pay the debt in one year. \nThe new balance is %.2f" \
                      %(i, monthly_payment, remaining_balance)
                return
##        print 'Balance after one year', remaining_balance
        monthly_payment += 10
        remaining_balance = initial_balance
##            print 'Remaining balance is', remaining_balance
        

def isCloseToZero(remaining_balance):
    if remaining_balance <= 0.11 and remaining_balance >= -0.11:
        return True
    else:
        return False

def payingOffDebtBisection():
    remaining_balance = initial_balance
    lower_bound = initial_balance / 12
    print 'lower_bound is', lower_bound
    upper_bound = (initial_balance * (1 + (annual_interest / 12)) ** 12) / 12
    monthly_payment = (lower_bound + upper_bound) / 2
    print isCloseToZero(remaining_balance)
    while not isCloseToZero(remaining_balance):
        remaining_balance = initial_balance
        print 'Balance is ', remaining_balance
        for i in range(1,13):
            remaining_balance = remaining_balance * (1 + monthly_interest) - monthly_payment
        if remaining_balance > 0:
            print'Too low'
            lower_bound = monthly_payment
            print 'lower_bound is now', upper_bound
            monthly_payment = (lower_bound + upper_bound) / 2
        elif remaining_balance < 0:
            print 'Too high'
            upper_bound = monthly_payment
            print 'upper_bound is now', lower_bound
            monthly_payment = (lower_bound + upper_bound) / 2
    print 'RESULT \nMonthly payment to pay off debt in one year is %.2f \nNumber of month needed: %i \nBalance: %.2f' %(monthly_payment, i, remaining_balance)

payingOffDebtBisection()      
print isCloseToZero(0.1)                
