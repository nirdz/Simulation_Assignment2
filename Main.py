from Simulation import Simulation
from Simulation import Simulation
from GraphsPlot import drawVelocity, drawLocation
from PygameVisualization import display_events

# print("**** Sim of 1 entity and the rest attr are default ****")
# sim = Simulation(1)
# numberOfIterations= sim.simulate()
# display_events(sim.entities_pos_dict, sim.room, numberOfIterations)
# print("Time:", sim.current_k-1)
# # print("Positions:")
# # print(sim.entities_pos_dict)
# print("Desired Velocities of each entity:")
# print(sim.desired_v_list)
# # print("Velocities:")
# # print(sim.entities_v_dict)
# drawVelocity(sim.entities_v_dict)
# drawLocation(sim.entities_pos_dict)
# print()

# print("**** Sim of 1 entity and random positions and desired velocities ****")
# sim = Simulation(1, starting_pos="random", velocities_type="random")
# sim.simulate()
# print("Time:", sim.current_k-1)
# # print("Positions:")
# # print(sim.entities_pos_dict)
# print("Desired Velocities of each entity:")
# print(sim.desired_v_list)
# # print("Velocities:")
# # print(sim.entities_v_dict)
# drawVelocity(sim.entities_v_dict)
# drawLocation(sim.entities_pos_dict )
# print()


print("**** Sim of 3 entities and random positions and desired velocities ****")
sim = Simulation(200, starting_pos="random", velocities_type="same", default_desired_v=0.9)
numberOfIterations = sim.simulate()
print("Time:", numberOfIterations)
display_events(sim.entities_pos_dict, sim.room, numberOfIterations)

# print("Positions:")
# print(sim.entities_pos_dict)
# print("Desired Velocities of each entity:")
# print(sim.desired_v_list)
# print("Velocities:")
# print(sim.entities_v_dict)
# drawVelocity(sim.entities_v_dict)
# drawLocation(sim.entities_pos_dict)

# while True:
#     sim = Simulation(20, starting_pos="random", velocities_type="same", default_desired_v=1.1)
#     numberOfIterations = sim.simulate()
#     print("Time:", numberOfIterations)
#     # display_events(sim.entities_pos_dict, sim.room, numberOfIterations)
#     if numberOfIterations > 2500:
#         # print(sim.entities_pos_dict)
#         # print(sim.entities_v_dict)
#         display_events(sim.entities_pos_dict, sim.room, numberOfIterations)
