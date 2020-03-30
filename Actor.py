from abc import abstractmethod

import pygame
import Display


class Actor:
    sprite = ""
    posX = 0  # X koordináta
    posY = 0  # Y koordináta
    width = 0  # Szélesség pixelekben
    height = 0  # Magasság pixelekben

    def __init__(self, spritePath):
        self.sprite = pygame.image.load(spritePath)

    # Textúra átállítása
    def setTexture(self, spritePath):
        self.sprite = pygame.image.load(spritePath)

    # Kirajzolás a képernyőre
    def show(self):
        self.act()
        Display.display.blit(self.sprite,(self.posX,self.posY))

    # Minden képfrissítésnél lefut
    @abstractmethod
    def act(self):
        ...