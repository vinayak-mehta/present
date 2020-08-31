# -*- coding: utf-8 -*-

import os
import re
import sys
import shutil
import warnings
from dataclasses import dataclass

import yaml
from pyfiglet import Figlet
from mistune import markdown

from .effects import COLORS, EFFECTS


@dataclass
class Heading(object):
    type: str = "heading"
    obj: dict = None
    fg: int = 0
    attr: int = 2  # Screen.A_NORMAL
    normal: int = 2  # Screen.A_NORMAL
    bg: int = 7

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
class List(object):
    type: str = "list"
    obj: dict = None
    fg: int = 0
    attr: int = 2  # Screen.A_NORMAL
    normal: int = 2  # Screen.A_NORMAL
    bg: int = 7

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
    fg: int = 0
    attr: int = 2  # Screen.A_NORMAL
    normal: int = 2  # Screen.A_NORMAL
    bg: int = 7

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


@dataclass
class Codio(object):
    type: str = "codio"
    obj: dict = None
    fg: int = 0
    attr: int = 2  # Screen.A_NORMAL
    normal: int = 2  # Screen.A_NORMAL
    bg: int = 7

    @property
    def speed(self):
        _speed = self.obj["speed"]

        if _speed < 1:
            warnings.warn("Codio speed < 1, setting it to 1")
            _speed = 1
        elif _speed > 10:
            warnings.warn("Codio speed > 10, setting it to 10")
            _speed = 10

        return 11 - _speed

    @property
    def width(self):
        _width = 0
        _terminal_width = int(shutil.get_terminal_size()[0] / 4)

        for l in self.obj["lines"]:
            prompt = l.get("prompt", "")
            inp = l.get("in", "")
            out = l.get("out", "")

            if l.get("progress") is not None and l["progress"]:
                _magic_width = _terminal_width
            else:
                _magic_width = 0

            _width = max(
                _width,
                _magic_width,
                len(prompt),
                len(inp) + inp.count(" "),
                len(out) + out.count(" "),
            )

        return _width + 4

    @property
    def size(self):
        lines = len(self.obj["lines"])

        for l in self.obj["lines"]:
            inp = l.get("in", "")
            out = l.get("out", "")
            if inp and out:
                lines += 1

        return lines + 2

    def render(self):
        _code = []
        _width = self.width

        for line in self.obj["lines"]:
            _c = {}

            # if there is a progress bar, don't display prompt or add style
            if line.get("progress") is not None and line["progress"]:
                progress_char = line.get("progressChar", "█")
                _c["prompt"] = ""
                _c["in"] = progress_char * int(0.6 * _width)
                _c["out"] = ""
            else:
                prompt = line.get("prompt", "")
                inp = line.get("in", "")
                out = line.get("out", "")

                if not (prompt or inp or out):
                    continue

                # if only prompt is present, print it all at once
                if prompt and not inp and not out:
                    out = prompt
                    prompt = ""

                _c["prompt"] = prompt
                _c["in"] = inp
                _c["out"] = out

                _c["color"] = line.get("color")
                _c["bold"] = line.get("bold")
                _c["underline"] = line.get("underline")

            _code.append(_c)

        return _code


@dataclass(init=False)
class Image(object):
    def __init__(
        self,
        type: str = "image",
        obj: dict = None,
        fg: int = 0,
        attr: int = 2,
        normal: int = 2,
        bg: int = 7,
    ):
        self.type = type
        self.obj = obj
        self.fg = fg
        self.attr = attr
        self.normal = normal
        self.bg = bg
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
    fg: int = 0
    attr: int = 2  # Screen.A_NORMAL
    normal: int = 2  # Screen.A_NORMAL
    bg: int = 7

    @property
    def size(self):
        raise NotImplementedError

    @property
    def style(self):
        _style = re.findall(r"((\w+)=(\w+))", self.obj["text"])
        return {s[1]: s[2] for s in _style}

    def render(self):
        raise NotImplementedError


@dataclass
class Text(object):
    type: str = "text"
    obj: dict = None
    fg: int = 0
    attr: int = 2  # Screen.A_NORMAL
    normal: int = 2  # Screen.A_NORMAL
    bg: int = 7

    @property
    def size(self):
        return 1

    def render(self):
        return self.obj["text"]


@dataclass
class Codespan(object):
    type: str = "codespan"
    obj: dict = None
    fg: int = 0
    attr: int = 3  # Screen.A_REVERSE
    normal: int = 2  # Screen.A_NORMAL
    bg: int = 7

    @property
    def size(self):
        raise NotImplementedError

    def render(self):
        return (
            f"${{{self.fg},{self.attr},{self.bg}}}"
            + self.obj["text"]
            + f"${{{self.fg},{self.normal},{self.bg}}}"
        )


@dataclass
class Strong(object):
    type: str = "strong"
    obj: dict = None
    fg: int = 0
    attr: int = 1  # Screen.A_BOLD
    normal: int = 2  # Screen.A_NORMAL
    bg: int = 7

    @property
    def size(self):
        raise NotImplementedError

    def render(self):
        return (
            f"${{{self.fg},{self.attr},{self.bg}}}"
            + self.obj["children"][0]["text"]
            + f"${{{self.fg},{self.normal},{self.bg}}}"
        )


@dataclass
class Emphasis(object):
    type: str = "emphasis"
    obj: dict = None
    fg: int = 0
    attr: int = 2  # Screen.A_NORMAL
    normal: int = 2  # Screen.A_NORMAL
    bg: int = 7

    @property
    def size(self):
        raise NotImplementedError

    def render(self):
        # TODO: add italic support
        return self.obj["children"][0]["text"]


@dataclass
class Link(object):
    type: str = "link"
    obj: dict = None
    fg: int = 0
    attr: int = 2  # Screen.A_NORMAL
    normal: int = 2  # Screen.A_NORMAL
    bg: int = 7

    @property
    def size(self):
        raise NotImplementedError

    def render(self):
        return f"{self.obj['children'][0]['text']} ({self.obj['link']})"


@dataclass
class Paragraph(object):
    type: str = "paragraph"
    obj: dict = None
    fg: int = 0
    attr: int = 2  # Screen.A_NORMAL
    normal: int = 2  # Screen.A_NORMAL
    bg: int = 7

    @property
    def size(self):
        # TODO: paragraph size should be sum of all element sizes in it
        return 1

    def render(self):
        text = ""

        for child in self.obj["children"]:
            element_name = child["type"].title().replace("_", "")
            Element = eval(element_name)
            e = Element(obj=child, fg=self.fg, bg=self.bg)
            text += e.render()

        return text


@dataclass
class BlockQuote(object):
    type: str = "quote"
    obj: dict = None
    fg: int = 0
    attr: int = 2  # Screen.A_NORMAL
    normal: int = 2  # Screen.A_NORMAL
    bg: int = 7

    @property
    def size(self):
        return len(self.obj["children"])

    def render(self):
        text = []

        for child in self.obj["children"]:
            p = Paragraph(obj=child, fg=self.fg, bg=self.bg)
            for t in p.render().split("\n"):
                text.append(f"▌ {t}")

        return "\n".join(text)


class Slide(object):
    def __init__(self, elements=None):
        self.elements = elements
        self.has_style = False
        self.has_effect = False
        self.has_image = False
        self.has_code = False
        self.has_codio = False
        self.style = {}
        self.effect = None
        self.fg_color = 0
        self.bg_color = 7

        # TODO: style should always be the first element on a slide
        # raise error if it isn't or if there are two style elements

        for e in self.elements:
            if e.type == "html":
                self.has_style = True
                self.style = e.style

            if e.type == "image":
                self.has_image = True

            if e.type == "code":
                self.has_code = True

            if e.type == "codio":
                self.has_codio = True

        # TODO: support everything!
        if self.style.get("effect") is not None:
            if self.style["effect"] not in EFFECTS:
                raise ValueError(f"Effect {self.style['effect']} is not supported")
            self.has_effect = True
            self.effect = self.style["effect"]

        if self.style.get("fg") is not None:
            try:
                self.fg_color = COLORS[self.style["fg"]]
            except KeyError:
                raise ValueError(f"Color {self.style['fg']} is not supported")

        if self.style.get("bg") is not None:
            try:
                self.bg_color = COLORS[self.style["bg"]]
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

        # apply fg and bg color to all elements
        for e in self.elements:
            e.fg = self.fg_color
            e.bg = self.bg_color

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

            try:
                if obj["type"] == "paragraph":
                    if (
                        len(obj["children"]) == 1
                        and obj["children"][0]["type"] == "image"
                    ):
                        image = obj["children"][0]
                        if image["alt"] == "codio":
                            with open(image["src"], "r") as f:
                                codio = yaml.load(f, Loader=yaml.Loader)
                            buffer.append(Codio(obj=codio))
                        else:
                            buffer.append(Image(obj=image))
                    else:
                        buffer.append(Paragraph(obj=obj))
                else:
                    element_name = obj["type"].title().replace("_", "")
                    Element = eval(element_name)
                    buffer.append(Element(obj=obj))
            except NameError:
                warnings.warn(f"(Slide {sliden + 1}) {element_name} is not supported")

            if i == len(ast) - 1:
                slides.append(Slide(elements=buffer))
                sliden += 1

        return slides
