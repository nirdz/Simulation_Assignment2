class Door:
    def __init__(self, width, top_x, top_y, bottom_x, bottom_y, center_x, center_y):
        self.width = width
        self.top_x = top_x
        self.top_y = top_y
        self.bottom_x = bottom_x
        self.bottom_y = bottom_y
        self.center_x = center_x
        self.center_y = center_y


class Room:
    def __init__(self, size=15.0, doors=1, door_width=1.7):
        self.size = size
        right_door = Door(door_width, size, round((size / 2.0) + (door_width / 2.0), 3), size,
                          round((size / 2.0) - (door_width / 2.0), 3), size, size/2)

        left_door = Door(door_width, 0, round((size / 2.0) + (door_width / 2.0), 3), 0,
                         round((size / 2.0) - (door_width / 2.0), 3), 0, size/2)

        if doors == 1:
            self.doors = [right_door]
        else:  # 2 doors
            self.doors = [right_door, left_door]
        # self.doors = doors
        # self.door_width = door_width
        # self.door_top_x = size
        # self.door_top_y = round((size / 2.0) + (door_width / 2.0), 3)
        # self.door_bottom_x = size
        # self.door_bottom_y = round((size / 2.0) - (door_width / 2.0), 3)
        # self.center_door_x = size
        # self.center_door_y = self.size/2


        """
        |
        |
        |   -> (door_top_x, door_top_y)
            

        |   -> (door_bottom_x, door_bottom_y)
        |
        | 
        """

    # def set_entities(self, entities):
    #     self.entities = entities  # list of entities
    #     self.entities_pos = []  # list of tuples, each represents entity's location in x and y axises
    #     for i in range(len(entities)):
    #         self.entities_pos.append(entities[i].location)