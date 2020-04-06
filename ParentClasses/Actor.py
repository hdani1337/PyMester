from abc import abstractmethod

import pygame


class Actor:
    sprite = None
    display = None
    posX = 0  # X koordináta
    posY = 0  # Y koordináta
    width = 0  # Szélesség pixelekben
    height = 0  # Magasság pixelekben

    def __init__(self, display, spritePath):
        self.display = display
        self.sprite = pygame.image.load(spritePath)

    # Textúra átállítása
    def setTexture(self, spritePath):
        self.sprite = pygame.image.load(spritePath)

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

    # Kirajzolás a képernyőre
    def show(self):
        self.act()
        self.display.display.blit(self.sprite,(self.posX,self.posY))

    # Minden képfrissítésnél lefut
    @abstractmethod
    def act(self):
        ...