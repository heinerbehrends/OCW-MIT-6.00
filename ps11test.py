# Problem Set 11: Simulating robots
# Name:
# Collaborators:
# Time:

import math
import random
import pylab
import ps11_visualize
import numpy as np
# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)


# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        # TODO: Your code goes here
        self.width = width
        self.height = height
        """
        Initialize tilesCleaned, an empty dictionary
        """
        self.tilesCleaned = {}

        
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # TODO: Your code goes here
        self.tilesCleaned[(math.floor(pos.getX()), math.floor(pos.getY()))] = True
        
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # TODO: Your code goes here
        try:
            if self.tilesCleaned[(m,n)]:
                return True        
            else:
                return False
        except KeyError:
            return False
        
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        return self.width * self.height
    
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        return len(self.tilesCleaned)

    def resetCleanedTiles(self):
        self.tilesCleaned = {}

    
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        # TODO: Your code goes here
        return Position(random.randrange(self.width), random.randrange(self.height))
        
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        # TODO: Your code goes here
        if pos.getX() <= self.width and pos.getY() <= self.height and pos.getX() > 0 and pos.getY() > 0:
            return True
        else:
            return False

        
class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # TODO: Your code goes here
        self.p = room.getRandomPosition()
        self.d = random.randrange(359)
        self.room = room
        self.speed = speed
        
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        # TODO: Your code goes here
        return self.p
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # TODO: Your code goes here
        return self.d
    
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        # TODO: Your code goes here
        self.p = position
    
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        # TODO: Your code goes here
        self.d = direction


class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # TODO: Your code goes here
        self.potentialP = self.p.getNewPosition(self.d, self.speed)     
        while not self.room.isPositionInRoom(self.potentialP):
            self.setRobotDirection(random.randrange(359))
##            print 'self.d is now ', self.d
            self.potentialP = self.p.getNewPosition(self.d, self.speed)
        self.p = self.potentialP
        self.room.cleanTileAtPosition(self.p)



def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """
    # TODO: Your code goes here
    
    simRoom = RectangularRoom(width, height)
    robots = []
    for x in xrange(num_robots):
        robots.append(robot_type(simRoom, speed))
        coverage = 0
    listOfLists = []
    
    for x in xrange(num_trials):
        trialList = []
        if visualize:
            anim = ps11_visualize.RobotVisualization(num_robots, simRoom.width, simRoom.height)
        
        simRoom.resetCleanedTiles()
        while True:
            for robot in robots:
                robot.updatePositionAndClean()
            coverage = simRoom.getNumCleanedTiles() / float(simRoom.getNumTiles())
            trialList.append(coverage)
            if visualize:
                anim.update(simRoom, robots)
            if coverage >= min_coverage:
                listOfLists.append(trialList)
                if visualize:
                    anim.done()
                break
            else: continue
    return listOfLists

def computeMean(list):
    return sum(list) / float(len(list))

# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means

# === Problem 4

def getAverageLength(list_of_lists):
    sumOfLengths = 0
    for list in list_of_lists:
        sumOfLengths += len(list)
    return float(sumOfLengths) / len(list_of_lists)
    
    
    
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    # TODO: Your code goes here
    listOfDimensions = [[5,5], [10,10], [15,15], [20,20], [25,25]]
    listOfSims = []
    listOfAverageTimes = []

    for dimensions in listOfDimensions:
        listOfSims.append(runSimulation(1, 1.0, dimensions[0], dimensions[1], 0.75, 500, Robot, False))

    for listOfLists in listOfSims:
        listOfAverageTimes.append(getAverageLength(listOfLists))

    pylab.plot(listOfAverageTimes, [25, 100 ,225, 400, 625])
    pylab.axis([0, 1000, 0, 700])
    pylab.title('Time for a single robot to clean different room sizes for 75%')
    pylab.xlabel('Time units')
    pylab.ylabel('Size of the floor')
    pylab.show()

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # TODO: Your code goes here
    listOfSims = []
    listOfAverageTimes = []
    
    for i in range(1,11):
        listOfSims.append(runSimulation(i, 1.0, 25, 25, 0.75, 500, Robot, False))
        
    for listOfLists in listOfSims:        
        listOfAverageTimes.append(getAverageLength(listOfLists))
        
    pylab.plot(range(1,11),listOfAverageTimes)
    pylab.axis([0, 10, 0, 1000])
    pylab.title('Time for 1-10 robots to clean 75% of a 25x25 room')
    pylab.xlabel('Number of robots')
    pylab.ylabel('Time units')
    pylab.show()

                            
def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    listOfDimensions = [[20,20], [25,16], [40,10], [50,8], [80,5], [100,4]]
    listOfSims = []
    listOfAverageTimes = []

    for dimensions in listOfDimensions:
        listOfSims.append(runSimulation(2, 1.0, dimensions[0], dimensions[1], 0.75, 500, Robot, False))
    
    for listOfLists in listOfSims:
        listOfAverageTimes.append(getAverageLength(listOfLists))
        
    pylab.plot([1, 1.5625, 4, 6.25, 16, 25],listOfAverageTimes)
    pylab.axis([0, 25, 250, 400])
    pylab.title('Time for 2 robots to clean 75% of different rooms with the same surface area.')
    pylab.xlabel('Ratio of the room height/width')
    pylab.ylabel('Time units')
    pylab.show()


def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    listOfSims = []
    listOfMeans = []
    
    for i in range(1, 6):
        listOfSims.append(runSimulation(i, 1.0, 25, 25, 0.75, 50, Robot, False))

    for listOfLists in listOfSims:
        listOfMeans.append(computeMeans(listOfLists))

    for means in listOfMeans:
        meansPerc = np.multiply(np.array(means), 100)
        pylab.plot(meansPerc, range(len(means)))
        
    pylab.title('Time plotted against percentage cleaned for 1-5 robots')
    pylab.xlabel('Percent of floor area cleaned')
    pylab.ylabel('Mean Time')
    pylab.show()
    
        
class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    def updatePositionAndClean(self):
            """
            Simulate the passage of a single time-step.

            Move the robot to a new position and mark the tile it is on as having
            been cleaned.
            """
            self.setRobotDirection(random.randrange(359))
            self.potentialP = self.p.getNewPosition(self.d, self.speed)     
            while not self.room.isPositionInRoom(self.potentialP):
                self.setRobotDirection(random.randrange(359))
                self.potentialP = self.p.getNewPosition(self.d, self.speed)
            self.p = self.potentialP
            self.room.cleanTileAtPosition(self.p)

class BiasedRobot(BaseRobot):
    """
    A Biased Robots continues in the same direction whenever he moved toward
    a dirty tile and randomly chooses a direction when he moved toward a clean tile
    """
    def updatePositionAndClean(self):
        
        
        self.potentialP = self.p.getNewPosition(self.d, self.speed)
        if self.room.isTileCleaned(math.floor(self.potentialP.getX()), math.floor(self.potentialP.getY())):
            self.setRobotDirection(random.randrange(359))
            
        while not self.room.isPositionInRoom(self.potentialP):
            self.setRobotDirection(random.randrange(359))
            self.potentialP = self.p.getNewPosition(self.d, self.speed)
        self.p = self.potentialP
        self.room.cleanTileAtPosition(self.p)
# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    robotsList = [RandomWalkRobot, BiasedRobot, Robot]
    listOfSims = []
    listOfMeans = []
    for robot in robotsList:
        listOfSims.append(runSimulation(1, 1.0, 25, 25, 0.75, 50, robot, False))
    for listOfLists in listOfSims:
        listOfMeans.append(computeMeans(listOfLists))

    for means in listOfMeans:
        meansPerc = np.multiply(np.array(means), 100)
        pylab.plot(meansPerc, range(len(means)))
        
    pylab.title('Time vs clean area for Robot and RandomWalkRobot')
    pylab.xlabel('Percent of floor area cleaned')
    pylab.ylabel('Mean Time')
    pylab.show() 

##avg = runSimulation(1, 1.0, 10, 10, 1.0, 500, BiasedRobot, True)
showPlot5()
