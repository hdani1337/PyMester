from abc import abstractmethod


class Game:

    # Végtelenciklus előtt fut le
    @abstractmethod
    def beforeRun(self):
        ...

    # Képfrissítés előtt fut le
    @abstractmethod
    def beforeUpdate(self):
        ...

    # Képfrissítés
    @abstractmethod
    def update(self):
        ...

    # Képfrissítés után fut le
    @abstractmethod
    def afterUpdate(self):
        ...

    # Végtelenciklus
    def run(self):
        try:
            self.beforeRun()
        except AttributeError:
            print("[Game] BeforeRun absztrakt metódus nincs kifejtve!")

        while True:
            try:
                self.beforeUpdate()
            except AttributeError:
                print("[Game] BeforeUpdate absztrakt metódus nincs kifejtve!")
            try:
                self.update()
            except AttributeError:
                print("[Game] Update absztrakt metódus nincs kifejtve!")
            try:
                self.afterUpdate()
            except AttributeError:
                print("[Game] AfterUpdate absztrakt metódus nincs kifejtve!")
