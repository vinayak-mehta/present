# -*- coding: utf-8 -*-

import os
import click

from .markdown import Markdown
from .slideshow import Slideshow


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.option(
    "--start",
    "-s",
    type=click.INT,
    default=0,
    show_default=True,
    help="start from a specific slide number",
)
def cli(filename, start):
    """present: A terminal-based presentation tool with colors and effects."""

    slides = Markdown(filename).parse()

    assert (
        0 <= start < len(slides)
    ), f"invalid starting slide number ({start}), must be between 0 and {len(slides)-1}"
    if start > 0:  # rotate slides so that requested starting slide is first
        slides = slides[start:] + slides[:start]

    with Slideshow(slides) as show:
        show.play()

    click.secho("All done! ✨ 🍰 ✨", bold=True)
