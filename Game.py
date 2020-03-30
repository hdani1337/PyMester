import pygame


class Game:
    gameName = ""
    displayWidth = 800  # Az ablak szélessége
    displayHeight = 600  # Az ablak magassága
    global display  # Az ablak

    fps = pygame.time.Clock()

    def __init__(self):
        pygame.display.set_caption(self.gameName)  # Ablak címe
        display = pygame.display.set_mode((self.displayWidth, self.displayHeight))  # Ablak mérete

    # Ablak ikonjának módosítása
    # @param path: Az ikon elérési útja
    def setIcon(self, path):
        pygame.display.set_icon(pygame.image.load(path))

    # Ablak címének módosítása
    def setTitle(self, title):
        self.gameName = title
        pygame.display.set_caption(self.gameName)
