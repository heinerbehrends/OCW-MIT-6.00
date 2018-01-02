import random

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """ 

class Virus(object):
    def __init__(self, maxBirth, dictionary, mutProb):
        self.resistances = dictionary        
        self.mutProb = mutProb
        self.maxBirth = maxBirth
        
    def mutate(self, mutProb):
        for key in self.resistances:
            if random.random() < mutProb:
                print self.resistances[key]
                print 'mutate'
                if self.resistances[key]:
                    self.resistances[key] = False
                else:
                    self.resistances[key] = True
                print self.resistances[key]
                
    def reproduce(self):
        if random.random() < self.maxBirth:
            offspring = Virus(self.maxBirth, self.resistances, self.mutProb)
            offspring.mutate(self.mutProb)
            return offspring
        else:
            raise NoChildException

    def getResistanceAllDrugs(self):
        counter = 0
        for key in self.resistances:
            if self.resistances[key]:
                counter += 1
            else:
                continue
        if len(self.resistances) == counter:
            return True
        else:
            return False
        
class Patient(object):
    def __init__(self, virusList):
        self.virusList = virusList

    def update(self):
        
        self.copyList = self.virusList
        self.offspringList = []
        for virus in self.virusList:
                print 'virusList before mutate', virus.getResistanceAllDrugs()
        for virus in self.copyList:
            try:
                offspring = virus.reproduce()
                self.offspringList.append(offspring)
            except NoChildException:
                continue
            
        for virus in self.virusList:
            print 'virusList before merge', virus.getResistanceAllDrugs()
            
        print 'Number of children', len(self.offspringList)
        
        self.counter = 0
        for virus in self.offspringList:
            if virus.getResistanceAllDrugs():
                self.counter += 1
                
        print 'Resistant children', self.counter
        for virus in self.offspringList:
            print 'offspringList before merge', virus.getResistanceAllDrugs()
        
        self.virusList += self.offspringList
        
        for virus in self.virusList:
            print 'merged virusList, offspringList', virus.getResistanceAllDrugs()
            
    def getVirusList(self):
        return self.virusList

    def getTotalPop(self):
        return len(virusList)

    
            
    def getResistPop(self):
        counter = 0
        for virus in self.virusList:
            if virus.getResistanceAllDrugs():
                counter += 1
        return counter
    
virusList = []
for i in xrange(10):
    virusList.append(Virus(0.5, {0:False}, 0.2))
testPatient = Patient(virusList)
for j in xrange(2):
    testPatient.update()
    print 'totalPop, ResistPop', testPatient.getTotalPop(), testPatient.getResistPop()
            





