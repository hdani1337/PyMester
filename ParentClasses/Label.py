import pygame


class Label:
    display = None
    text = ""
    textRenderer = ""
    posX = 0
    posY = 0
    color = (255, 255, 255)

    # Üres szöveg, 18-as betűméret fehér színnel, (0,0) pozíció
    def __init__(self, display, text=""):
        self.text = text
        font = pygame.font.Font('E:/Python/Mester/ParentClasses/assets/calibrib.ttf', 18)
        self.textRenderer = font.render(self.text, True, (255, 255, 255))
        self.display = display

    # Label szövegének módosítása
    def setText(self, text):
        font = pygame.font.Font('E:/Python/Mester/ParentClasses/assets/calibrib.ttf', 18)
        self.textRenderer = font.render(text, True, (255, 255, 255))
        self.text = text

    # Label betűtípusának módosítása
    def setFont(self, fontPath):
        font = pygame.font.Font(fontPath, 18)
        self.textRenderer = font.render(self.text, True, (255, 255, 255))

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

    # Kirajzolás a képernyőre, minden alkalommal megkell hívni
    def show(self):
        self.display.display.blit(self.textRenderer, (self.posX, self.posY))
