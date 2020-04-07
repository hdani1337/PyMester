import pygame

from CarDemo.DemoCar import DemoCar
from CarDemo.DemoButton import DemoButton
from CarDemo.DemoKeyboardListener import DemoKeyboardListener
from ParentClasses.Display import Display
from ParentClasses.Game import Game
from ParentClasses.Label import Label

pygame.init()  # Pygame inicializálása, ez a lépés kötelező


class DemoGame(Game):
    display = Display(800, 600)  # Képernyő egy alap felbontással
    kocsi = DemoCar(display, 'car.png')  # Kocsi példány
    gomb = DemoButton(display, "Nyomj meg!")  # Gomb példány
    szoveg = Label(display, "Teszt Szöveg")  # Label példány

    keyboardListener = DemoKeyboardListener(kocsi)  # Billentyűk leütésének figyelője

    def beforeRun(self):
        pass

    def beforeUpdate(self):
        pass

    def update(self):
        self.display.display.fill((0, 0,
                                   0))  # Minden egyes alkalommal teljesen kiürítjük a képernyőt fekete színnel, hogy ne maradjanak ott az autó előző pozíciói
        self.keyboardListener.listen()  # Billentyűleütések figyelése, csak utána rajzolunk ki mindent
        self.kocsi.show()  # Rajzoljuk ki az autót
        self.gomb.show()  # Rajzoljuk ki a gombot
        self.szoveg.show()  # Rajzoljuk ki a labelt
        self.display.fps.tick(60)  # Másodpercenkénti képfrissítés száma
        pygame.display.update()  # Frissítjuk a képet

    def afterUpdate(self):
        pass


def setPositions(game):
    game.szoveg.setToCenter()


def init():
    game = DemoGame()
    setPositions(game)
    game.run()


init()  # A program elkezdése
