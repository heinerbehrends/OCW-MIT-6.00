# 6.00 Problem Set 12
#
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """    

#
# PROBLEM 1
#

class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        
    def doesClear(self):
        """
        Stochastically determines whether this virus is cleared from the
        patient's body at a time step. 

        returns: Using a random number generator (random.random()), this method
        returns True with probability self.clearProb and otherwise returns
        False.
        """
        if random.random() < self.clearProb:
            return True
        else:
            return False
    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        if random.random() < self.maxBirthProb * (1 - popDensity):
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException

class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getTotalPop(self):
        """
        Gets the current total virus population. 

        returns: The total virus population (an integer)
        """
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
          of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update() 

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: the total virus population at the end of the update (an
        integer)
        """

        self.copyOfViruses = self.viruses

        for virus in self.copyOfViruses:
            if virus.doesClear():
                self.viruses.remove(virus)

        self.popDensity = self.getTotalPop() / float(self.maxPop)

        self.newBornViruses = []
        for virus in self.viruses:
            try:
                self.newBornViruses.append(virus.reproduce(self.popDensity))
            except NoChildException:
                continue
        self.viruses.extend(self.newBornViruses)
                

##maxBirthProb = 0.1
##maxClearProb = 0.1
##
##testVirus = SimpleVirus(maxBirthProb, maxClearProb)
##viruses = []
##for i in xrange(10):
##    viruses.append(SimpleVirus(maxBirthProb, maxClearProb))
##maxPop = 100
##
##testPatient = SimplePatient(viruses, maxPop)
##
##for x in xrange(10):
##    testPatient.update()
##    print testPatient.getTotalPop()
#
# PROBLEM 2
#

def problem2():
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    

    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """
    viruses = []
    for i in xrange(100):
        viruses.append(SimpleVirus(0.1, 0.05))
    maxPop = 1000
    testPerson = SimplePatient(viruses, maxPop)
    numberOfUpdates = 200
    virusPopList = []
    virusPopList.append(testPerson.getTotalPop())

    for x in xrange(numberOfUpdates):
        testPerson.update()
        virusPopList.append(testPerson.getTotalPop())

    pylab.plot(virusPopList)
    pylab.show()

##problem2()
    
#
# PROBLEM 3
#

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """    
    
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        
        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb
        
    def getResistance(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.        

        drug: the drug (a string).

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        if self.resistances[drug]:
            return True
        else:
            return False

    def getResistanceAllDrugs(self, activeDrugs):
        """
        Check resistance against all Drugs in activeDrugs and count them.
        """
        if activeDrugs:
            self.isResistantCounter = 0
            for drug in activeDrugs:
                if self.getResistance(drug):
                    self.isResistantCounter += 1
                else:
                    continue
                """Check the counter against the length of the list"""
            if len(activeDrugs) == self.isResistantCounter:
                 return True
            else:
                return False
        else:
            return True

    def mutate(self):
        """
        Is called by reproduce().
        stochastically determines whether or not the virus will inherent its parents reisitance
        or mutate to be resistant against drugs.
        
        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        Checks if the virus has any resistances. If so it mutates the resistances
        with probability mutProb.
        """
        if self.resistances:
            for drug in self.resistances:
                if random.random() < self.mutProb:
##                    print 'mutate mutate mutate mutate mutate mutate'
                    if self.resistances[drug]:
                        self.resistances[drug] = False
                    else:
                        self.resistances[drug] = True

                        
    def createMutOffspring(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step and mutates the offspring. Called by the reproduce() method in the ResistentVirus class.
        """
        if random.random() < self.maxBirthProb * (1 - popDensity):
            self.offspring = ResistantVirus(self.maxBirthProb, self.clearProb, self.resistances.copy(), self.mutProb)
            self.offspring.mutate()
            return self.offspring
        else:
            raise NoChildException
                        
        
    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        # TODO
        """if there are no drugs in activeDrugs or if the virus is resistant to all drugs,
        reproduce with createOffspring, otherwise check if virus is resistant to all drugs"""
        
        if not activeDrugs:
            return self.createMutOffspring(popDensity)
        else:
            if self.getResistanceAllDrugs(activeDrugs):
                return self.createMutOffspring(popDensity)
            else:
                raise NoChildException


##for k in xrange(100):
##    testResistantVirus.mutate()
##    print 'guttagonol', testResistantVirus.getResistance('guttagonol')
##    print 'grimpex', testResistantVirus.getResistance('grimpex')


##for j in xrange(1000):
##    try:
##        print testResistantVirus.reproduce(popDensity, activeDrugs).getResistance('guttagonol')
##        print testResistantVirus.reproduce(popDensity, activeDrugs).getResistance('grimpex')
##    except NoChildException:
##        continue

    
class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop
        self.activeDrugs = []
        
    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        if newDrug not in self.activeDrugs:
            self.activeDrugs.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.activeDrugs

        
    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        """For each virus in self.viruses"""
        self.resistantVirusCounter = 0
        for virus in self.viruses:
            if virus.getResistanceAllDrugs(drugResist):
                self.resistantVirusCounter += 1
        """return counter"""          
        return self.resistantVirusCounter

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly
          
        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)

        Iterates over a copy of viruses and removes them from the original
        list when doesClear() returns True.
        """
        self.virusesBeforeClear = len(self.viruses)
        self.copyOfViruses = list(self.viruses)
        
        for virus in self.copyOfViruses:
            if virus.doesClear():
                self.viruses.remove(virus)
                
        self.virusesAfterClear = len(self.viruses)
##        print 'deceased', self.virusesBeforeClear - self.virusesAfterClear
        
        self.popDensity = self.getTotalPop() / float(self.maxPop)
        
        self.offspring = []
        self.copyTwoOfViruses = self.viruses

        for virus in self.copyTwoOfViruses:
            try:
                self.offspring.append(virus.reproduce(self.popDensity, self.activeDrugs))
            except NoChildException:
                continue
##        print 'number of children', len(self.offspring)
        self.viruses.extend(self.offspring)


##maxBirthProb = 0.3
##clearProb = 0.1
##mutProb = 0.1
##resistances = {'guttagonol': False}
##activeDrugs = ['guttagonol']
##popDensity = 0.0
##testResistantVirus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
##
##
##viruses = []
##maxPop = 1000
####for v in xrange(100):
####    viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
##for h in xrange(1):
##    viruses.append(ResistantVirus(maxBirthProb, clearProb, {'guttagonol': False}, mutProb))
##for j in xrange(8):
##    viruses.append(ResistantVirus(maxBirthProb, clearProb, {'guttagonol': True}, mutProb))
####viruses.append(ResistantVirus(maxBirthProb, clearProb, {'guttagonol': False}, mutProb))
##
##
##
##testPatient = Patient(viruses, maxPop)
##
####for m in xrange(50):
####    testPatient.update()
##print testPatient.getResistPop(activeDrugs)
##print testPatient.getTotalPop()

#
# PROBLEM 4
#

def problem4():
    """
    Runs simulations and plots graphs for problem 4.

    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.

    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    
    viruses = []
    var_resistances = {'guttagonol':False}
    for i in xrange(100):
        viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False}, 0.005))
    maxPop = 1000
    testPerson = Patient(viruses, maxPop)
    
    numberOfUpdates = 150
    
    resistVirusPopList = []
    virusPopList = []
    virusPopList.append(testPerson.getTotalPop())
    resistVirusPopList.append(testPerson.getResistPop(['guttagonol']))

    for x in xrange(numberOfUpdates):
        testPerson.update()
##        print 'totalPop, resistPop:', testPerson.getTotalPop(), testPerson.getResistPop(['guttagonol'])
        virusPopList.append(testPerson.getTotalPop())
        resistVirusPopList.append(testPerson.getResistPop(['guttagonol']))

    testPerson.addPrescription('guttagonol')
    
    for x in xrange(numberOfUpdates):
        testPerson.update()
##        print 'totalPop, resistPop:', testPerson.getTotalPop(), testPerson.getResistPop(['guttagonol'])
        virusPopList.append(testPerson.getTotalPop())
        resistVirusPopList.append(testPerson.getResistPop(['guttagonol']))

    pylab.plot(virusPopList)
    pylab.plot(resistVirusPopList)
    pylab.show()

##problem4()

#
# PROBLEM 5
#
        
def problem5():
    """
    Runs simulations and make histograms for problem 5.

    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    # TODO
    viruses = []
    for i in xrange(100):
        viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005))
    maxPop = 1000
    testPerson = Patient(list(viruses), maxPop)
    
    numberOfUpdates = 150
    numberOfUpdatesMod = [300,150,75,0]
    
    virusPopList = []

    for j in xrange(500):
        testPerson = Patient(list(viruses), maxPop)
        for x in xrange(150):
            testPerson.update()

        testPerson.addPrescription('guttagonol')

        for x in xrange(150):
            testPerson.update()
            
        virusPopList.append(testPerson.getTotalPop())
        print testPerson.getTotalPop()

    pylab.hist(virusPopList)
    pylab.show()

problem5()
#
# PROBLEM 6
#

def problem6():
    """
    Runs simulations and make histograms for problem 6.

    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
    
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    # TODO
    viruses = []
    for i in xrange(100):
        viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005))
    maxPop = 1000
    testPerson = Patient(list(viruses), maxPop)
    
    numberOfUpdates = 150
    numberOfUpdatesMod = [300,150,75,0]
    
    virusPopList = []

    for j in xrange(500):
        testPerson = Patient(list(viruses), maxPop)
        for x in xrange(150):
            testPerson.update()

        testPerson.addPrescription('guttagonol')
        
        for x in xrange(300):
            testPerson.update()

        testPerson.addPrescription('grimpex')

        for x in xrange(150):
            testPerson.update()
            
        virusPopList.append(testPerson.getTotalPop())
        print testPerson.getTotalPop()

    pylab.hist(virusPopList)
    pylab.show()

#
# PROBLEM 7
#
     
def problem7():
    """
    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.

    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        
    """
    # TODO
