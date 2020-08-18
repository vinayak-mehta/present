# -*- coding: utf-8 -*-

import click


@click.command("present")
@click.pass_context
def cli(*args, **kwargs):
    """A terminal presentation tool."""
    print("I'm present!")
