from ParentClasses.Button import Button


class DemoButton(Button):
    n = 0

    def clicked(self):
        self.n += 1
        print("Klikk: " + str(self.n))

    def act(self):
        pass
