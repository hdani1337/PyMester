import pygame

import Game


class Button:

    #Változók

    text = "" #Gomb szövege
    posX = 0 #X koordináta
    posY = 0 #Y koordináta
    width = 0 #Szélesség pixelekben
    height = 0 #Magasság pixelekben
    color = (200,200,200) #A gomb alapértelmezett színe (RGB skálán, ez például nem olyan fehér)
    color_hover = (255,255,255) #A gomb színe, ha rajta van az egér (RGB skálán, ez például fehér)
    mousePosition = pygame.mouse.get_pos() #Kurzor pontos koordinátái
    mouseClick = pygame.mouse.get_pressed() #Kurzos kattintása, hasonló mint a ClickListener

    global clicked #True értéket vesz fel ha rákattintottak

    #Konstruktorok

    # A gomb szövegét adjuk csak meg, alapértelmezett pozíció a (0,0), alapértelmezett méret a (100,50), alapértelmezett színek
    def __init__(self, text):
        self.text = text
        self.posX = 0
        self.posY = 0
        self.width = 100
        self.height = 50
        self.color = (255,255,255)
        self.color_hover = (200,200,200)

    # Átadjuk a gomb szövegét és pozícióját, többi alapértelmezett érték
    def __init__(self, text, posX, posY):
        self.text = text
        self.posX = posX
        self.posY = posY
        self.width = 100
        self.height = 50
        self.color = (200, 200, 200)
        self.color_hover = (255, 255, 255)

    # Átadjuk a gomb szövegét, pozícióját és méretét, a színek alapértelmezettek
    def __init__(self, text, posX, posY, width, height):
        self.text = text
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.color = (200, 200, 200)
        self.color_hover = (255, 255, 255)

    # Átadjuk a gomb szövegét, pozícióját, méretét és alapszínét, a hover szín alapértelmezett
    def __init__(self, text, posX, posY, width, height, color):
        self.text = text
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.color = color
        self.color_hover = (255, 255, 255)

    # Minden értéket átadunk
    def __init__(self, text, posX, posY, width, height, color, color_hover):
        self.text = text
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.color = color
        self.color_hover = color_hover

    #Metódusok

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

    # Kirajzolás a képernyőre, minden alkalommal megkell hívni
    def show(self):
        if self.posX + self.width > self.mousePosition[0] > self.posX and self.posY + self.height > self.mousePosition[1] > self.posY:
            # Rajt van a kurzor
            pygame.draw.rect(Game.display, self.color_hover, (self.posX, self.posY, self.width, self.height))

            # Rá is kattintottak
            if self.mouseClick[0] == 1: self.clicked = True

        else:
            # Nincs rajt a kurzor
            pygame.draw.rect(Game.display, self.color, (self.posX, self.posY, self.width, self.height))


