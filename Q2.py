from Simulation import Simulation
from GraphsPlot import drawVelocity, drawLocation, escapeTimeBar
from PygameVisualization import display_events
import math
""" a """
# 20 Ents with 1.5 desired velocity and random starting positions:
sim1 = Simulation(70, starting_pos="random", velocities_type="same", default_desired_v=1.5)
numberOfIterations = sim1.simulate()
print("escape iterations: " + str(numberOfIterations))
drawLocation(sim1.entities_pos_dict)
# Animate the simulation
display_events(sim1.entities_pos_dict, sim1.room, numberOfIterations)
# drawVelocity(sim1.entities_v_dict)
