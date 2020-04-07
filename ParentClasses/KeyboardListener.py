from abc import abstractmethod

import pygame


class KeyboardListener:
    @abstractmethod
    def onKeyDown(self, event):
        ...

    @abstractmethod
    def onKeyUp(self, event):
        ...

    # Frissítés
    def listen(self):
        # Ez a ciklus csak egy helyen futhat a programban, ezért hoztam létre neki külön osztályt
        for event in pygame.event.get():
            # Ha a játékos kiakar lépni, engedjük neki
            if event.type == pygame.QUIT:
                pygame.quit()  # Álljon le a program
                quit()  # És záródjon be az ablak

            # Billentyű lenyomásakor ez fut le
            if event.type == pygame.KEYDOWN:
                self.onKeyDown(event)

            # Billentyű elengedésekor ez fut le
            if event.type == pygame.KEYUP:
                self.onKeyUp(event)
