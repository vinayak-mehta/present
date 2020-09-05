# -*- coding: utf-8 -*-

import os
import warnings

import yaml
from mistune import markdown

from .slide import (
    Slide,
    Heading,
    Paragraph,
    Text,
    Strong,
    Codespan,
    Emphasis,
    Link,
    List,
    Image,
    Codio,
    BlockCode,
    BlockHtml,
    BlockQuote,
)


class Markdown(object):
    """Parse and traverse through the markdown abstract syntax tree."""

    def __init__(self, filename):
        self.filename = filename
        self.dirname = os.path.dirname(os.path.realpath(filename))

    def parse(self):
        with open(self.filename, "r") as f:
            text = f.read()

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
                        image["src"] = os.path.join(self.dirname, image["src"])

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
