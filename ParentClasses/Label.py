import os
from pathlib import Path

import pygame


class Label:
    display = None
    text = ""
    textRenderer = None
    posX = 0
    posY = 0
    fontSize = 18
    color = (255, 255, 255)

    # Üres szöveg, 18-as betűméret fehér színnel, (0,0) pozíció
    def __init__(self, display, text=""):
        self.text = text
        path = str(Path(os.getcwd()).parent) + '/ParentClasses/assets/calibrib.ttf'
        while path.__contains__("\\"):
            path = path.replace("\\", "/")
        font = pygame.font.Font(path, self.fontSize)
        self.textRenderer = font.render(self.text, True, (255, 255, 255))
        self.display = display

    # Label szövegének módosítása
    def setText(self, text):
        path = str(Path(os.getcwd()).parent) + '/ParentClasses/assets/calibrib.ttf'
        while path.__contains__("\\"):
            path = path.replace("\\", "/")
        font = pygame.font.Font(path, self.fontSize)
        self.textRenderer = font.render(text, True, (255, 255, 255))
        self.text = text

    # Label méretét visszaadja pixelekben
    def getWidth(self):
        return self.fontSize * len(self.text)/2

    # Label betűtípusának módosítása
    def setFont(self, fontPath):
        font = pygame.font.Font(fontPath, 18)
        self.textRenderer = font.render(self.text, True, (255, 255, 255))

    # Új pozíció beállítása
    def setPosition(self, posX, posY):
        self.posX = posX
        self.posY = posY

    # Középre állítás
    def setToCenter(self):
        self.setPosition(self.display.displayWidth / 2 - self.getWidth() / 2, self.display.displayHeight / 2 - self.fontSize / 2)

    # Középre helyezés horizontálisan (X tengelyen)
    def setToCenterHorizontally(self):
        self.setX(self.display.displayWidth / 2 - self.getWidth() / 2)

    # Középre helyezés vertikálisan (Y tengelyen)
    def setToCenterVertically(self):
        self.setY(self.display.displayHeight / 2 - self.fontSize / 2)

    # Új pozíció beállítása az X tengelyen
    def setX(self, posX):
        self.setPosition(posX, self.posY)

    # Új pozíció beállítása az Y tengelyen
    def setY(self, posY):
        self.setPosition(self.posX, posY)

    # Kirajzolás a képernyőre, minden alkalommal megkell hívni
    def show(self):
        self.display.display.blit(self.textRenderer, (self.posX, self.posY))
