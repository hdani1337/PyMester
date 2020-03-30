import pygame


class MusicPlayer:
    path = ""

    def __init__(self, path):
        self.path = path
        pygame.mixer.music.load(self.path)

    def play(self):
        pygame.mixer.music.play()

    def changeMusic(self, path):
        self(path)