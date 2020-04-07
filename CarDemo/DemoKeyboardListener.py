import pygame

from ParentClasses.KeyboardListener import KeyboardListener


class DemoKeyboardListener(KeyboardListener):
    kocsi = None

    def __init__(self, kocsi):
        self.kocsi = kocsi

    def onKeyDown(self, event):
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:  # BALRA
            self.kocsi.xChange = -9

        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:  # JOBBRA
            self.kocsi.xChange = 9

        if event.key == pygame.K_DOWN or event.key == pygame.K_s:  # LE
            self.kocsi.yChange = 9

        if event.key == pygame.K_UP or event.key == pygame.K_w:  # FEL
            self.kocsi.yChange = -9

    def onKeyUp(self, event):
        # Ha nem nyomjuk az irányító gombokat, akkor nullázódjon le a mozgatás
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
            self.kocsi.xChange = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
            self.kocsi.yChange = 0
