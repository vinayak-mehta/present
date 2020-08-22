# -*- coding: utf-8 -*-

from random import randint

from asciimatics.effects import Print
from asciimatics.screen import Screen
from asciimatics.particles import Explosion
from asciimatics.effects import Stars, Matrix
from asciimatics.renderers import (
    StaticRenderer,
    ColourImageFile,
    SpeechBubble,
    DynamicRenderer,
    Plasma,
)


EFFECTS = ["explosions", "stars", "matrix", "plasma"]
COLORMAP = {
    "black": Screen.COLOUR_BLACK,
    "red": Screen.COLOUR_RED,
    "green": Screen.COLOUR_GREEN,
    "yellow": Screen.COLOUR_YELLOW,
    "blue": Screen.COLOUR_BLUE,
    "magenta": Screen.COLOUR_MAGENTA,
    "cyan": Screen.COLOUR_CYAN,
    "white": Screen.COLOUR_WHITE,
}


class Text(StaticRenderer):
    def __init__(self, text):
        super(Text, self).__init__()
        self._images = [text]


class Codio(DynamicRenderer):
    def __init__(self, code=None, height=100, width=100):
        super(Codio, self).__init__(height, width)
        self._code = code
        self._height = height
        self._width = width
        self._state = {
            i: {"len": 0, "start": False, "end": False} for i in range(len(code))
        }

    def _get_code(self, i):
        if self._state.get(i - 1) is None:
            self._state[i]["start"] = True

        if self._code[i]["in"]:
            if self._state[i]["len"] == len(self._code[i]["in"]):
                self._state[i]["end"] = True
                return self._code[i]["in"], self._code[i]["out"]

            if self._state.get(i - 1) is not None and not self._state[i - 1]["end"]:
                return None, None
            else:
                c = self._code[i]["in"][: self._state[i]["len"]]
                self._state[i]["len"] += 1
                return c, None

        if not self._code[i]["in"] and self._code[i]["out"]:
            if self._state.get(i - 1) is not None and not self._state[i - 1]["end"]:
                return None, None
            else:
                self._state[i]["end"] = True
                return None, self._code[i]["out"]

    def _render_now(self):
        x = y = 1

        for i, c in enumerate(self._code):
            kwargs = {}

            if self._code[i].get("color") is not None:
                kwargs.update({"colour": COLORMAP[self._code[i]["color"]]})

            if self._code[i].get("bold") is not None and self._code[i]["bold"]:
                kwargs.update({"attr": Screen.A_BOLD})

            if (
                self._code[i].get("underline") is not None
                and self._code[i]["underline"]
            ):
                kwargs.update({"attr": Screen.A_UNDERLINE})

            inp, out = self._get_code(i)
            if inp is not None:
                prompt = self._code[i]["prompt"]
                if prompt:
                    self._write(f"{prompt} {inp}", x, y, **kwargs)
                else:
                    self._write(f"{inp}", x, y, **kwargs)
                y += 1
            if out is not None and out:
                # colour=Screen.COLOUR_GREEN, attr=Screen.A_BOLD
                self._write(out, x, y, **kwargs)
                y += 1

        return self._plain_image, self._colour_map


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


def _codio(screen, element, row):
    codio = Print(
        screen,
        Codio(code=element.render(), width=element.width, height=element.size),
        row,
        colour=Screen.COLOUR_WHITE,
        bg=Screen.COLOUR_BLACK,
        transparent=False,
        speed=element.speed,
    )

    return [codio]


def _explosions(screen):
    for _ in range(20):
        yield Explosion(
            screen,
            randint(int(screen.width * 0.2), int(screen.width - (screen.width * 0.2))),
            randint(
                int(screen.height * 0.2), int(screen.height - (screen.height * 0.2))
            ),
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
