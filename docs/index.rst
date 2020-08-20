.. present documentation master file, created by
   sphinx-quickstart on Sat Aug  1 03:02:35 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

present — A terminal presentation tool with colors and effects
==============================================================

.. image:: https://readthedocs.org/projects/present/badge/?version=latest
    :target: https://present.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/present.svg
    :target: https://pypi.org/project/present/

.. image:: https://img.shields.io/pypi/pyversions/present.svg
    :target: https://pypi.org/project/present/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black

``present`` is a terminal presentation tool with colors and effects.

.. image:: _static/demo.gif

``present`` is built on `asciimatics <https://github.com/peterbrittain/asciimatics>`_.

Installation
------------

You can simply use pip to install ``present``::

    $ pip install present

Usage
-----

.. code-block:: bash

    $ present sample.md

Syntax
------

Slides follow `Markdown <https://guides.github.com/features/mastering-markdown/>`_ syntax. You can check out the `sample slides <https://github.com/vinayak-mehta/present/blob/master/examples/sample.md>`_ for reference.

.. note:: Some things aren't supported yet:

    - Emphasis, inline code, links, blockquotes, tables and strikethroughs.
    - Effects and foreground / background colors on the same slide.
    - Effects and code on the same slide.

Slide separator
^^^^^^^^^^^^^^^

Each slide can be separated with a ``---``.

.. code-block::

    Slide 1

    ---

    Slide 2

Slide style
^^^^^^^^^^^

Each slide can be styled with foreground / background colors and effects. By default, slides are black on white with no effects. You can add style to a slide by adding an HTML comment at the beginning of the slide (after the slide separator):

.. code-block::

    Slide 1

    ---
    <!-- fg=black bg=yellow -->

    Slide 2

    ---
    <!-- effect=explosions -->

    Slide 3

Available colors: ``black``, ``red``, ``green``, ``yellow``, ``blue``, ``magenta``, ``cyan``, ``white``.
Available effects: ``explosions``, ``stars``, ``matrix``, ``plasma``. More coming soon!

Text
^^^^

.. code-block::

    Slide 1

    ---

    Slide 2

Headers
^^^^^^^

Level 1 headings become figlets, level 2 headings get underlined with `-`, and level 3 headings are treated as normal text, for now.

.. code-block::

    # Heading 1

    ## Heading 2

    ### Heading 3

Lists
^^^^^

Ordered lists become unordered lists automatically, for now.

.. code-block::

    - Item 1
        - Item 1a
        - Item 1b
        - Item 1c
    - Item 2
        - Item 2a

Images
^^^^^^

Image paths are relative to the directory where your slides are kept, and where you invoke `present`.

.. code-block::

    ![RC](images/recurse.png)

Code blocks
^^^^^^^^^^^

.. code-block::

    ```
    import os

    os.getcwd()
    ```

Versioning
----------

``present`` uses `Semantic Versioning <https://semver.org/>`_. For the available versions, see the tags on the GitHub repository.

License
-------

This project is licensed under the Apache License, see the `LICENSE <https://github.com/vinayak-mehta/present/blob/master/LICENSE>`_ file for details.
