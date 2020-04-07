from abc import abstractmethod


class Game:

    # Végtelenciklus előtt fut le
    @abstractmethod
    def beforeRun(self):
        raise NotImplementedError

    # Képfrissítés előtt fut le
    @abstractmethod
    def beforeUpdate(self):
        raise NotImplementedError

    # Képfrissítés
    @abstractmethod
    def update(self):
        raise NotImplementedError

    # Képfrissítés után fut le
    @abstractmethod
    def afterUpdate(self):
        raise NotImplementedError

    # Végtelenciklus
    def run(self):
        try:
            self.beforeRun()
        except NotImplementedError:
            print("[Game] BeforeRun absztrakt metódus nincs kifejtve!")

        while True:
            try:
                self.beforeUpdate()
            except NotImplementedError:
                print("[Game] BeforeUpdate absztrakt metódus nincs kifejtve!")
            try:
                self.update()
            except NotImplementedError:
                print("[Game] Update absztrakt metódus nincs kifejtve!")
            try:
                self.afterUpdate()
            except NotImplementedError:
                print("[Game] AfterUpdate absztrakt metódus nincs kifejtve!")
