import math

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
        if self.is_reached_door():
            return self.x, self.y

        # The distance we moved in time k
        d = ((self.v_k + self.v_k_minus1) / 2.0) * 0.01

        # The distance in axis x
        b = d * math.cos(math.radians(self.alpha))

        # The distance in axis y
        a = d * math.sin(math.radians(self.alpha))

        # TODO: Check collision with walls and other entities
        x1 = self.x + b
        y1 = self.y + a
        x1 = round(x1, 6)
        y1 = round(y1, 6)

        # Update the current entity's position
        self.x = x1
        self.y = y1

        # Update the velocity
        new_v = min(self.desired_v, self.v_k + self.a * 0.01)
        self.v_k_minus1 = self.v_k
        self.v_k = round(new_v, 5)

        return x1, y1

    def is_reached_door(self):
        room = self.room
        return self.x >= room.door_top_x and room.door_bottom_y <= self.y <= room.door_top_y