# -*- coding: utf-8 -*-

import click

from .markdown import Markdown


@click.command("present")
@click.argument("filename")
def cli(filename):
    """A terminal presentation tool."""

    markdown = Markdown()
    with open(filename, "r") as f:
        slides = markdown.parse(f.read())

    print(slides)
