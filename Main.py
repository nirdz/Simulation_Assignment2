from Simulation import Simulation
from Simulation import Simulation
from GraphsPlot import drawVelocity, drawLocation

print("**** Sim of 1 entity and the rest attr are default ****")
sim = Simulation(1)
sim.simulate()
print("Time:", sim.current_k-1)
# print("Positions:")
# print(sim.entities_pos_dict)
print("Desired Velocities of each entity:")
print(sim.desired_v_list)
# print("Velocities:")
# print(sim.entities_v_dict)
drawVelocity(sim.entities_v_dict)
drawLocation(sim.entities_pos_dict)
print()

print("**** Sim of 1 entity and random positions and desired velocities ****")
sim = Simulation(1, starting_pos="random", velocities_type="random")
sim.simulate()
print("Time:", sim.current_k-1)
# print("Positions:")
# print(sim.entities_pos_dict)
print("Desired Velocities of each entity:")
print(sim.desired_v_list)
# print("Velocities:")
# print(sim.entities_v_dict)
drawVelocity(sim.entities_v_dict)
drawLocation(sim.entities_pos_dict )
print()

print("**** Sim of 3 entities and random positions and desired velocities ****")
sim = Simulation(3, starting_pos="random", velocities_type="random")
sim.simulate()
print("Time:", sim.current_k-1)
# print("Positions:")
# print(sim.entities_pos_dict)
print("Desired Velocities of each entity:")
print(sim.desired_v_list)
# print("Velocities:")
# print(sim.entities_v_dict)
drawVelocity(sim.entities_v_dict)
drawLocation(sim.entities_pos_dict)
