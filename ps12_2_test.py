import ps12_2

maxBirthProb = 0.1
clearProb = 0.05
resistances = {'guttagonol':True}
mutProb = 0.5
testVirus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
for x in xrange(100):
####    print x
    try:
        print testVirus.reproduce(0.1, [])
        print testVirus.getResistance('guttagonol')
    except NoChildException:
        print 'no child'
        continue
