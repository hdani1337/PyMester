import pygame


class Display:
    gameName = ""
    displayWidth = 800  # Az ablak szélessége
    displayHeight = 600  # Az ablak magassága
    global display  # Az ablak

    fps = pygame.time.Clock()

    # Új ablak létrehozása, alapértelmezetten 800x600-as felbontással
    def __init__(self):
        pygame.display.set_caption(self.gameName)  # Ablak címe
        self.display = pygame.display.set_mode((self.displayWidth, self.displayHeight)) # Ablak létrehozása

    # Úgy hozzuk létre az ablakot, hogy paraméterben megadjuk a méreteit
    def __init__(self, displayWidth, displayHeight):
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        pygame.display.set_caption(self.gameName)  # Ablak címe
        self.display = pygame.display.set_mode((self.displayWidth, self.displayHeight))  # Ablak létrehozása

    # Ablak ikonjának módosítása
    # @param path: Az ikon elérési útja
    def setIcon(self, path):
        pygame.display.set_icon(pygame.image.load(path))

    # Ablak címének módosítása
    def setTitle(self, title):
        self.gameName = title
        pygame.display.set_caption(self.gameName)
