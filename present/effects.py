# -*- coding: utf-8 -*-

from random import randint

from asciimatics.particles import Explosion
from asciimatics.effects import Stars, Matrix


def explosions(screen):
    for _ in range(20):
        yield Explosion(
            screen,
            randint(3, screen.width - 4),
            randint(1, screen.height - 2),
            randint(20, 30),
            start_frame=randint(0, 250),
        )


def matrix(screen):
    return [Matrix(screen, stop_frame=200)]


def stars(screen):
    return [Stars(screen, (screen.width + screen.height) // 2, stop_frame=100)]
