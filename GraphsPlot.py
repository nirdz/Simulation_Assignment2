import matplotlib.pyplot as plt
import numpy as np

def drawVelocity(Velocities , numberOfEntities):
    data = {'velocity': Velocities,
            'time' : [ X*0.01 for X in range(int(len(Velocities)))] ,
            'intervals' : [ X*2 for X in range(int(len(Velocities)/200)+1)] }
    for entityIndex in range(numberOfEntities):
        plt.plot(data['time'] , [x[entityIndex] for x in data['velocity']])
    plt.xticks(data['intervals'])
    plt.title('velocity VS time')
    plt.ylabel('Velocity')
    plt.xlabel('time')
    plt.show()



def drawLocation(Locations , numberOfEntities):
    data = {'location': Locations }
    for entityIndex in range(numberOfEntities):
        plt.plot([x[entityIndex][0] for x in data['location']],[x[entityIndex][1] for x in data['location']])
    plt.xticks([x for x in range(16)])
    plt.yticks([y for y in range(16)])
    axes = plt.gca()
    axes.set_xlim([0, 15.5])
    axes.set_ylim([0, 15.5])
    plt.title('entities moving in the room')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.show()

def escapeTimeBar(escapeTimes):
    numberOfTimes = [str(x+1) for x in range(len(escapeTimes))]
    plt.bar(numberOfTimes, escapeTimes)
    plt.yticks(np.arange(0, max(escapeTimes) + 1, 250))
    plt.title('Escape Times of Simulations')
    plt.ylabel('Time in k')
    plt.xlabel('Sim #')
    plt.show()
