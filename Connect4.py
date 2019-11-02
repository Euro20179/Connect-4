import pygame
import tkinter
from tkinter import messagebox as msgbox

winWidth = 500
winHeight = round(winWidth * 6/7)

win = pygame.display.set_mode((winWidth, winHeight))

r = round(winWidth * 2/49)

colors = {"empty":(0, 0, 0),
"blue":(0, 0, 255),
"red":(255, 0, 0)}

turnN = 0
rowN = [5, 5, 5, 5, 5, 5, 5]

#columns
columns = [pygame.Rect((0, 0, winWidth/7, winHeight)),
    pygame.Rect((winWidth/7, 0, winWidth/7, winHeight)),
    pygame.Rect((winWidth/7 * 2, 0, winWidth/7, winHeight)),
    pygame.Rect((winWidth/7 * 3, 0, winWidth/7, winHeight)),
    pygame.Rect((winWidth/7 * 4, 0, winWidth/7, winHeight)),
    pygame.Rect((winWidth/7 * 5, 0, winWidth/7, winHeight)),
    pygame.Rect((winWidth/7 * 6, 0, winWidth/7, winHeight))
]


#rows
rows = [
    pygame.Rect((0, 0, winWidth, winHeight/7)),
    pygame.Rect((0, winHeight/6, winWidth, winHeight/6)),
    pygame.Rect((0, winHeight/6 * 2, winWidth, winHeight/6)),
    pygame.Rect((0, winHeight/6 * 3, winWidth, winHeight/6)),
    pygame.Rect((0, winHeight/6 * 4, winWidth, winHeight/6)),
    pygame.Rect((0, winHeight/6 * 5, winWidth, winHeight/6))
]


class Main:
    def __init__(self):
        pass

    def turn1(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    Run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for column in columns:
                            if column.collidepoint(event.pos):
                                if column == columns[0]:
                                    pygame.draw.circle(win, colors["blue"], (20, round(winHeight/6 * rowN[0] + 40)), r)
                                    pygame.display.update()
                                    rowN[0] -= 1
                                    self.turn2(self)
                                if column == columns[1]:
                                    pygame.draw.circle(win, colors["blue"], (round(winWidth/7) + 20, round(winHeight/6 * rowN[1] + 40)), r)
                                    pygame.display.update()
                                    rowN[1] -= 1
                                    self.turn2(self)
                                if column == columns[2]:
                                    pygame.draw.circle(win, colors["blue"], ((round(winWidth/7 * 2) + 20, round(winHeight/6 * rowN[2] + 40))), r)
                                    pygame.display.update()
                                    rowN[2] -= 1
                                    self.turn2(self)
                                if column == columns[3]:
                                    pygame.draw.circle(win, colors["blue"], ((round(winWidth/7 * 3) + 20, round(winHeight/6 * rowN[3] + 40))), r)
                                    pygame.display.update()
                                    rowN[3] -= 1
                                    self.turn2(self)
                                if column == columns[4]:
                                    pygame.draw.circle(win, colors["blue"], ((round(winWidth/7 * 4) + 20, round(winHeight/6 * rowN[4] + 40))), r)
                                    pygame.display.update()
                                    rowN[4] -= 1
                                    self.turn2(self)
                                if column == columns[5]:
                                    pygame.draw.circle(win, colors["blue"], ((round(winWidth/7 * 5) + 20, round(winHeight/6 * rowN[5] + 40))), r)
                                    pygame.display.update()
                                    rowN[5] -= 1
                                    self.turn2(self)
                                if column == columns[6]:
                                    pygame.draw.circle(win, colors["blue"], ((round(winWidth/7 * 6) + 20, round(winHeight/6 * rowN[6] + 40))), r)
                                    pygame.display.update()
                                    rowN[6] -= 1
                                    self.turn2(self)
                            

    def turn2(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    Run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for column in columns:
                            if column.collidepoint(event.pos):
                                if column == columns[0]:
                                    pygame.draw.circle(win, colors["red"], (20, round(winHeight/6 * rowN[0] + 40)), r)
                                    pygame.display.update()
                                    rowN[0] -= 1
                                    self.turn1(self)
                                if column == columns[1]:
                                    pygame.draw.circle(win, colors["red"], (round(winWidth/7) + 20, round(winHeight/6 * rowN[1] + 40)), r)
                                    pygame.display.update()
                                    rowN[1] -= 1
                                    self.turn1(self)
                                if column == columns[2]:
                                    pygame.draw.circle(win, colors["red"], ((round(winWidth/7 * 2) + 20, round(winHeight/6 * rowN[2] + 40))), r)
                                    pygame.display.update()
                                    rowN[2] -= 1
                                    self.turn1(self)
                                if column == columns[3]:
                                    pygame.draw.circle(win, colors["red"], ((round(winWidth/7 * 3) + 20, round(winHeight/6 * rowN[3] + 40))), r)
                                    pygame.display.update()
                                    rowN[3] -= 1
                                    self.turn1(self)
                                if column == columns[4]:
                                    pygame.draw.circle(win, colors["red"], ((round(winWidth/7 * 4) + 20, round(winHeight/6 * rowN[4] + 40))), r)
                                    pygame.display.update()
                                    rowN[4] -= 1
                                    self.turn1(self)
                                if column == columns[5]:
                                    pygame.draw.circle(win, colors["red"], ((round(winWidth/7 * 5) + 20, round(winHeight/6 * rowN[5] + 40))), r)
                                    pygame.display.update()
                                    rowN[5] -= 1
                                    self.turn1(self)
                                if column == columns[6]:
                                    pygame.draw.circle(win, colors["red"], ((round(winWidth/7 * 6) + 20, round(winHeight/6 * rowN[6] + 40))), r)
                                    pygame.display.update()
                                    rowN[6] -= 1
                                    self.turn1(self)

    def game(self):
        Run = True
        turnN = 0
        #game loop
        while Run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    Run = False
                    break
            if Run:
                if turnN == 0:
                    win.fill((255, 255, 255))
                    for circle in range(7):
                        if circle == 1:
                            pygame.draw.circle(win, colors["empty"], (20, 40), r)
                        else:
                            pygame.draw.circle(win, colors["empty"], (20, round(winHeight/6 * (circle - 1) + 40)), r)
                    for circle in range(7):
                        if circle == 1:
                            pygame.draw.circle(win, colors["empty"], (round(winWidth/7) + 20, 40), r)
                        else:
                            pygame.draw.circle(win, colors["empty"], (round(winWidth/7) + 20, round(winHeight/6 * (circle - 1) + 40)), r)
                    for circle in range(7):
                        if circle == 1:
                            pygame.draw.circle(win, colors["empty"], (round(winWidth/7 * 2) + 20, 40), r)
                        else:
                            pygame.draw.circle(win, colors["empty"], (round(winWidth/7 * 2) + 20, round(winHeight/6 * (circle - 1) + 40)), r)
                    for circle in range(7):
                        if circle == 1:
                            pygame.draw.circle(win, colors["empty"], (round(winWidth/7 * 3) + 20, 40), r)
                        else:
                            pygame.draw.circle(win, colors["empty"], (round(winWidth/7 * 3) + 20, round(winHeight/6 * (circle - 1) + 40)), r)
                    for circle in range(7):
                        if circle == 1:
                            pygame.draw.circle(win, colors["empty"], (round(winWidth/7 * 4) + 20, 40), r)
                        else:
                            pygame.draw.circle(win, colors["empty"], (round(winWidth/7 * 4) + 20, round(winHeight/6 * (circle - 1) + 40)), r)
                    for circle in range(7):
                        if circle == 1:
                            pygame.draw.circle(win, colors["empty"], (round(winWidth/7 * 5) + 20, 40), r)
                        else:
                            pygame.draw.circle(win, colors["empty"], (round(winWidth/7 * 5) + 20, round(winHeight/6 * (circle - 1) + 40)), r)
                    for circle in range(7):
                        if circle == 1:
                            pygame.draw.circle(win, colors["empty"], (round(winWidth/7 * 6) + 20, 40), r)
                        else:
                            pygame.draw.circle(win, colors["empty"], (round(winWidth/7 * 6) + 20, round(winHeight/6 * (circle - 1) + 40)), r)
                    pygame.display.update()
                    turnN = 1
                else:
                    if turnN == 1:
                        self.turn1(self)
            else:
                break


main = Main
game = main.game(main)