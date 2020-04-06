import pygame


class MouseListener:
    onHover = False
    onClick = False

    delta = 0.0

    def update(self, actorWidth, actorHeight, actorX, actorY):
        # Rajt az egér az actoron
        if actorX + actorWidth > pygame.mouse.get_pos()[0] > actorX and actorY + actorHeight > pygame.mouse.get_pos()[1] > actorY:
            self.onHover = True

            # Kell egy kis késleltetés a nyomvatartás miatt
            if self.delta < 0.3:
                # Rá is kattintottak
                if pygame.mouse.get_pressed()[0] == 1:
                    self.onClick = True
                    self.delta += 0.3
            else:
                if pygame.mouse.get_pressed()[0] == 0:
                    self.onClick = False
                    self.delta = 0

        else:
            self.onHover = False
