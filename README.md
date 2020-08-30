<p align="center">
   <img src="https://user-images.githubusercontent.com/27065646/91667596-3503e400-eb06-11ea-9c1c-7763cddb1668.png" width="95%" height="95%">
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#syntax">Syntax</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#cersioning">Versioning</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#license">License</a>
</p>

<p align="center">
  <a href="https://present.readthedocs.io/en/latest/"><img src="https://readthedocs.org/projects/present/badge/?version=latest" alt="Documentation Status"></a>
  <a href="https://pypi.org/project/present/"><img src="https://img.shields.io/pypi/v/present.svg" alt="image"></a>
  <a href="https://pypi.org/project/present/"><img src="https://img.shields.io/pypi/pyversions/present.svg" alt="image"></a>
  <a href="https://github.com/ambv/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="image"></a>
</p>

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

Some controls:

- Quit: `q`
- Previous slide: `b`, Left arrow
- Next slide: `n`, Space bar, Right arrow

At the end, you can press `r` to restart the presentation.

## Syntax

Slides follow [Markdown](https://guides.github.com/features/mastering-markdown/) syntax. You can check out the [sample slides](https://github.com/vinayak-mehta/present/blob/master/examples/sample.md) for reference.

**Note:** Some things aren't supported yet:
- Effects and foreground / background colors on the same slide.
- Effects and code on the same slide.

### Separator

Each slide can be separated with a `---`.

```
Slide 1

---

Slide 2
```

### Headers

Level 1 headings become figlets, level 2 headings get underlined with `-`, and level 3 headings become bold.

```
# Heading 1

## Heading 2

### Heading 3
```

### Text

```
This is normal text

This is **bold text**

This is *italic text*

This is `inline code`

This is a [link](www.google.com)

As Kanye West said:

> We're living the future so
> the present is our past.
```

### Lists

Ordered lists become unordered lists automatically.

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

Note: You can use high resolution images and tweak the terminal font size to get the best results.

### Code blocks

<pre>
```
import os

os.getcwd()
```
</pre>

### Codios

Codios are pre-recorded playable code blocks which can be useful for live demos. You can find out how to write one in the [codio](https://present.readthedocs.io/en/latest/codio.html) section of the documentation.

```
![codio](codio.yml)
```

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

Colors: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`.

Effects: `fireworks`, `explosions`, `stars`, `matrix`, `plasma`. More coming soon!

## Versioning

`present` uses [Semantic Versioning](https://semver.org/). For the available versions, see the tags on the GitHub repository.

## License

This project is licensed under the Apache License, see the [LICENSE](https://github.com/vinayak-mehta/present/blob/master/LICENSE) file for details.
