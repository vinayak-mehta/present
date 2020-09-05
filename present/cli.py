# -*- coding: utf-8 -*-

import os
import click

from .markdown import Markdown
from .slideshow import Slideshow


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def cli(filename):
    """present: A terminal-based presentation tool with colors and effects."""

    slides = Markdown(filename).parse()

    with Slideshow(slides) as show:
        show.play()

    click.secho("All done! ✨ 🍰 ✨", bold=True)
