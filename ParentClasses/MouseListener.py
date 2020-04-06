import pygame


class MouseListener:
    mousePosition = ""  # Kurzor pontos koordinátái
    mouseClick = ""  # Kurzos kattintása, hasonló mint a ClickListener

    onHover = False
    onClick = False

    def __init__(self):
        self.mousePosition = pygame.mouse.get_pos()
        self.mouseClick = pygame.mouse.get_pressed()

    def update(self, actorWidth, actorHeight, actorX, actorY):
        self.mousePosition = pygame.mouse.get_pos()
        self.mouseClick = pygame.mouse.get_pressed()
        # Rajt az egér az actoron
        if actorX + actorWidth > self.mousePosition[0] > actorX and actorY + actorHeight > self.mousePosition[1] > actorY:
            self.onHover = True

            # Rá is kattintottak
            if self.mouseClick[0] == 1:
                self.onClick = True
            else:
                self.onClick = False

        else:
            self.onHover = False
