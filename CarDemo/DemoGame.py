import pygame

from CarDemo.DemoCar import DemoCar
from CarDemo.DemoButton import DemoButton
from ParentClasses.Display import Display
from ParentClasses.Game import Game
from ParentClasses.Label import Label

pygame.init()

display = Display(800, 600)  # Képeernyő egy alap felbontással
kocsi = DemoCar(display, 'car.png')  # Kocsi, egyszerű actor példány
gomb = DemoButton(display, "Nyomj meg!")
szoveg = Label(display, "Teszt")


class TesztGame(Game):
    xChange = 0  # Autó X koordinátájának változása
    yChange = 0  # Autó Y koordinátájának változása

    def beforeRun(self):
        pass

    def beforeUpdate(self):

        # Események vizsgálása a képfrissítés előtt
        for event in pygame.event.get():
            # Ha a játékos kiakar lépni, engedjük neki
            if event.type == pygame.QUIT:
                pygame.quit()  # Álljon le a program
                quit()  # És záródjon be az ablak

            # Ha a játékos lenyom egy billentyűt
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:  # BALRA
                    self.xChange = -9

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:  # JOBBRA
                    self.xChange = 9

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:  # LE
                    self.yChange = 9

                if event.key == pygame.K_UP or event.key == pygame.K_w:  # FEL
                    self.yChange = -9

            # Ha a játékos elenged egy billentyűt
            if event.type == pygame.KEYUP:
                # Ha nem nyomjuk az irányító gombokat, akkor nullázódjon le a mozgatás
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    self.xChange = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    self.yChange = 0

        # Kocsi helyzetének frissítése és képfrissítés
        kocsi.setPosition(kocsi.posX + self.xChange, kocsi.posY + self.yChange)

    def update(self):
        display.display.fill((0, 0,
                              0))  # Minden egyes alkalommal teljesen kiürítjül a képernyőt fekete színnel, hogy ne maradjanak ott az autó előző pozíciói
        kocsi.show()  # Rajzoljuk ki az autót
        gomb.show()
        szoveg.show()
        pygame.display.update()  # Frissítjuk a képet
        display.fps.tick(60)  # Másodpercenkénti képfrissítés száma

    def afterUpdate(self):
        pass


szoveg.setPosition(100, 200)
game = TesztGame()
game.run()
