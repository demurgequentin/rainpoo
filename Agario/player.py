import random

import pygame
from pygame.math import Vector2, Vector3

from p5 import core


class Player:
    def __init__(self):
        self.taille = random.randint(8, 50)
        self.vitesse = 10
        self.forme = "rond"
        self.position = Vector2(155, 200)
        self.direction = Vector2(155, 200)
        self.couleur = Vector3(155, 200, 100)

    def manger(self):
        pass

    def mourir(self):
        pass

    def deplacer(self,position):
        self.position.x = position[0]
        self.position.y = position[1]

    def afficher(self):
        if self.forme == "rond":
            pygame.draw.circle(core.screen, (int(self.couleur.x), int(self.couleur.y), int(self.couleur.z)), (int(self.position.x), int(self.position.y)), self.taille)

