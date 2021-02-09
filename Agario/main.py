from Agario.bille import Bille
from Agario.creep import Creep
from Agario.player import Player
from p5 import core

#variable global
joueur1 = Player()

creep1 = []

def setup():

    print("Setup START---------")
    core.WINDOW_SIZE = [400, 400]

    for i in range(0,1000):
        creep1.append(Creep())

    global joueur1
    joueur1 = Player()


    print("Setup END-----------")


def run():
    print("running")

    for d in creep1:
        d.afficher(core)

    if core.getMouseLeftClick() is not None:
        joueur1.deplacer(core.getMouseLeftClick())


if __name__ == "__main__":
    core.main(setup, run)