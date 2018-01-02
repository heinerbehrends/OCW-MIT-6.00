import random

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in Virus
    to indicate that a virus particle does not reproduce. 
    """ 

class Virus(object):
    """
    A Virus Object has a 20% chance to reproduce and its offspring has a 20% chance that
    it will mutate and change its parents boolean value.
    """
    def __init__(self, booleanDict):
        self.trueOrFalse = booleanDict

    def mutate(self):
        """
        Mutates the boolean in self.trueOrFalse.
        Called by update() in the Patient class.
        """
        if random.random() < 1:
            print 'mutate offspring'            
            if self.trueOrFalse[0]:
                self.trueOrFalse[0] = False
            else:
                self.trueOrFalse[0] = True
        
    def reproduce(self):
        """
        Returns a new virus object that might have mutated or
        raises a NoChildException. Called by update() in Patient class.
        """
        if random.random() < 0.5:            
            return Virus(dict(self.trueOrFalse))
        else:
            raise NoChildException

class Patient(object):
    def __init__(self):
        """
        Initializes virusList and adds instances of Virus object to virusList.
        """
        self.virusList = []
        for i in xrange(10):
            self.virusList.append(Virus({0: True}))

    def update(self):
        """
        Simulates reproduction and mutation of viruses
        """
        self.offspringList = []
        self.copyOfViruses = list(self.virusList)
            
        for virus in self.copyOfViruses:
            try:
                self.offspringList.append(virus.reproduce())
            except NoChildException:
                continue
        
        for z in self.virusList:
            print 'virusList before mutate', z.trueOrFalse[0]

        for virusOffspring in self.offspringList:
            virusOffspring.mutate()

        for z in self.virusList:
            print 'virusList after mutate', z.trueOrFalse[0]
            
        self.virusList += self.offspringList
        
        
testPatient = Patient()
for j in xrange(1):
    testPatient.update()
