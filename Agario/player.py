from pygame.math import Vector2, Vector3


class Player:
    def __init__(self):
        self.taille
        self.vitesse
        self.forme
        self.position = Vector2(155, 200)
        self.direction = Vector2(155, 200)
        self.couleur = Vector3(155, 200, 100)

    def manger(self):
        self.manger = self.manger +1

    def mourir(self):
        pass

    def deplacer(self):
        pass
