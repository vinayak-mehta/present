# -*- coding: utf-8 -*-

from random import randint

from asciimatics.effects import Print
from asciimatics.screen import Screen
from asciimatics.particles import Explosion
from asciimatics.effects import Stars, Matrix
from asciimatics.renderers import StaticRenderer, ColourImageFile, SpeechBubble


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


def _base(screen, element, height_factor, line_height, fg_color, bg_color):
    if element.type == "heading":
        if element.obj["level"] == 1:
            height_factor = 6
        else:
            height_factor = 4

    base = Print(
        screen,
        Text(element.render()),
        int(
            screen.height / 2 - (height_factor * line_height)
        ),
        colour=fg_color,
        bg=bg_color,
    )
    return [base]


def _image(screen, element, height_factor, line_height, bg_color):
    image = Print(
        screen,
        ColourImageFile(
            screen,
            element.obj["src"],
            int(screen.height / 2),
            bg=bg_color,
            fill_background=True,
            uni=screen.unicode_aware,
            dither=screen.unicode_aware,
        ),
        int(
            screen.height / 2 - (height_factor * line_height)
        ),
    )
    return [image]


def _code(screen, element, height_factor, line_height):
    code = Print(
        screen,
        Text(element.render()),
        int(
            screen.height / 2 - (height_factor * line_height)
        ),
        colour=Screen.COLOUR_WHITE,
        bg=Screen.COLOUR_BLACK,
        transparent=False,
    )
    return [code]


def _explosions(screen):
    for _ in range(20):
        yield Explosion(
            screen,
            randint(3, screen.width - 4),
            randint(1, screen.height - 2),
            randint(20, 30),
            start_frame=randint(0, 250),
        )


def _matrix(screen):
    return [Matrix(screen, stop_frame=200)]


def _stars(screen):
    return [Stars(screen, (screen.width + screen.height) // 2, stop_frame=100)]
