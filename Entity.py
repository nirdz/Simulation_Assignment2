import math

class Entity:
    def __init__(self, i, room, x0, y0, body_radius=0.5, v0=0, desired_v=0.6, tau=0.5):
        self.i = i
        self.room = room  # Room object
        self.x = x0  # starting x location
        self.y = y0  # starting y location
        self.body_radius = body_radius  # For collision with other people
        self.goal_x = room.door_x
        self.goal_y = room.door_y
        self.goal_y_offset = room.door_width / 2
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
        return self.x >= self.goal_x \
               and \
               self.goal_y - self.goal_y_offset <= self.y <= self.goal_y + self.goal_y_offset