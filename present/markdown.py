# -*- coding: utf-8 -*-

import os
import re
import shutil
from dataclasses import dataclass

from pyfiglet import Figlet

from ._vendor.mistune import markdown


EFFECTS = ["explosions", "stars", "matrix", "plasma"]
COLORMAP = {
    "black": 0,
    "red": 1,
    "green": 2,
    "yellow": 3,
    "blue": 4,
    "magenta": 5,
    "cyan": 6,
    "white": 7,
}


@dataclass
class Heading(object):
    type: str = "heading"
    obj: dict = None

    @property
    def size(self):
        if self.obj["level"] == 1:
            f = Figlet()
            text = self.obj["children"][0]["text"]
            return len(f.renderText(text).splitlines())
        elif self.obj["level"] == 2:
            return 2
        else:
            return 1

    def render(self):
        text = self.obj["children"][0]["text"]

        if self.obj["level"] == 1:
            f = Figlet()
            return f.renderText(text)
        elif self.obj["level"] == 2:
            return "\n".join([text, "-" * len(text)])
        else:
            return text


@dataclass
class Text(object):
    type: str = "text"
    obj: dict = None

    @property
    def size(self):
        return 1

    def render(self):
        return self.obj["text"]


@dataclass
class List(object):
    type: str = "list"
    obj: dict = None

    def walk(self, obj, text=None, level=0):
        if text is None:
            text = []

        for child in obj.get("children", []):
            if child.get("text") is not None:
                text.append((" " * 2 * level) + "• " + child["text"])

            if "children" in obj:
                self.walk(child, text=text, level=level + 1)

        return text

    @property
    def size(self):
        return len(self.walk(self.obj))

    def render(self):
        return "\n".join(self.walk(self.obj))


@dataclass
class BlockCode(object):
    type: str = "code"
    obj: dict = None

    @staticmethod
    def pad(s, fill=" "):
        lines = s.splitlines()
        max_len = max(len(l) for l in lines)
        top = bottom = " " * (max_len + 2)

        lines = [l.ljust(max_len + 1, fill) for l in lines]
        lines = [" " + l for l in lines]
        lines.insert(0, top)
        lines.append(bottom)

        return "\n".join(lines)

    @property
    def size(self):
        return len(self.obj["text"].splitlines())

    def render(self):
        return self.pad(self.obj["text"])


@dataclass(init=False)
class Image(object):
    type: str = "image"
    obj: dict = None

    def __init__(self, type: str = "image", obj: dict = None):
        self.type = type
        self.obj = obj
        if not os.path.exists(self.obj["src"]):
            raise FileNotFoundError(f"{self.obj['src']} does not exist")

    @property
    def size(self):
        # TODO: Support small, medium, large image sizes
        return int(shutil.get_terminal_size()[1] / 2)

    def render(self):
        raise NotImplementedError


@dataclass
class BlockHtml(object):
    type: str = "html"
    obj: dict = None

    @property
    def size(self):
        raise NotImplementedError

    @property
    def style(self):
        _style = re.findall(r"((\w+)=(\w+))", self.obj["text"])
        return {s[1]: s[2] for s in _style}

    def render(self):
        raise NotImplementedError


class Slide(object):
    def __init__(self, elements=None):
        self.elements = elements
        self.has_style = False
        self.has_effect = False
        self.has_code = False
        self.style = {}
        self.effect = None
        self.fg_color = 0
        self.bg_color = 7

        # TODO: style should always be the first element on a slide
        # raise error if it isn't

        for e in elements:
            if e.type == "html":
                self.has_style = True
                self.style = e.style

            if e.type == "code":
                self.has_code = True

        # TODO: support everything!

        if self.style.get("effect") is not None:
            if self.style["effect"] not in EFFECTS:
                raise ValueError(f"Effect {self.style['effect']} is not supported")
            self.has_effect = True
            self.effect = self.style["effect"]

        if self.style.get("fg") is not None:
            try:
                self.fg_color = COLORMAP[self.style["fg"]]
            except KeyError:
                raise ValueError(f"Color {self.style['fg']} is not supported")

        if self.style.get("bg") is not None:
            try:
                self.bg_color = COLORMAP[self.style["bg"]]
            except KeyError:
                raise ValueError(f"Color {self.style['bg']} is not supported")

        if self.has_effect and (
            self.style.get("fg") is not None or self.style.get("bg") is not None
        ):
            raise ValueError("Effects and colors on the same slide are not supported")

        if self.has_effect and self.has_code:
            raise ValueError("Effects and code on the same slide are not supported")

        if self.has_effect:
            self.fg_color, self.bg_color = 7, 0

    def __repr__(self):
        return f"<Slide elements={self.elements} has_style={self.has_style} has_code={self.has_code} fg_color={self.fg_color} bg_color={self.bg_color}>"


class Markdown(object):
    """Parse and traverse through the markdown abstract syntax tree.
    """

    def parse(self, text):
        slides = []
        ast = markdown(text, renderer="ast")

        sliden = 0
        buffer = []
        for i, obj in enumerate(ast):
            if obj["type"] in ["newline"]:
                continue

            if obj["type"] == "thematic_break" and buffer:
                slides.append(Slide(elements=buffer))
                sliden += 1
                buffer = []
                continue

            if obj["type"] == "paragraph":
                for child in obj["children"]:
                    try:
                        element_name = child["type"].title().replace("_", "")
                        Element = eval(element_name)
                    except NameError:
                        raise ValueError(f"(Slide {sliden + 1}) {element_name} is not supported")
                    buffer.append(Element(obj=child))
            else:
                try:
                    element_name = obj["type"].title().replace("_", "")
                    Element = eval(element_name)
                except NameError:
                    raise ValueError(f"(Slide {sliden + 1}) {element_name} is not supported")
                buffer.append(Element(obj=obj))

            if i == len(ast) - 1:
                slides.append(Slide(elements=buffer))
                sliden += 1

        return slides
