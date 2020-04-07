from ParentClasses.Actor import Actor


class DemoCar(Actor):
    xChange = 0  # Autó X koordinátájának változása
    yChange = 0  # Autó Y koordinátájának változása

    def act(self):
        # Kocsi helyzetének frissítése
        self.setPosition(self.posX + self.xChange, self.posY + self.yChange)
