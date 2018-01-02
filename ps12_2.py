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
        # TODO
        
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
        # TODO
    
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
        # TODO
        if random.random() < self.maxBirthProb * (1 - popDensity):
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException

testVirus = SimpleVirus(0.5, 0.5)
print testVirus.doesClear()

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
        self.popDensity = float(len(viruses)) / maxPop
        # TODO

    def getTotalPop(self):
        """
        Gets the current total virus population. 

        returns: The total virus population (an integer)
        """
        return len(self.viruses)
        # TODO        

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
        # TODO
        self.copyOfViruses = self.viruses
        for virus in self.copyOfViruses:
            if virus.doesClear():
                self.viruses.remove(virus)
        self.popDensity = self.getTotalPop() / float(self.maxPop)
        for virus in self.viruses:
            try:
                self.viruses.append(virus.reproduce(self.popDensity))
            except NoChildException:
                continue
        
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
    # TODO
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
        # TODO
        
    def getResistance(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.        

        drug: the drug (a string).

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        # TODO
        if self.resistances[drug]:
            return True
        else:
            return False

    def getResistanceAllDrugs(self, activeDrugs):
        """
        Returns True if the virus is resistant against all drugs in the list activeDrugs, False otherwise.
        """
        self.isResistantCounter = 0
        for drug in activeDrugs:
            if self.getResistance(drug):
                self.isResistantCounter += 1
            else:
                continue
            """if virus is resistent against all drugs, add to one to counter"""
        if len(activeDrugs) == self.isResistantCounter:
             return True
        else:
            return False
        
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
        """
        print self.resistances
        if len(self.resistances) > 0:
            for drug in self.resistances:
                if self.resistances[drug]:
                    if random.random() < self.mutProb:
                        self.resistances[drug] = False
                    else: continue
                else:
                    if random.random() < 1 - self.mutProb:
                        self.resistances[drug] = True
        else:
            return False
        
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

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         

        If there are no active drugs, die or live and maybe reproduce and maybe mutate"""
        if len(activeDrugs) < 1:
            if random.random() < self.maxBirthProb * (1 - popDensity):
                child = ResistantVirus(self.maxBirthProb, self.clearProb, self.resistances, self.mutProb)
                child.mutate()
                return child
            else:
                raise NoChildException        
        else:
            for drug in activeDrugs:
                if self.resistances[drug]:
                    """
                    If 
                    """
                    if random.random() < self.maxBirthProb * (1 - popDensity):
                        
                        child = ResistantVirus(self.maxBirthProb, self.clearProb, self.resistances, self.mutProb)
                        child.mutate()
                        return child

                    else:
                        raise NoChildException
                else:
                    """
                    Live on
                    """
                    print 'virus is not resistant'
                    raise NoChildException

maxBirthProb = 0.1
clearProb = 0.05
resistances = {'guttagonol':True}
mutProb = 0.01
testVirus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
##for x in xrange(100):
####    print x
##    try:
##        print testVirus.reproduce(0.1, [])
##        print testVirus.getResistance('guttagonol')
##    except NoChildException:
##        print 'no child'
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
        # TODO
        
    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        # TODO
        if newDrug not in self.activeDrugs:
            self.activeDrugs.append(newDrug)
        else: return

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        # TODO
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
        # TODO
        
        self.resistentVirusCounter = 0
        self.copyOfViruses = self.viruses
##        self.isVirusResistant = False
        """For each virus in self.viruses"""
        for virus in self.copyOfViruses:
            if virus.getResistanceAllDrugs(drugResist):
                self.resistentVirusCounter += 1
        """return counter"""          
        return self.resistentVirusCounter

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
        """
        # TODO
        self.copyOfViruses = self.viruses
        self.newViruses = []
        for virus in self.copyOfViruses:
            if virus.doesClear():
##                print 'virus died'
                self.copyOfViruses.remove(virus)
            else:
##                print 'virus survived'
                continue

        self.viruses = self.copyOfViruses
        self.popDensity = self.getTotalPop() / float(self.maxPop)
        
        for virus in self.copyOfViruses:
            try:
                self.newViruses.append(virus.reproduce(self.popDensity, self.activeDrugs))
##                print 'reproduced'
            except NoChildException:
##                print 'no child'
                continue
        self.viruses.extend(self.newViruses)
        print 'virus population is now, ', len(self.viruses)
##viruses = []
##resistances = {'guttagonol':False}
##for i in xrange(100):
##    viruses.append(ResistantVirus(0.1, 0.05, resistances, 0.5))
##testPatient = Patient(viruses, 1000)
##for i in xrange(500):
##    testPatient.update()
##    print 'getResistPop', testPatient.getResistPop(['guttagonol'])
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
    # TODO
    viruses = []
    resistances = {'guttagonol':False}
    for i in xrange(10):
        viruses.append(ResistantVirus(0.1, 0.05, resistances, 0.005))
    maxPop = 20
    testPerson = Patient(viruses, maxPop)
    numberOfUpdates = 10
    virusPopList = []
    virusPopList.append(testPerson.getTotalPop())

    for x in xrange(numberOfUpdates):
        testPerson.update()
        print 'totalPop, resistPop:', testPerson.getTotalPop(), testPerson.getResistPop(['guttagonol'])
        virusPopList.append(testPerson.getTotalPop())

    print 'totalPop and resistantPop', testPerson.getTotalPop(), testPerson.getResistPop(['guttagonol'])
    testPerson.addPrescription('guttagonol')
    
    for x in xrange(numberOfUpdates):
        testPerson.update()
        virusPopList.append(testPerson.getTotalPop())
        
    pylab.plot(virusPopList)
    pylab.show()

problem4()
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
