import pygame


class MouseListener:
    onHover = False
    onClick = False


    def update(self, actorWidth, actorHeight, actorX, actorY):
        # Rajt az egér az actoron
        if actorX + actorWidth > pygame.mouse.get_pos()[0] > actorX and actorY + actorHeight > pygame.mouse.get_pos()[1] > actorY:
            self.onHover = True

            # Rá is kattintottak
            if pygame.mouse.get_pressed()[0] == 1:
                self.onClick = True
            else:
                self.onClick = False

        else:
            self.onHover = False
