from math import floor

from makemazes import Maze
import pygame
from sys import exit

# GENERAL WINDOW AND PYGAME UTILITIES
pygame.init()
WINWIDTH = 980
WINHEIGHT = 700
screen = pygame.display.set_mode((WINWIDTH, WINHEIGHT))  # create window of dimension...
pygame.display.set_caption("maze dude")  # window title
clock = pygame.time.Clock()  # main game clock

# EVENTS
NEWGAME = pygame.USEREVENT + 1
SOLVED = pygame.USEREVENT + 2


class Character:
    def __init__(self, x, y, cellsize):
        self.x = x
        self.y = y
        self.cellsize = cellsize
        self.color = (0, 0, 255)  # the color of the character
        self.speed = 40  # character speed (the lower, the faster)
        self.last_move = pygame.time.get_ticks()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x * self.cellsize, self.y * self.cellsize, self.cellsize, self.cellsize))

    def move(self, dx, dy, maze):
        now = pygame.time.get_ticks()
        if now - self.last_move > self.speed:  # check if enough time has passed since the last move
            if maze.mazegrid[self.y + dy][self.x + dx] != 'W':  # if it's not a wall
                self.x += dx
                self.y += dy
                self.last_move = now
            if maze.mazegrid[self.y][self.x] == "WIN":
                pygame.event.post(pygame.event.Event(SOLVED))


def main():
    currentmaze = Maze(24, 17)
    cellsize = 20
    character = Character(0, 0, cellsize)  # initializing the character at the top left corner
    character.x = 1
    character.y = 1
    start_ticks = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == NEWGAME:
                if event.type == NEWGAME:
                    currentmaze = Maze(24, 17)  # generate a new maze
                    start_ticks = pygame.time.get_ticks()  # restart the timer
            if event.type == SOLVED:
                solved_screen(start_ticks)
                pygame.event.post(pygame.event.Event(NEWGAME))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            character.move(0, -1, currentmaze)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            character.move(0, 1, currentmaze)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            character.move(-1, 0, currentmaze)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            character.move(1, 0, currentmaze)

        drawmaze(currentmaze, cellsize)
        character.draw(screen)  # draw the character
        pygame.display.update()
        clock.tick(60)  # frame rate


def drawmaze(mymaze, cellsize):
    maze = mymaze.mazegrid
    maze_height = len(maze)
    maze_width = len(maze[0])
    for i in range(maze_height):
        for j in range(maze_width):
            cell = maze[i][j]
            color = None
            if cell == 'W':
                color = (0, 0, 0)
            elif cell == "WIN":
                color = (0, 255, 0)
            else:
                color = (255, 255, 255)
            pygame.draw.rect(screen, color, (j * cellsize, i * cellsize, cellsize, cellsize))


def solved_screen(time_taken):
    font = pygame.font.Font(None, 36)
    font = pygame.font.Font(None, 36)
    minutes_taken = floor(time_taken / 60)
    seconds_taken = floor(time_taken % 60)
    if minutes_taken<=2:
        message = font.render(f"You solved it in {seconds_taken} seconds!", True, (0, 0, 0))
    else:
        message = font.render(f"You solved it in {minutes_taken} minutes and {seconds_taken} seconds!", True, (0, 0, 0))
    message_rect = message.get_rect(center=(WINWIDTH / 2, WINHEIGHT / 2))

    button_color = (200, 200, 200)
    button_text_color = (0, 0, 0)
    button_font = pygame.font.Font(None, 24)
    button_text = button_font.render("Play Again", True, button_text_color)
    button_width = 200
    button_height = 50
    button_rect = pygame.Rect(WINWIDTH / 2 - button_width / 2, WINHEIGHT / 2 + button_height, button_width,
                              button_height)

    screen.fill((255, 255, 255))  # clear the screen
    screen.blit(message, message_rect)
    pygame.draw.rect(screen, button_color, button_rect)
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)

    pygame.display.flip()

    while True:  # wait for the user to click the button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):  # if the mouse click is within the button
                    return  # exit the solved screen
        pygame.time.delay(100)  # don't consume 100% CPU


if __name__ == '__main__':
    main()
