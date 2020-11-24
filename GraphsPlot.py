import matplotlib.pyplot as plt
import numpy as np

def drawVelocity(velocities_dict):
    # data = {'velocity': Velocities,
    #         'time' : [ X*0.01 for X in range(int(len(Velocities)))] ,
    #         'intervals' : [ X*2 for X in range(int(len(Velocities)/200)+1)] }

    for key, val in velocities_dict.items():
        list_to_plot = val
        time_to_plot = [x for x in range(len(list_to_plot))]
        plt.plot(time_to_plot, list_to_plot)

    plt.title('velocity VS time')
    plt.ylabel('Velocity')
    plt.xlabel('time')
    plt.show()



def drawLocation(locations_dict):
    data = {'location': locations_dict}
    # for entityIndex in range(numberOfEntities):
    #     plt.plot([x[entityIndex][0] for x in data['location']],[x[entityIndex][1] for x in data['location']])


    for key, val in locations_dict.items():
        list_x_to_plot = []
        list_y_to_plot = []
        for p in val:
            list_x_to_plot.append(p[0])
            list_y_to_plot.append(p[1])
        plt.plot(list_x_to_plot, list_y_to_plot)

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
