from Simulation import Simulation
from GraphsPlot import drawVelocity, drawLocation, escapeTimeBar
from PygameVisualization import display_events
import numpy as np
""" a """
print("*** a ***")
entities_numbers = [20, 50, 100, 200]
# n Ents with 1.5 desired velocity and random starting positions:
for n in entities_numbers:
    sim1 = Simulation(n, starting_pos="random", velocities_type="same", default_desired_v=1.5)
    numberOfIterations = sim1.simulate()
    print("Escape iterations for", n,  "Ents:", numberOfIterations)
    # drawVelocity(sim1.entities_v_dict)
    # drawLocation(sim1.entities_pos_dict)
    # Animate the simulation
    # if n == 200:
    #     display_events(sim1.entities_pos_dict, sim1.room, numberOfIterations)

""" b """
print()
print("*** b ***")
desired_v_values = np.arange(0.6, 1.6, 0.1)
# n Ents with v desired velocity and random starting positions:
for n in entities_numbers:
    for v in desired_v_values:
        des_v = round(v, 1)
        sim1 = Simulation(n, starting_pos="random", velocities_type="same", default_desired_v=des_v)
        numberOfIterations = sim1.simulate()
        print("Escape iterations for", n,  "Ents and", des_v, "desired velocity:", numberOfIterations, )
        # drawVelocity(sim1.entities_v_dict)
        # drawLocation(sim1.entities_pos_dict)
        # Animate the simulation
        # if n == 200:
        #     display_events(sim1.entities_pos_dict, sim1.room, numberOfIterations)

""" c """
print()
print("*** c ***")
entities_numbers = [20, 50, 100, 125, 150, 175, 200]
# n Ents with v desired velocity, random starting positions,
# and 20% of the Ents are old people and have 1/3 of the desired velocity:
for n in entities_numbers:
    for v in desired_v_values:
        des_v = round(v, 1)
        sim1 = Simulation(n, starting_pos="random", velocities_type="same but part old", default_desired_v=des_v)
        numberOfIterations = sim1.simulate()
        print("Escape iterations for", n,  "Ents and", des_v, "desired velocity", numberOfIterations, "and 20% are old people:")
        # drawVelocity(sim1.entities_v_dict)
        # drawLocation(sim1.entities_pos_dict)
        # Animate the simulation
        # if n == 200:
        #     display_events(sim1.entities_pos_dict, sim1.room, numberOfIterations)