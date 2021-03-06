import os
from abc import abstractmethod
from pathlib import Path

import pygame

from ParentClasses.MouseListener import MouseListener


class Button:
    # Változók

    display = None  # Képernyő
    font = None
    text = ""  # Gomb szövege
    posX = 0  # X koordináta
    posY = 0  # Y koordináta
    width = 0  # Szélesség pixelekben
    height = 0  # Magasság pixelekben
    color = None  # A gomb alapértelmezett színe (RGB skálán, ez például nem olyan fehér)
    color_hover = None  # A gomb színe, ha rajta van az egér (RGB skálán, ez például fehér)
    font_color = None  # A betű színe, alapértelmezetten fekete
    font_size = 18  # A betű mérete, alapértelmezetten 18
    mouseListener = None

    def __init__(self, display, text="", posX=0, posY=0, width=100, height=50, color=(255, 255, 255), color_hover=(200, 200, 200), font_color=(0, 0, 0)):
        self.display = display
        self.text = text
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.color = color
        self.color_hover = color_hover
        self.font_color = font_color
        self.initMouse()

    # Metódusok

    def initMouse(self):
        if self.display is not None:
            self.mouseListener = MouseListener()

    # Új pozíció beállítása
    def setPosition(self, posX, posY):
        self.posX = posX
        self.posY = posY

    # Új pozíció beállítása az X tengelyen
    def setX(self, posX):
        self.setPosition(posX, self.posY)

    # Új pozíció beállítása az Y tengelyen
    def setY(self, posY):
        self.setPosition(self.posX, posY)

    # Új méret beállítása pixelben
    def setSize(self, width, height):
        self.width = width
        self.height = height

    # Szélesség módosítása
    def setWidth(self, width):
        self.setSize(width, self.height)

    # Magasság módosítása
    def setHeight(self, height):
        self.setSize(self.width, height)

    # Betűszín módosítása
    def setFontColor(self, color):
        self.font_color = color

    def setFontSize(self, size):
        self.font_size = size

    # Gomb betűtípusának módosítása
    def setFont(self, fontPath):
        self.font = pygame.font.Font(fontPath, 18)

    def getTextSurface(self, text, font):
        textSurface = font.render(text, True, self.font_color)
        return textSurface, textSurface.get_rect()

    # Kirajzolás a képernyőre, minden alkalommal megkell hívni
    def show(self):
        self.act()
        self.mouseListener.update(self.width, self.height, self.posX, self.posY)
        if self.mouseListener.onHover:
            # Rajt van a kurzor
            pygame.draw.rect(self.display.display, self.color_hover, (self.posX, self.posY, self.width, self.height))

            # Rá is kattintottak
            if self.mouseListener.onClick:
                try:
                    self.clicked()
                    self.mouseListener.onClick = False
                except NotImplementedError:
                    print("[Button] Click absztrakt metódus nincs kifejtve!")

        else:
            # Nincs rajt a kurzor
            pygame.draw.rect(self.display.display, self.color, (self.posX, self.posY, self.width, self.height))

        self.font = pygame.font.Font(self.fontPath(), self.font_size)
        textSurface, textBox = self.getTextSurface(self.text, self.font)
        textBox.center = ((self.posX + (self.width / 2)), (self.posY + (self.height / 2)))
        self.display.display.blit(textSurface, textBox)

    @staticmethod
    def fontPath():
        path = str(Path(os.getcwd()).parent) + '/ParentClasses/assets/calibrib.ttf'
        while path.__contains__("\\"):
            path = path.replace("\\", "/")
        return path

    # Klikkesedésnél fut le
    @abstractmethod
    def clicked(self):
        raise NotImplementedError

    # Minden képfrissítésnél lefut
    @abstractmethod
    def act(self):
        ...
