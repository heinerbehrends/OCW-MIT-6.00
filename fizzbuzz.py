#1-100 /3=fizz /5=buzz /3&/5=fizzbuzz
##for i in range(1,101):
##    if i % 3 == 0 and i % 5 == 0:
##        print 'fizzbuzz'
##    elif i % 3 == 0:
##        print 'fizz'
##    elif i % 5 == 0:
##        print 'buzz'
##    else: print i

for i in range(1,101):
    ans = ''
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0:
            ans += 'Fizz'
        if i % 5 == 0:
            ans += 'Buzz'
        print ans
    else:
        print i
