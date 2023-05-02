from makemazes import Maze
import pygame
from sys import exit

# GENERAL WINDOW AND PYGAME UTILITIES
pygame.init()
WINWIDTH = 800
WINHEIGHT = 800
screen = pygame.display.set_mode((WINWIDTH, WINHEIGHT))  # create window of dimension...
pygame.display.set_caption("maze dude")  # window title
clock = pygame.time.Clock()  # main game clock
# EVENTS
NEWGAME = pygame.USEREVENT + 1
PAUSE = pygame.USEREVENT + 2
MENU = pygame.USEREVENT + 3
SOLVED = pygame.USEREVENT + 4
#Global Vars (general)



def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == NEWGAME:
                pass
            if event.type == PAUSE:
                pass
            if event.type == MENU:
                pass
            if event.type == SOLVED:
                pass
        pygame.display.update()
        clock.tick(60)  # frame rate

def newgame(difficulty):
    pass
def drawmaze(difficulty): # I'm not doing anything with difficulty for now, that'll determine the maze-size later.
    maze_size = 10
    cell_size = WINWIDTH//900
    for x in range(0,maze_size):
        for y in range(0,maze_size):
            pass

'''
So we'll place it on like four edges around a node on the graph and if the edge exists, we don't draw a line (for every edge delete a line)
The thing starts like a grid, and the squares are nodes and the walls are edges (or ig the lack of edges?). Graph is unweighted, nodes are numbered.

Difficulty to size mapping (by cell count, cell size is proportional to window size, window size to fit screen):
Easy: 50 x 50
Medium: 100 x 100
Hard: 200 x 200
Impossible: 1000 x 1000

Controls - WASD standard

TEXTURES & PICTURES AND STUFF
character -
walls -
open space -
movement sound effect -
music for impossible -
music for hard -
music for medium -
music for start screen/easy -
success sound effect -

Stuff to make:
function to draw the maze
function to generate the maze
function to move the character
function to put in the character
function for pause screen (start button, quit button, back to main menu button, music & image creds on side)
function for home screen (quit button, difficulty selection: easy, medium, hard, impossible)
function for success screen (quit button, share button, difficulty selection: easy, medium, hard, impossible)
function to track time on maze
function to check if character is on the end square
If you have time you can do a high scores leaderboard, but I don't really want to do file handling, or
anything like that so that choice is your's alone.
'''

if __name__ == '__main__':
    test_maze = Maze(5, "easy", 0)