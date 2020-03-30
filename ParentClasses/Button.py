from abc import abstractmethod

import pygame

import Display
from MouseListener import MouseListener


class Button:

    #Változók

    fontPath = "pygame/calibrib.ttf" #Font elérési útja
    text = "" #Gomb szövege
    posX = 0 #X koordináta
    posY = 0 #Y koordináta
    width = 0 #Szélesség pixelekben
    height = 0 #Magasság pixelekben
    color = (200,200,200) #A gomb alapértelmezett színe (RGB skálán, ez például nem olyan fehér)
    color_hover = (255,255,255) #A gomb színe, ha rajta van az egér (RGB skálán, ez például fehér)
    font_color = (0,0,0) #A betű színe, alapértelmezetten fekete
    font_size = 18 #A betű mérete, alapértelmezetten 18
    mousePosition = pygame.mouse.get_pos() #Kurzor pontos koordinátái
    mouseClick = pygame.mouse.get_pressed() #Kurzos kattintása, hasonló mint a ClickListener
    mouseListener = MouseListener()

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
        self.mouseListener.update(self.width,self.height,self.posX,self.posY)
        if self.mouseListener.onHover:
            # Rajt van a kurzor
            pygame.draw.rect(Display.display, self.color_hover, (self.posX, self.posY, self.width, self.height))

            # Rá is kattintottak
            if self.mouseListener.onClick:
                self.clicked()

        else:
            # Nincs rajt a kurzor
            pygame.draw.rect(Display.display, self.color, (self.posX, self.posY, self.width, self.height))

        font = pygame.font.Font(self.fontPath, self.font_size)
        textSurface, textBox = self.getTextSurface(self.text, font)
        textBox.center = ((self.posX + (self.width / 2)), (self.posY + (self.height / 2)))
        Display.display.blit(textSurface, textBox)

    # Klikkesedésnél fut le
    @abstractmethod
    def clicked(self):
        ...

    # Minden képfrissítésnél lefut
    @abstractmethod
    def act(self):
        ...


