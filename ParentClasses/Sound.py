import pygame


class Sound:
    path = ""

    def __init__(self, path):
        self.path = path

    def play(self):
        pygame.mixer.Sound.play(pygame.mixer.Sound(self.path))

    def setSound(self, path):
        self(path)
