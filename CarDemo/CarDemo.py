import pygame

from ParentClasses.Actor import Actor
from ParentClasses.Display import Display

display = Display(800, 600) # Képeernyő egy alap felbontással
kocsi = Actor(display, 'car.png') # Kocsi, egyszerű actor példány


def game():
    xChange = 0 # Autó X koordinátájának változása
    yChange = 0 # Autó Y koordinátájának változása

    #Végtelen ciklus
    while True:
        #Események vizsgálása
        for event in pygame.event.get():
            #Ha a játékos kiakar lépni, engedjük neki
            if event.type == pygame.QUIT:
                pygame.quit()  # Álljon le a program
                quit()  # És záródjon be az ablak

            #Ha a játékos lenyom egy billentyűt
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:#BALRA
                    xChange = -9

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:#JOBBRA
                    xChange = 9

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:#LE
                    yChange = 9

                if event.key == pygame.K_UP or event.key == pygame.K_w:#FEL
                    yChange = -9

            #Ha a játékos elenged egy billentyűt
            if event.type == pygame.KEYUP:
                # Ha nem nyomjuk az irányító gombokat, akkor nullázódjon le a mozgatás
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    xChange = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    yChange = 0

        # Kocsi helyzetének frissítése és képfrissítés
        kocsi.setPosition(kocsi.posX + xChange, kocsi.posY + yChange)
        update()


def update():
    display.display.fill((0, 0, 0))  # Minden egyes alkalommal teljesen kiürítjül a képernyőt fekete színnel, hogy ne maradjanak ott az autó előző pozíciói
    kocsi.show() # Rajzoljuk ki az autót
    pygame.display.update()  # Frissítjuk a képet
    display.fps.tick(60)  # Másodpercenkénti képfrissítés száma


display.setTitle("PyMester Demo") # Ablak címének átállítása
game() # Meghívjuk a game metódust, ami a végtelen ciklus miatt addig fut amíg le nem állítjuk a programot
