# name

# start modules
import pgzrun

# create constants
WIDTH = 1024
HEIGHT = 768
score = 0

Y_TARGET = 657

WHITE = (255, 255, 255)
BLACK = (0,0,0)

# make lanes
lanes = [Actor('laneleft'), Actor('laneup'), Actor('lanedown'), Actor('laneright')]
lanes_x = [282, 432, 592, 742]
lane_y = HEIGHT/2

for i in range(4):
    lanes[i].x = lanes_x[i]
    lanes[i].y = lane_y


# make notes - filenames are in the image folder
note_y_initial = 100


# draw everything to screen
def draw():
    global score
    
    for lane in lanes:
        lane.draw()

    screen.draw.text('Score ' + str(score),topleft=(10,10), color=WHITE, fontsize = 45, fontname='videogame')    
    
# Scoring:
    # If distance <= 15, this is a PERFECT score and receives 10 points
    # If 15 < distance <= 50, this is a GOOD score and receives 5 points
    # If 50 < distance <= 100, this is a BAD score and receives -1 points
    # If 100 < distance <= 200, this is a MISS and receives -5 points

    # Try writing the score message (perfect, good etc.) on the screen after each note

# update everything
# def update():


# play music
    # check the music folder for the name of the music file
    # use the pygame cheatsheet for help.


# runs everything
pgzrun.go()
