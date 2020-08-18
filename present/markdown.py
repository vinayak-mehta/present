# -*- coding: utf-8 -*-

import re
from dataclasses import dataclass

from pyfiglet import Figlet

from ._vendor.mistune import markdown


@dataclass
class Heading(object):
    type: str = "heading"
    obj: dict = None

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

    def render(self):
        return self.pad(self.obj["text"])


@dataclass
class Image(object):
    type: str = "image"
    obj: dict = None

    def render(self):
        raise NotImplementedError


@dataclass
class BlockHtml(object):
    type: str = "html"
    obj: dict = None

    @property
    def style(self):
        _style = [s[2] for s in re.findall(r"((\w+)='(\w+)')", self.obj["text"])][0]
        return _style

    def render(self):
        raise NotImplementedError


class Slide(object):
    def __init__(self, elements=None):
        self.elements = elements
        self.has_style = False
        self.has_code = False

        for e in elements:
            if e.type == "html":
                self.has_style = True

            if e.type == "code":
                self.has_code = True

        if self.has_style and self.has_code:
            raise ValueError("Effects and code not supported on the same slide.")

        if self.has_style:
            self.fg_color, self.bg_color = 7, 0
        else:
            self.fg_color, self.bg_color = 0, 7

    def __repr__(self):
        return f"<Slide elements={self.elements} has_style={self.has_style} fg_color={self.fg_color} bg_color={self.bg_color}>"


class Markdown(object):
    """Parse and traverse through the markdown abstract syntax tree.
    """

    def parse(self, text):
        slides = []
        ast = markdown(text, renderer="ast")

        buffer = []
        for i, obj in enumerate(ast):
            if obj["type"] in ["newline"]:
                continue

            if obj["type"] == "thematic_break" and buffer:
                slides.append(Slide(elements=buffer))
                buffer = []
                continue

            if obj["type"] == "paragraph":
                for child in obj["children"]:
                    Element = eval(child["type"].title().replace("_", ""))
                    buffer.append(Element(obj=child))
            else:
                Element = eval(obj["type"].title().replace("_", ""))
                buffer.append(Element(obj=obj))

            if i == len(ast) - 1:
                slides.append(Slide(elements=buffer))

        return slides
