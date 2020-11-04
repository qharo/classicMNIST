#------MODULES------#
import pygame
import tens
#------------#

#----------COLORS---------#
WHITE = (255, 255, 255)
BLACK = (0,0,0)
CREAM = (255, 255, 240)
#------------#

#------CLASSES------#
class Block:
  def __init__(self, x, y, color, width):
    self.x = x
    self.y = y
    self.color = color
    self.width = width

class State:
  def __init__(self, n, start):
    self.n = n
    self.x = start[0]
    self.y = start[1]
    self.grid = []
    xM = start[0]
    yM = start[1]
    for x in range(n):
        row = []
        for y in range(0,n):
            block = Block(xM, yM, WHITE, 10)
            row.append(block)
            xM += 11
        yM += 11
        xM = self.x
        self.grid.append(row)
#-------------#

#-------INITIALIZATION------#
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Classic MNIST")
#------------#

#---DRAWING---#
def draw(surface, curState):
    N = curState.n
    for x in range(N):
        for y in range(N):
            block = curState.grid[x][y]
            pygame.draw.rect(surface, block.color, [block.x, block.y, block.width, block.width])
#------------#

#------FONT RENDERING------#
def write(text, location, size):
    x = location[0]
    y = location[1]    
    fontStyle = pygame.font.Font("freesansbold.ttf", size)
    textSurf = fontStyle.render(text, True, BLACK)
    textRect = textSurf.get_rect()
    textRect.center = (x, y)
    screen.blit(textSurf, textRect)
#------------#

#------UI------#
def ui():
    pygame.draw.rect(screen, CREAM, [500, 0, 300, 600])
    pygame.draw.rect(screen, BLACK, [525, 50, 250, 75])
    pygame.draw.rect(screen, CREAM, [525 + B_W, 50 + B_W, 250 - 2*B_W, 75 - 2*B_W])
    pygame.draw.rect(screen, BLACK, [525, 475, 250, 75])
    pygame.draw.rect(screen, CREAM, [525 + B_W, 475 + B_W, 250 - 2*B_W, 75 - 2*B_W])
    write("PREDICT", (650, 88), 40)
    write("RESET", (650, 513), 40)
#------------#

#------SENDING IMAGE------#
def img(blocks):
    grid = []
    for x in range(len(blocks)):
        row = []
        for y in range(len(blocks[x])):
            if blocks[x][y].color == WHITE:
                row.append(0)
            else:
                row.append(1)
        grid.append(row)
    return grid
#------------#

#---------EVENT LOOP-------#
running = True
MOUSEDOWN = False
N = 28
GRIDSTART = [100,125]
state = State(N, GRIDSTART)
GRIDEND = [GRIDSTART[0] + (N*11-1), GRIDSTART[1] + (N*11-1)]
B_W = 3
draw(screen, state)
ui()
while running:
    #EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            MOUSEDOWN = True
        if event.type == pygame.MOUSEBUTTONUP:
                MOUSEDOWN = False
    mx, my = pygame.mouse.get_pos()

    #DRAWING THE NUMBER
    if(GRIDSTART[0] < mx < GRIDEND[0] and GRIDSTART[1] < my < GRIDEND[1] and MOUSEDOWN):
        ix = (mx - GRIDSTART[0])//11
        iy = (my - GRIDSTART[1])//11
        state.grid[iy][ix].color = BLACK
        draw(screen,state)
    
    #PREDICT
    if(525 < mx < 775 and 50 < my < 125 and MOUSEDOWN):
        empty = True        
        for x in range(N):
            for y in range(N):
                if(state.grid[x][y].color == BLACK):
                    empty = False
        if(not empty):
            write("PREDICTION:", (650, 200), 40)
            write(tens.predict([img(state.grid)]), (650,325), 200)
        

    #RESET
    if(525 < mx < 775 and 475 < my < 550 and MOUSEDOWN):
        for x in range(N):
            for y in range(N):
                state.grid[x][y].color = WHITE
        draw(screen, state)
        ui()

    pygame.display.update()
#------------#

