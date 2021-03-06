from Room import Room
from Entity import Entity
from random import randrange
import random
import numpy as np
from GraphsPlot import drawVelocity, drawLocation, escapeTimeBar

def get_random_desired_v(min_v, max_v, jumps=0.05):
    # Create array of all the possible values
    random_v_arr = np.arange(min_v, max_v + jumps, jumps)
    return round(random_v_arr[randrange(0, len(random_v_arr))], 5)

def get_random_legal_pos_list(room_size):
    pos_list = []
    for i in range(int(room_size) - 1):
        for j in range(int(room_size)):
            pos_list.append( (i + 0.5, j + 0.5) )
    # Shuffle the list
    random.shuffle(pos_list)
    return pos_list

class Simulation:
    def __init__(self, entities_num, max_k=900000, room_size=15.0, doors=1, starting_pos="center", velocities_type="same", default_desired_v=0.6):
        room = Room(size=room_size, doors=doors)
        entities_list = []
        x0 = room_size / 2  # default position, middle of the room
        y0 = room_size / 2
        v0 = 0
        desired_v = default_desired_v  # default desired velocity under relaxed is 0.6
        tau = 0.5
        random_starting_pos_list = get_random_legal_pos_list(room_size)
        self.desired_v_list = []  # List for each of the entities desired velocity
        for i in range(entities_num):
            if starting_pos == "random":
                x0, y0 = random_starting_pos_list[i][0], random_starting_pos_list[i][1]

            if velocities_type == "random":
                desired_v = get_random_desired_v(0.6, 1.5, 0.05)

            entity = Entity(i, room, x0, y0, v0=v0, desired_v=desired_v, tau=tau)
            entities_list.append(entity)
            self.desired_v_list.append(desired_v)




        self.entities_list = entities_list

        # Each item represents an entity's locations list
        self.entities_pos_dict = dict(zip([str(ent.i) for ent in entities_list], [ [ent.location] for ent in entities_list]))
        # Each item represents an entity's velocities list
        self.entities_v_dict = dict(zip([str(ent.i) for ent in entities_list], [ [v0] for ent in entities_list]))



        self.entities_num = entities_num
        self.max_k = max_k
        self.current_k = 1

    def simulate(self):
        iteration = 0
        while len(self.entities_list) > 0: #while self.current_k <= self.max_k and len(self.entities_list) > 0:
            entities_to_remove = []
            for entity in self.entities_list:
                entity.move(self.entities_list)
                self.entities_pos_dict[str(entity.i)].append(entity.location)
                self.entities_v_dict[str(entity.i)].append(entity.v_k)
                if entity.is_outside:
                    entities_to_remove.append(entity)

            for ent in entities_to_remove:
                self.entities_list.remove(ent)

            self.current_k += 1
            is_v_0_for_all = True
            for ent in self.entities_list:
                if ent.v_k_minus1 > 0:
                    is_v_0_for_all = False
                    break
            if is_v_0_for_all:
                print("k:", self.current_k)
            iteration = iteration + 1
        return iteration
                # drawVelocity(self.entities_v_dict)
                # drawLocation(self.entities_pos_dict)

            # if self.current_k % 20 == 0:
            #     print("k:", self.current_k)
            #     drawLocation(self.entities_pos_dict)



    # """ Returns true if the room is empty """
    # def check_if_people_inside(self):
    #     for entity in self.entities_list:
    #         if not entity.is_reached_door():
    #             return True
    #     return False

