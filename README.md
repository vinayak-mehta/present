<p align="center">
   <img src="https://raw.githubusercontent.com/vinayak-mehta/present/master/docs/_static/present.png" width="200">
</p>

# present

[![Documentation Status](https://readthedocs.org/projects/present/badge/?version=latest)](https://present.readthedocs.io/en/latest/) [![image](https://img.shields.io/pypi/v/present.svg)](https://pypi.org/project/present/) [![image](https://img.shields.io/pypi/pyversions/present.svg)](https://pypi.org/project/present/) [![image](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

A terminal-based presentation tool with colors and effects.

<p align="center">
   <img src="https://raw.githubusercontent.com/vinayak-mehta/present/master/docs/_static/demo.gif" width="800">
</p>

`present` is built on [asciimatics](https://github.com/peterbrittain/asciimatics).

## Installation

You can simply use pip to install `present`:

```bash
$ pip install present
```

## Usage

```bash
$ present sample.md
```

You can navigate between slides using the arrow keys and quit the presentation with `q`. At the end, you can use `r` to restart the presentation.

## Syntax

Slides follow [Markdown](https://guides.github.com/features/mastering-markdown/) syntax. You can check out the [sample slides](https://github.com/vinayak-mehta/present/blob/master/examples/sample.md) for reference.

**Note:** Some things aren't supported yet.
- Emphasis, inline code, links, blockquotes, tables and strikethroughs.
- Effects and foreground / background colors on the same slide.
- Effects and code on the same slide.

### Separator

Each slide can be separated with a `---`.

```
Slide 1

---

Slide 2
```

### Text

```
Slide 1

---

Slide 2
```

### Headers

Level 1 headings become figlets, level 2 headings get underlined with `-`, and level 3 headings are treated as normal text, for now.

```
# Heading 1

## Heading 2

### Heading 3
```

### Lists

Ordered lists become unordered lists automatically, for now.

```
- Item 1
    - Item 1a
    - Item 1b
    - Item 1c
- Item 2
    - Item 2a
```

### Images

Image paths are relative to the directory where your slides are kept, and where you invoke `present`.

```
![RC](images/recurse.png)
```

### Code blocks

<pre>
```
import os

os.getcwd()
```
</pre>

### Style

Each slide can be styled with foreground / background colors and effects. By default, slides are black on white with no effects. You can add style to a slide by adding a comment at the beginning of the slide (after the slide separator):

```
Slide 1

---
<!-- fg=black bg=yellow -->

Slide 2

---
<!-- effect=explosions -->

Slide 3
```

Color options: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`.

Effect options: `explosions`, `stars`, `matrix`, `plasma`. More coming soon!

## Versioning

`present` uses [Semantic Versioning](https://semver.org/). For the available versions, see the tags on the GitHub repository.

## License

This project is licensed under the Apache License, see the [LICENSE](https://github.com/vinayak-mehta/present/blob/master/LICENSE) file for details.
