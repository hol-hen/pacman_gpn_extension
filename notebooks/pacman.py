# name

# start modules
import pgzrun

# create constants
WIDTH = 1024
HEIGHT = 768
lives = 3

WHITE = (255, 255, 255)
BLACK = (0,0,0)

# make pacman
pacman = Actor('pacopen') # how can you animate pacman too?
pacman.x = 487
pacman.y = 675

# make ghosts
ghosts = [Actor('ghostblue'), Actor('ghostgreen'), Actor('ghostpink'), Actor('ghostred')]
ghosts_x = [487, 537, 287, 937]
ghosts_y = [475, 375, 125, 575]

for i in range(len(ghosts)):
    ghosts[i].x = ghosts_x[i]
    ghosts[i].y = ghosts_y[i]

# make lives
lives_pics = [Actor('heart'), Actor('heart'), Actor('heart')]     
i = 0
for heart in lives_pics:
    heart.y = 22
    heart.x = 888 + i*30
    i += 1

# make walls -- you will need to make sure ghosts and pacman can't go through walls
walls = []
with open("walls.csv", "r") as file:
    lines = file.readlines()
    
for line in lines:
    coords = line.split(",")
    wall = Actor('wall')
    wall.x = int(coords[0])
    wall.y = int(coords[1])
    walls.append(wall)

# make dots -- you will need to make sure ghosts and pacman can't go through walls
dots = []
with open("dots.csv", "r") as file:
    lines_dots = file.readlines()
    
for line in lines_dots:
    coords = line.split(",")
    dot = Actor('dot')
    dot.x = int(coords[0])
    dot.y = int(coords[1])
    dots.append(dot)

# draw everything to screen
def draw():
    global lives
    
    for i in range(lives):
        lives_pics[i].draw()

    screen.draw.text('Lives ',topright=(860,10), color=WHITE, fontsize = 25, fontname='videogame')    

    # draw characters
    pacman.draw()
    for ghost in ghosts:
        ghost.draw()

    # draw walls
    for wall in walls:
        wall.draw()

    # draw dots
    for dot in dots:
        dot.draw()



    
# update everything
# def update():


# runs everything
pgzrun.go()
