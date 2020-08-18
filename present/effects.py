# -*- coding: utf-8 -*-

from random import randint

from asciimatics.particles import Explosion


def explosions(screen):
    for _ in range(20):
        yield Explosion(
            screen,
            randint(3, screen.width - 4),
            randint(1, screen.height - 2),
            randint(20, 30),
            start_frame=randint(0, 250),
        )
