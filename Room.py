class Room:
    def __init__(self, size=15.0, doors=1, door_width=0.9):
        self.size = size
        self.doors = doors
        self.door_width = door_width
        self.door_x = size
        self.door_y = size / 2.0

    # def set_entities(self, entities):
    #     self.entities = entities  # list of entities
    #     self.entities_pos = []  # list of tuples, each represents entity's location in x and y axises
    #     for i in range(len(entities)):
    #         self.entities_pos.append(entities[i].location)