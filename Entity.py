import math
import random

class Entity:
    def __init__(self, i, room, x0, y0, body_radius=0.3, space_radius=0.5, v0=0, desired_v=0.6, tau=0.5):
        self.i = i
        self.room = room  # Room object
        self.x = x0  # starting x location
        self.y = y0  # starting y location
        self.space_radius = space_radius  # For collision with other people
        self.body_radius = body_radius  # For not colliding with the door's walls

        # Determine the goal point of the entity
        self.goal_x = -1
        self.goal_y = -1
        self.set_goal_point()

        self.desired_v = desired_v
        self.a = desired_v / tau
        self.v_k_minus1 = v0
        self.v_k = v0 + self.a * 0.01

        """ Alpha is the angle between the starting position and the door """
        tan_alpha = (self.goal_y - y0) / (self.goal_x - x0)
        self.alpha = math.degrees(math.atan(tan_alpha))  # alpha in degrees
        self.is_outside = False
        # print(tan_alpha)
        # print(self.alpha)

    @property
    def location(self):
        return self.x, self.y

    def set_goal_point(self):
        room = self.room
        body_r = self.body_radius
        if room.door_top_y - body_r <= self.y <= room.size:
            self.goal_x = room.door_top_x
            self.goal_y = room.door_top_y - body_r
        elif 0 <= self.y <= room.door_bottom_y + body_r:
            self.goal_x = room.door_bottom_x
            self.goal_y = room.door_bottom_y + body_r
        else:
            self.goal_x = room.door_top_x
            self.goal_y = self.y

    """ Move a step, returns the new entity's position (x, y) """
    def move(self, entities_in_room):
        if self.is_outside:
            return self.x, self.y

        # The distance we moved in time k
        d = ((self.v_k + self.v_k_minus1) / 2.0) * 0.01

        # The distance in axis x
        b = d * math.cos(math.radians(self.alpha))

        # The distance in axis y
        a_line = d * math.sin(math.radians(self.alpha))

        x1 = self.x + b
        y1 = self.y + a_line
        x1 = round(x1, 6)
        y1 = round(y1, 6)

        # Check collision with walls and other entities
        num_of_collisions = get_how_many_collisions_at_pos(self, self.i, x1, y1, entities_in_room)
        if num_of_collisions == 0:  # make the step
            # Update the current entity's position
            self.x = x1
            self.y = y1

            # Update the velocity
            new_v = min(self.desired_v, self.v_k + self.a * 0.01)
            self.v_k_minus1 = self.v_k
            self.v_k = round(new_v, 5)
            self.is_reached_door()
            return x1, y1
        elif num_of_collisions > 1:
            # Stand still and do not make the move
            self.v_k_minus1 = 0
            self.v_k = 0 + self.a * 0.01
            return self.x, self.y
        else:  # Only one potential collision
            # Try to Increase the angle by "random_alpha_inc" and try to make the move
            random_alpha_inc = random.randrange(-180, 181)
            is_safe, new_x1, new_y1 = is_angle_safe(self, self.i, self.x, self.y, self.alpha, random_alpha_inc, self.v_k, self.v_k_minus1,
                                                    entities_in_room, self.room.size)
            if is_safe:
                # Do this step and update the new angle to the goal target

                # Update the current entity's position
                self.x = new_x1
                self.y = new_y1

                # Update to the new angle
                self.set_goal_point()
                tan_alpha = (self.goal_y - new_y1) / (self.goal_x - new_x1)
                self.alpha = math.degrees(math.atan(tan_alpha))  # alpha in degrees

                # Update the velocity
                new_v = min(self.desired_v, self.v_k + self.a * 0.01)
                self.v_k_minus1 = self.v_k
                self.v_k = round(new_v, 5)
                self.is_reached_door()
                return self.x, self.y

            else:  # Try angle "-random_alpha_inc"
                is_safe, new_x1, new_y1 = is_angle_safe(self,self.i, self.x, self.y, self.alpha, -1*random_alpha_inc,
                                                        self.v_k, self.v_k_minus1, entities_in_room, self.room.size)
                if is_safe:
                    # Do this step and update the new angle to the goal target

                    # Update the current entity's position
                    self.x = new_x1
                    self.y = new_y1


                    self.set_goal_point()
                    # Update to the angle to the new goal
                    tan_alpha = (self.goal_y - new_y1) / (self.goal_x - new_x1)
                    self.alpha = math.degrees(math.atan(tan_alpha))  # alpha in degrees

                    # Update the velocity
                    new_v = min(self.desired_v, self.v_k + self.a * 0.01)
                    self.v_k_minus1 = self.v_k
                    self.v_k = round(new_v, 5)
                    self.is_reached_door()
                    return self.x, self.y
                else:  # There are still collisions
                    # Stand still and do not make the move
                    self.v_k_minus1 = 0
                    self.v_k = 0 + self.a * 0.01
                    return self.x, self.y




    def is_reached_door(self):
        room = self.room
        if not self.is_outside and self.x >= room.door_top_x and room.door_bottom_y <= self.y <= room.door_top_y:
            self.is_outside = True
        return self.is_outside


""" Returns how many collisions are around a point (x,  y), 
    returns 2 if there is more than 1 collision. """
def get_how_many_collisions_at_pos(self, i, x, y, entities_in_room):
    count = 0
    if closestEntityToDoor(self,entities_in_room):
        return 0
    for entity in entities_in_room:
        # Check if the entity is not me and the it is inside the room
        if i != entity.i and not entity.is_outside:
            other_ent_x = entity.x
            other_ent_y = entity.y
            # Check the dist between us
            if math.sqrt( ((x-other_ent_x)**2)+((y-other_ent_y)**2) ) < 0.5:
                count += 1
                if count > 1:
                    return count
    return count

def closestEntityToDoor(self,entities_in_room):

    distanceToDoor = math.sqrt( ((self.x-self.goal_x)**2)+((self.y-self.goal_y)**2) )
    for entity in entities_in_room:
        # Check if the entity is not me and the it is inside the room
        if self.i != entity.i and not entity.is_outside:
            other_ent_x = entity.x
            other_ent_y = entity.y
            # Check the dist between us
            distanceEntityToDoor = math.sqrt(((other_ent_x - entity.goal_x) ** 2) + ((other_ent_y - entity.goal_y) ** 2))
            if distanceToDoor > distanceEntityToDoor:
                return False
    return True



""" Returns False if the next step with the new angle will make the entity 
    hit the wall or there would be more collisions """
def is_angle_safe(self, i, curr_x, curr_y, curr_alpha, alpha_inc, curr_vk, curr_vk_minus1, entities_in_room, room_size):
    new_alpha = curr_alpha + alpha_inc
    new_d = ((curr_vk + curr_vk_minus1) / 2.0) * 0.01
    new_b = new_d * math.cos(math.radians(new_alpha))
    new_a = new_d * math.sin(math.radians(new_alpha))

    new_x1 = curr_x + new_b
    new_y1 = curr_y + new_a
    new_x1 = round(new_x1, 6)
    new_y1 = round(new_y1, 6)
    # If we are out of boundaries:
    if new_x1 < 0.6 or new_x1 > room_size - 0.6 or new_y1 < 0.6 or new_y1 > room_size - 0.6:
        return False, -1, -1

    new_num_of_collisions = get_how_many_collisions_at_pos(self, i, new_x1, new_y1, entities_in_room)
    if new_num_of_collisions == 0:
        return True, new_x1, new_y1
    return False, -1, -1