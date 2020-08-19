# -*- coding: utf-8 -*-

from random import randint

from asciimatics.effects import Print
from asciimatics.screen import Screen
from asciimatics.particles import Explosion
from asciimatics.effects import Stars, Matrix
from asciimatics.renderers import StaticRenderer, ColourImageFile, SpeechBubble, Plasma


class Text(StaticRenderer):
    def __init__(self, text):
        super(Text, self).__init__()
        self._images = [text]


def _reset(screen):
    reset = Print(
        screen,
        SpeechBubble("Press 'r' to restart."),
        int(screen.height / 2),
        attr=Screen.A_BOLD,
    )
    return [reset]


def _base(screen, element, row, fg_color, bg_color):
    base = Print(screen, Text(element.render()), row, colour=fg_color, bg=bg_color,)

    return [base]


def _image(screen, element, row, bg_color):
    image = Print(
        screen,
        ColourImageFile(
            screen,
            element.obj["src"],
            element.size,
            bg=bg_color,
            fill_background=True,
            uni=screen.unicode_aware,
            dither=screen.unicode_aware,
        ),
        row,
    )

    return [image]


def _code(screen, element, row):
    code = Print(
        screen,
        Text(element.render()),
        row,
        colour=Screen.COLOUR_WHITE,
        bg=Screen.COLOUR_BLACK,
        transparent=False,
    )

    return [code]


def _explosions(screen):
    for _ in range(20):
        yield Explosion(
            screen,
            randint(int(screen.width * 0.2), int(screen.width - (screen.width * 0.2))),
            randint(int(screen.height * 0.2), int(screen.height - (screen.height * 0.2))),
            randint(20, 30),
            start_frame=randint(0, 250),
        )


def _stars(screen):
    return [Stars(screen, (screen.width + screen.height) // 2, stop_frame=100)]


def _matrix(screen):
    return [Matrix(screen, stop_frame=200)]


def _plasma(screen):
    return [
        Print(
            screen,
            Plasma(screen.height, screen.width, screen.colours),
            0,
            speed=1,
            transparent=False,
        )
    ]
