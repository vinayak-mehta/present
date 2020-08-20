# -*- coding: utf-8 -*-

import os
import click

from .slideshow import Slideshow
from .markdown import Markdown


@click.command()
@click.argument("filename")
def cli(filename):
    """present: A terminal-based presentation tool with colors and effects."""

    markdown = Markdown()

    with open(filename, "r") as f:
        slides = markdown.parse(f.read())

    with Slideshow(slides) as show:
        show.play()

    click.secho("All done! ✨ 🍰 ✨", bold=True)
