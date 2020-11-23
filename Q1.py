from Simulation import Simulation
from GraphsPlot import drawVelocity, drawLocation
import copy

print(sum(list(range(200,1,-1))))
""" a """
print("**** Sim of 1 entity and the rest attr are default ****")
sim1 = Simulation(1)
sim1.simulate()
print("Positions:")
print(len(sim1.entities_pos_at_k))
print(sim1.entities_pos_at_k)
print("Desired Velocities of each entity:")
print(sim1.desired_v_list)
print("Velocities:")
print(len(sim1.entities_v_at_k))
print(sim1.entities_v_at_k)
# Displaying the graphs
drawVelocity(sim1.entities_v_at_k, sim1.entities_num)
drawLocation(sim1.entities_pos_at_k, sim1.entities_num)

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
# TODO: Display here the time graph of each sim

""" c """
closeness_per_k = [0 for i in range(max_time + 1)]  # How many times the entities were dangerously close in each k
for k in range(len(closeness_per_k)):
    points_at_curr_k = []
    for pos_list in entities_pos_at_k_for_each_sim:
        if k < len(pos_list):
            points_at_curr_k.append(pos_list[k][0])  # [0] because there is only 1 point (1 entity)
    # Now we have a list of positions at k,
    # check for each position whether it is close to the other points
    for i in range(len(points_at_curr_k)):  # Should be 0 -> 199
        for j in range(i + 1, (len(points_at_curr_k))):
            point_i = points_at_curr_k[i]
            point_j = points_at_curr_k[j]
            if abs(point_j[0] - point_i[0]) < 0.5 or abs(point_j[1] - point_i[1]) < 0.5:
                closeness_per_k[k] += 1

print(closeness_per_k)
in_how_many_ks_was_closeness = 0
in_how_many_ks_was_not_closeness = 0
for val in closeness_per_k:
    if val > 0:
        in_how_many_ks_was_closeness += 1
    else:
        in_how_many_ks_was_not_closeness += 1
print("In", in_how_many_ks_was_closeness, "ks there was closeness between at least 1 pair of entities")
print("In", in_how_many_ks_was_not_closeness, "ks there were no interferences")
print("The k with the most collisions was", closeness_per_k.index(max(closeness_per_k)), ", with", max(closeness_per_k), "collisions")
print("The average number of collisions is", sum(closeness_per_k)/len(closeness_per_k))