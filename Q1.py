from Simulation import Simulation
from GraphsPlot import drawVelocity, drawLocation
import copy

""" a """
print("**** Sim of 1 entity and the rest attr are default ****")
sim = Simulation(1)
sim.simulate()
print("Positions:")
print(len(sim.entities_pos_at_k))
print(sim.entities_pos_at_k)
print("Desired Velocities of each entity:")
print(sim.desired_v_list)
print("Velocities:")
print(len(sim.entities_v_at_k))
print(sim.entities_v_at_k)
# Displaying the graphs
drawVelocity(sim.entities_v_at_k, sim.entities_num)
drawLocation(sim.entities_pos_at_k, sim.entities_num)

""" b """
print("**** 200 Sims of 1 entity and random positions and default velocity ****")
sims = []
time_to_complete_list = []  # Total k it took for each sim to complete
entities_pos_at_k_for_each_sim = []
for i in range(200):
    sim = Simulation(1, starting_pos="random")
    sim.simulate()
    sims.append(sim)
    print(i, ": Num of steps: ", sim.current_k-1)
    time_to_complete_list.append(sim.current_k-1)
    entities_pos_at_k_for_each_sim.append(sim.entities_pos_at_k)
    # drawVelocity(sim.entities_v_at_k, sim.entities_num)
    # drawLocation(sim.entities_pos_at_k, sim.entities_num)
    print()

print("Avg time to complete: ", sum(time_to_complete_list)/len(time_to_complete_list))
max_time = max(time_to_complete_list)
print("Max time to complete: ", max_time)

# """ Section that not needed in report """
# min_time = min(time_to_complete_list)
# index_of_min_time = time_to_complete_list.index(min_time)
# # Graphs of the min time (not needed in the report)
# drawVelocity(sims[index_of_min_time].entities_v_at_k, sims[index_of_min_time].entities_num)
# drawLocation(sims[index_of_min_time].entities_pos_at_k, sims[index_of_min_time].entities_num)
#
# index_of_max_time = time_to_complete_list.index(max_time)
# # Graphs of the max time (not needed in the report)
# drawVelocity(sims[index_of_max_time].entities_v_at_k, sims[index_of_max_time].entities_num)
# drawLocation(sims[index_of_max_time].entities_pos_at_k, sims[index_of_max_time].entities_num)
# """ End of section"""

# Sorting the time list
sorted_time_to_complete_list = copy.deepcopy(time_to_complete_list)
sorted_time_to_complete_list.sort()
print()
