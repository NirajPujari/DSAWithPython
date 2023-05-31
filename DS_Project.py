import pygame
import random
from pygame.locals import *
from Circular_Queue import CircularQueue
from time import *

#Define the Car class.
class Car:

    def __init__(self, image, x, y, speed):
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed

    def R1_1_move(self):
        self.x += self.speed
    def R1_2_move(self):
        self.x += self.speed
    def R2_1_move(self):
        self.y += self.speed
    def R2_2_move(self):
        self.y += self.speed
    def R3_1_move(self):
        self.x -= self.speed
    def R3_2_move(self):
        self.x -= self.speed
    def R4_1_move(self):
        self.y -= self.speed
    def R4_2_move(self):
        self.y -= self.speed

#Colours
Red = (255, 0, 0)
Black = (0,0,0)
White = (255,255,255)
Color1 = (0, 0, 139)
Color2 = (135, 206, 235)

#This is used to show the route.
def Show_Road(text, x):
    text_rects = list()
    special_font = pygame.font.SysFont('comicsansms', 40)
    text_surfaces = [special_font.render(line, True, Color1) for line in text.split("\n")]
    for i in range(len(text_surfaces)):
        if i == 0:
            text_rects.append(text_surfaces[0].get_rect(center=(x, 700)))
            continue
        else:
            text_rects.append(text_surfaces[i].get_rect(center=(x, 80*i+700)))
    return (text_surfaces, text_rects)

#This function is used to make the button with taking all the necessary inputs.
def create_button(text, position, button_size, color_of_button, text_color):

    #Create the button surface.
    button_width, button_height = button_size
    button_surface = pygame.Surface((button_width, button_height))
    button_rect = button_surface.get_rect(center=position)
    
    #To change the color of the button.
    button_color = pygame.Color(color_of_button)
    button_surface.fill(button_color)

    #Render the text surface.
    text_surface = font.render(text, True, pygame.Color(text_color))

    #Blit the text surface onto the button surface.
    text_rect = text_surface.get_rect(center=button_surface.get_rect().center)
    button_surface.blit(text_surface, text_rect)

    #Return the button surface and rect as a tuple, along with the action function.
    return (button_surface, button_rect)

#This is used to show Road No..
def Road_No(text, x, y):
    special_font = pygame.font.SysFont('timesnewroman', 30)
    text_surfaces = special_font.render(text, True, White)
    text_rects = text_surfaces.get_rect(center=(x, y))
    return (text_surfaces, text_rects)

#Initialize Pygame.
pygame.init()

#Create a Queue for traffic lights.
traffic_lights = CircularQueue()

#Set the window size.
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 1000

#Create a font object.
font = pygame.font.SysFont("timesnewroman", 80)

#Create the window.
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#Set the title of the window.
pygame.display.set_caption('Four-Way Traffic Road')

#Create Rect objects for the horizontal and vertical parts of the road.
horizontal_road = pygame.Rect(0, 405, 1500, 220)
vertical_road = pygame.Rect(650, 0, 200, 1000)

#Make a black screen and draw the roads onto the screen.
screen.fill(Color2)
pygame.draw.rect(screen, White, horizontal_road)
pygame.draw.rect(screen, White, vertical_road)


#Create buttons using the create_button function.
Forward = create_button("Forward", (325 , 200), (350, 400), Color2, Color1)
Backward = create_button("Backward", (350, 825), (450, 400), Color2, Color1)
Mode = create_button("Change Mode", (1175, 100), (650, 203), Color2, Color1)

#It is used to print the button on screen.
screen.blit(Forward[0], Forward[1])
screen.blit(Backward[0], Backward[1])
screen.blit(Mode[0], Mode[1])

#Using a create button function Create objects to show the mode
Auto = create_button("Auto Mode", (1175, 300), (650, 203),  Color2, Color1)
Manual = create_button("Manual Mode", (1175, 300), (650, 203),  Color2, Color1)
screen.blit(Auto[0], Auto[1])

#Displaying the road routes.
Road1 = Show_Road("Top->R1\nStop->R2\nStop->R3\nRear->R4", 1175)
Road2 = Show_Road("Top->R2\nStop->R3\nStop->R4\nRear->R1", 1175)
Road3 = Show_Road("Top->R3\nStop->R4\nStop->R1\nRear->R2", 1175)
Road4 = Show_Road("Top->R4\nStop->R1\nStop->R2\nRear->R3", 1175)

#Displaying the road no..
R1 = Road_No('R1', 50, 350)
R2 = Road_No('R2', 900, 50)
R3 = Road_No('R3', 1450, 675)
R4 = Road_No('R4', 600, 950)

screen.blit(R1[0],R1[1])
screen.blit(R2[0],R2[1])
screen.blit(R3[0],R3[1])
screen.blit(R4[0],R4[1])

#To change the the road.
Temp = pygame.Rect(950,650,450,350)

#This are the block roads
Block_1_1 = pygame.Rect(850,525,100,100)
Block_1_2 = pygame.Rect(750,305,100,100)
Block_2_1 = pygame.Rect(650,625,100,100)
Block_2_2 = pygame.Rect(850,525,100,100)
Block_3_1 = pygame.Rect(550,405,100,100)
Block_3_2 = pygame.Rect(650,625,100,100)
Block_4_1 = pygame.Rect(750,305,100,100)
Block_4_2 = pygame.Rect(550,405,100,100)

#Update the screen.
pygame.display.flip()

#This function is used to check if the mouse is clicked.
#If the button is clicked check for which button is clicked and do the work.
def check_button():
    if Mode[1].collidepoint(event.pos):
        traffic_lights.mode = change_mode()
    else:
        if traffic_lights.mode == 'Manual':
            change_road()

#This function is used to change the mode of the road movement.
def change_mode():
    if traffic_lights.mode == 'Auto':
        mode = 'Manual'
        screen.blit(Manual[0], Manual[1])
        return mode
    if traffic_lights.mode == 'Manual':
        mode = 'Auto'
        screen.blit(Auto[0], Auto[1])
        return mode
        
#This function is used to change the road.
def change_road():
    if Forward[1].collidepoint(event.pos):
        traffic_lights.forward()
        pygame.draw.rect(screen, White, horizontal_road)
        pygame.draw.rect(screen, White, vertical_road)
    elif Backward[1].collidepoint(event.pos):
        traffic_lights.backward()
        pygame.draw.rect(screen, White, horizontal_road)
        pygame.draw.rect(screen, White, vertical_road)

#Set the position of the horizontal and vertical roads.
horizontal_road_x = 0
horizontal_road_y = (WINDOW_HEIGHT - 200) // 2
vertical_road_x = (WINDOW_WIDTH - 200) // 2
vertical_road_y = 0

#Set the speed of the cars.
car_speed = 3

#Load the car images.
V_car_images = [pygame.image.load('V_car_red.png'), pygame.image.load('V_car_green.png'), pygame.image.load('V_car_blue.png')]
H_car_images = [pygame.image.load('H_car_red.png'), pygame.image.load('H_car_green.png'), pygame.image.load('H_car_blue.png')]
V1_car_images = [pygame.image.load('V1_car_red.png'), pygame.image.load('V1_car_green.png'), pygame.image.load('V1_car_blue.png')]
H1_car_images = [pygame.image.load('H1_car_red.png'), pygame.image.load('H1_car_green.png'), pygame.image.load('H1_car_blue.png')]

#Load the image of the center.
r1_image = pygame.image.load('R1.png')
r2_image = pygame.image.load('R2.png')
r3_image = pygame.image.load('R3.png')
r4_image = pygame.image.load('R4.png')

#Create a list of cars.
R1_1_cars = list()
R1_2_cars = list()
R2_1_cars = list()
R2_2_cars = list()
R3_1_cars = list()
R3_2_cars = list()
R4_1_cars = list()
R4_2_cars = list()

#Create a clock object to control the frame rate.
clock = pygame.time.Clock()

#This is the starting time.
start_time = monotonic()

#Create a game loop.
while True:

    #Checking for all mouse clicks
    for event in pygame.event.get():

        #Quit the game if the user clicks the close button.
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        #This function is used to change the mode of the road movement.
        elif event.type == pygame.MOUSEBUTTONUP:

            #Check if either button was clicked and call its action function if so
            check_button()
                    
    #Add new cars to the list.
    if random.randint(1, 100) == 1:
        R1_1_cars.append(Car(random.choice(H_car_images), -100, 425, car_speed))
    if random.randint(1, 100) == 1:
        R1_2_cars.append(Car(random.choice(H_car_images), 850, 425, car_speed))
    if random.randint(1, 100) == 1:
        R2_1_cars.append(Car(random.choice(V_car_images), 775, 0, car_speed))
    if random.randint(1, 100) == 1:
        R2_2_cars.append(Car(random.choice(V_car_images), 775, 600, car_speed))
    if random.randint(1, 100) == 1:
        R3_1_cars.append(Car(random.choice(H1_car_images), 1500, 550, car_speed))
    if random.randint(1, 100) == 1:
        R3_2_cars.append(Car(random.choice(H1_car_images), 575, 550, car_speed))
    if random.randint(1, 100) == 1:
        R4_1_cars.append(Car(random.choice(V1_car_images), 675, 900, car_speed))
    if random.randint(1, 100) == 1:
        R4_2_cars.append(Car(random.choice(V1_car_images), 675, 350, car_speed))

    #Move and draw the cars.
    #According to the mode.
    if traffic_lights.mode =='Auto':

        #This is to show the rotue of the cars.
        if traffic_lights.road == "R1":
            pygame.draw.rect(screen, Red, Block_1_1)
            pygame.draw.rect(screen, Red, Block_1_2)
            pygame.draw.rect(screen, Color2, Temp)
            for i, surface in enumerate(Road1[0]):
                screen.blit(surface, Road1[1][i])
            screen.blit(r1_image, (650, 410))
        if traffic_lights.road == "R2":
            pygame.draw.rect(screen, Red, Block_2_1)
            pygame.draw.rect(screen, Red, Block_2_2)
            pygame.draw.rect(screen, Color2, Temp)
            for i, surface in enumerate(Road2[0]):
                screen.blit(surface, Road2[1][i])
            screen.blit(r2_image, (650, 409))
        if traffic_lights.road == "R3":
            pygame.draw.rect(screen, Red, Block_3_1)
            pygame.draw.rect(screen, Red, Block_3_2)
            pygame.draw.rect(screen, Color2, Temp)
            for i, surface in enumerate(Road3[0]):
                screen.blit(surface, Road3[1][i])
            screen.blit(r3_image, (650, 409))
        if traffic_lights.road == "R4":
            pygame.draw.rect(screen, Red, Block_4_1)
            pygame.draw.rect(screen, Red, Block_4_2)
            pygame.draw.rect(screen, Color2, Temp)
            for i, surface in enumerate(Road4[0]):
                screen.blit(surface, Road4[1][i])
            screen.blit(r4_image, (650, 409))

        #This is the current time.
        current_time = monotonic()

        #When Road 1 and 2 is on.
        if traffic_lights.road == "R1" or traffic_lights.road == "R2":
            for car in R1_1_cars:
                car.R1_1_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.x >= 575:
                    R1_1_cars.remove(car)
                    new = pygame.Surface((car.image.get_width(), car.image.get_height()))
                    new.fill(White)
                    screen.blit(new, (575,425))

        #When Road 2 and 3 is on.
        if traffic_lights.road == "R2" or traffic_lights.road == "R3":
            for car in R2_1_cars:
                car.R2_1_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.y >= 325:
                    R2_1_cars.remove(car)
                    new = pygame.Surface((car.image.get_width(), car.image.get_height()))
                    new.fill(White)
                    screen.blit(new, (775,325))

        #When Road 3 and 4 is on.
        if traffic_lights.road == "R3" or traffic_lights.road == "R4":
            for car in R3_1_cars:
                car.R3_1_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.x < 850:
                    R3_1_cars.remove(car)
                    new = pygame.Surface((car.image.get_width(), car.image.get_height()))
                    new.fill(White)
                    screen.blit(new, (850,550))

        #When Road 4 and 1 is on.
        if traffic_lights.road == "R4" or traffic_lights.road == "R1":
            for car in R4_1_cars:
                car.R4_1_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.y < 625:
                    R4_1_cars.remove(car)
                    new = pygame.Surface((car.image.get_width(), car.image.get_height()))
                    new.fill(White)
                    screen.blit(new, (675,625))

        #It will be work doen't matter the road.
        if traffic_lights.road:
            for car in R1_2_cars:
                car.R1_2_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.x > WINDOW_WIDTH:
                    R1_2_cars.remove(car)

            for car in R2_2_cars:
                car.R2_2_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.y > WINDOW_HEIGHT:
                    R2_2_cars.remove(car)

            for car in R3_2_cars:
                car.R3_2_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.x < -100:
                    R3_2_cars.remove(car)

            for car in R4_2_cars:
                car.R4_2_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.y < -100:
                    R4_2_cars.remove(car)

        #Here we are checking if the 30 sec is passed or not.
        #If the time is passed it will change the road
        if current_time - start_time >= 3:
            start_time = monotonic()
            traffic_lights.forward()
            pygame.draw.rect(screen, pygame.Color('white'), horizontal_road)
            pygame.draw.rect(screen, pygame.Color('white'), vertical_road)


    #This is used to make The manual work.
    if traffic_lights.mode =='Manual':

        #This is to show the rotue of the cars.
        if traffic_lights.road == "R1":
            pygame.draw.rect(screen, Red, Block_1_1)
            pygame.draw.rect(screen, Red, Block_1_2)
            pygame.draw.rect(screen, Color2, Temp)
            for i, surface in enumerate(Road1[0]):
                screen.blit(surface, Road1[1][i])
            screen.blit(r1_image, (650, 410))
        if traffic_lights.road == "R2":
            pygame.draw.rect(screen, Red, Block_2_1)
            pygame.draw.rect(screen, Red, Block_2_2)
            pygame.draw.rect(screen, Color2, Temp)
            for i, surface in enumerate(Road2[0]):
                screen.blit(surface, Road2[1][i])
            screen.blit(r2_image, (650, 409))
        if traffic_lights.road == "R3":
            pygame.draw.rect(screen, Red, Block_3_1)
            pygame.draw.rect(screen, Red, Block_3_2)
            pygame.draw.rect(screen, Color2, Temp)
            for i, surface in enumerate(Road3[0]):
                screen.blit(surface, Road3[1][i])
            screen.blit(r3_image, (650, 409))
        if traffic_lights.road == "R4":
            pygame.draw.rect(screen, Red, Block_4_1)
            pygame.draw.rect(screen, Red, Block_4_2)
            pygame.draw.rect(screen, Color2, Temp)
            for i, surface in enumerate(Road4[0]):
                screen.blit(surface, Road4[1][i])
            screen.blit(r4_image, (650, 409))

        #When Road 1 and 2 is on.
        if traffic_lights.road == "R1" or traffic_lights.road == "R2":
            for car in R1_1_cars:
                car.R1_1_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.x >= 575:
                    R1_1_cars.remove(car)
                    new = pygame.Surface((car.image.get_width(), car.image.get_height()))
                    new.fill(White)
                    screen.blit(new, (575,425))

        #When Road 2 and 3 is on.
        if traffic_lights.road == "R2" or traffic_lights.road == "R3":
            for car in R2_1_cars:
                car.R2_1_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.y >= 325:
                    R2_1_cars.remove(car)
                    new = pygame.Surface((car.image.get_width(), car.image.get_height()))
                    new.fill(White)
                    screen.blit(new, (775,325))

        #When Road 3 and 4 is on.
        if traffic_lights.road == "R3" or traffic_lights.road == "R4":
            for car in R3_1_cars:
                car.R3_1_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.x < 850:
                    R3_1_cars.remove(car)
                    new = pygame.Surface((car.image.get_width(), car.image.get_height()))
                    new.fill(White)
                    screen.blit(new, (850,550))

        #When Road 4 and 1 is on.
        if traffic_lights.road == "R4" or traffic_lights.road == "R1":
            for car in R4_1_cars:
                car.R4_1_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.y < 625:
                    R4_1_cars.remove(car)
                    new = pygame.Surface((car.image.get_width(), car.image.get_height()))
                    new.fill(White)
                    screen.blit(new, (675,625))

        #It will be work doen't matter the road.
        if traffic_lights.road:
            for car in R1_2_cars:
                car.R1_2_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.x > WINDOW_WIDTH:
                    R1_2_cars.remove(car)

            for car in R2_2_cars:
                car.R2_2_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.y > WINDOW_HEIGHT:
                    R2_2_cars.remove(car)

            for car in R3_2_cars:
                car.R3_2_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.x < -100:
                    R3_2_cars.remove(car)

            for car in R4_2_cars:
                car.R4_2_move()
                screen.blit(car.image, (car.x, car.y))
                #Remove cars that have gone off the bottom of the screen.
                if car.y < -100:
                    R4_2_cars.remove(car)
    
    #Update the display.
    pygame.display.update()
    
    #Control the frame rate.
    clock.tick(100)