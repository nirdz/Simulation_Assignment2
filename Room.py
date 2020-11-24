class Room:
    def __init__(self, size=15.0, doors=1, door_width=1.1):
        self.size = size
        self.doors = doors
        self.door_width = door_width
        self.door_top_x = size
        self.door_top_y = round((size / 2.0) + (door_width / 2.0), 3)
        self.door_bottom_x = size
        self.door_bottom_y = round((size / 2.0) - (door_width / 2.0), 3)
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