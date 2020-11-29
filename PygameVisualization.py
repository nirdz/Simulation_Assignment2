import pygame

def display_events(pos_dict, room, num_time_iterations, wait_time=15, sim_size=800):
    # colors
    background_color = (170, 170, 170)  # grey
    people_color = (250, 0, 0)  # red
    object_color = (0, 0, 0)  # black

    # variable for initializing pygame
    normalizer = int(sim_size / room.size)  # the ratio (size of image) / (size of actual room)
    map_size = (int(room.size) * normalizer + 100,  # size of the map
                int(room.size) * normalizer + 100)  # plus a little free space
    wait_time = wait_time  # time that the simultation waits between each timestep
    wait_time_after_sim = 3000  # wait time after simulation
    #movement_data_dim = movement_data.shape

    pygame.init()  # initialize the intanz
    simulate = False  # variable to indicate if the simulation is running
    font = pygame.font.Font(None, 32)  # create a new object of type Font(filename, size)
    worldmap = pygame.display.set_mode(map_size)
    while True:
        # start simulation if any key is pressed and quits pygame if told so
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                simulate = True
            elif event.type == pygame.QUIT:
                pygame.quit()
        worldmap.fill(0)
        # This creates a new surface with text already drawn onto it
        text = font.render('Press any key to start the simulation', True, (255, 255, 255))
        # printing the text starting with a 'distance' of (100,100) from top left
        worldmap.blit(text, (100, 100))
        pygame.display.update()

        if simulate == True:
            # print the map for each timestep
            for t in range(num_time_iterations):
                # quit the simulation if told so
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                # initialize the map with background color
                worldmap.fill(background_color)

                # draw each peron for timestep t
                for key, val in pos_dict.items():
                    if t < len(val):
                        pygame.draw.circle(worldmap, people_color, (normalizer*val[t][0], normalizer*val[t][1]), normalizer*0.25)

                # draw walls
                # up and down walls
                pygame.draw.line(worldmap, object_color,
                                 (0, 0),
                                 (int(room.size) * normalizer, 0), 2)
                pygame.draw.line(worldmap, object_color,
                                 (0, int(room.size) * normalizer),
                                 (int(room.size) * normalizer, int(room.size) * normalizer), 2)
                # door
                pygame.draw.line(worldmap, object_color,
                                 (int(room.size) * normalizer, 0),
                                 (normalizer * room.door_bottom_x, normalizer * room.door_bottom_y), 2)
                pygame.draw.line(worldmap, object_color,
                                 (normalizer * room.door_top_x, normalizer * room.door_top_y),
                                   (int(room.size) * normalizer, int(room.size) * normalizer), 2)
                # pygame.draw.lines(worldmap, object_color, True,
                #                   [(normalizer * room.door_top_x, normalizer * room.door_top_y),
                #                    (normalizer * room.door_bottom_x, normalizer * room.door_bottom_y)])



                strd = "Number of People: " + str(len(pos_dict))
                textd = font.render(strd, True, (255, 255, 255))
                # printing the text starting with a 'distance' of (400,10) from top left
                worldmap.blit(textd, (400, 10))

                # update the map
                pygame.display.update()
                # wait for a while before drawing new positions
                pygame.time.wait(wait_time)
            simulate = False
            text = font.render('SIMULATION FINISHED', True, (255, 255, 255))
            worldmap.blit(text, (100, 100))
            pygame.display.update()
            pygame.time.wait(wait_time_after_sim)