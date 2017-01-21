import random
import tkMessageBox
from Tkinter import *
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 360), 0, 32)


def gravity(t):
    return 8 * t - 8


def main():
    counter = 0
    rectcounter = 0
    pipes = []
    bools = []
    a = 186
    b = 182
    c = 194
    d = 190
    e = 198
    f = 300
    rectspeed = -1
    check = False
    dead = False
    score = 0

    while True:
        penguin = [[f + 4, a], [f + 12, b], [f + 20, b], [f + 28, a], [f + 36, a], [f + 36, c], [f + 28, c],
                   [f + 20, e],
                   [f + 12, e], [f + 2, c], [f + 4, a]]
        one = [[f + 32, c], [f + 28, c], [f + 28, e]]
        two = [[f + 4, a], [f, a], [f, d]]
        three = [[f + 4, d], [f, c], [f, d]]
        four = [[f + 20, c], [f + 20, d], [f + 8, a]]
        screen.fill((32, 178, 170))

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[K_SPACE]:
                check = True
                break
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if check:
            break

        pygame.draw.polygon(screen, (0, 0, 0), penguin)
        pygame.draw.polygon(screen, (255, 127, 80), one)
        pygame.draw.polygon(screen, (255, 127, 80), two)
        pygame.draw.polygon(screen, (255, 127, 80), three)
        pygame.draw.polygon(screen, (0, 0, 255), four)

        pygame.display.update()

    while True:
        penguin = [[f + 4, a], [f + 12, b], [f + 20, b], [f + 28, a], [f + 36, a], [f + 36, c], [f + 28, c],
                   [f + 20, e],
                   [f + 12, e], [f + 2, c], [f + 4, a]]
        one = [[f + 32, c], [f + 28, c], [f + 28, e]]
        two = [[f + 4, a], [f, a], [f, d]]
        three = [[f + 4, d], [f, c], [f, d]]
        four = [[f + 20, c], [f + 20, d], [f + 8, a]]

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[K_SPACE]:
                counter = 0
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((32, 178, 170))

        pygame.draw.polygon(screen, (0, 0, 0), penguin)
        pygame.draw.polygon(screen, (255, 127, 80), one)
        pygame.draw.polygon(screen, (255, 127, 80), two)
        pygame.draw.polygon(screen, (255, 127, 80), three)
        pygame.draw.polygon(screen, (0, 0, 255), four)

        if rectcounter % 135 == 0:
            pipes.append(640)
            pipes.append(random.randint(0, 240))
            bools.append(True)

        for x in range(0, len(pipes) - 1, 2):
            pygame.draw.rect(screen, (0, 0, 255), Rect((pipes[x], 0), (40, pipes[x + 1])))
            newy = pipes[x + 1] + 120
            pygame.draw.rect(screen, (0, 0, 255), Rect((pipes[x], newy), (40, 360 - newy)))
            pipes[x] += rectspeed

        for y in range(0, len(pipes) - 1, 2):
            test1 = e > pipes[y + 1] + 120
            test2 = b < pipes[y + 1]
            test3 = 36 + f > pipes[y]
            test4 = 36 + f < pipes[y] + 40
            test5 = 36 + f > pipes[y] + 40

            if test4 and test3 and (test2 or test1):
                dead = True

            if bools[y / 2] and test5:
                bools[y / 2] = False
                score += 1

        if e > 360 or b < 0:
            dead = True

        pygame.display.update()

        if not dead:
            a += gravity(counter)
            b += gravity(counter)
            c += gravity(counter)
            d += gravity(counter)
            e += gravity(counter)
            counter += .05
            rectcounter += 1

        else:
            rectspeed = 0
        if dead:
            root = Tk().withdraw()
            if tkMessageBox.askokcancel("RESTART",
                                        'You died with a score of ' + str(
                                            score) + ". \n Press 'space' to start again."):
                main()
            break


root = Tk().withdraw()
if tkMessageBox.askokcancel("START", "Press 'space' to start."):
    main()
