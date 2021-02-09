from pygame.math import Vector3, Vector2


class Bille:
    def __init__(self):
        self.vitesse = 10
        self.taille = 10
        self.couleur = Vector3(155, 100, 155)
        self.direction = Vector2(155, 200)
        self.position = Vector2(155, 200)

    def suivre(self):
        pass

    def mourir(self):
        pass

    def manger(self):
        pass

    def afficher(self):
        pass
