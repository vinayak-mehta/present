# -*- coding: utf-8 -*-

from dataclasses import dataclass

import mistune
from pyfiglet import Figlet
from pygments import highlight
from pygments.lexers import Python3Lexer
from pygments.formatters import Terminal256Formatter


@dataclass
class Heading(object):
    type: str = "heading"
    obj: dict = None

    def render(self):
        if self.obj["level"] == 1:
            f = Figlet()
            return f.renderText(self.obj["text"])
        elif self.obj["level"] == 2:
            return "\n".join([self.obj["text"], "-" * len(self.obj["text"])])
        else:
            return self.obj["text"]


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
                self.walk(child, text=text, level=level+1)

        return text

    def render(self):
        return "\n".join(self.walk(self.obj))


@dataclass
class BlockCode(object):
    type: str = "code"
    obj: dict = None

    def render(self):
        result = highlight(self.obj["text"], Python3Lexer(), Terminal256Formatter())
        return result


@dataclass
class Image(object):
    type: str = "text"
    obj: dict = None

    def render(self):
        return ""


@dataclass
class BlockHtml(object):
    type: str = "html"
    obj: dict = None

    def render(self):
        return ""


class Markdown(object):
    """Parse and traverse through the markdown abstract syntax tree.
    """
    def __init__(self):
        self.objs = []

    def parse(self, text):
        ast = mistune.markdown(text, renderer="ast")

        buffer = []
        for i, obj in enumerate(ast):
            if obj["type"] in ["newline"]:
                continue

            if obj["type"] == "thematic_break" and buffer:
                self.objs.append(buffer)
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
                self.objs.append(buffer)

        return self.objs
