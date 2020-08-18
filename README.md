# present

A terminal presentation tool.

## Installation

```bash
$ pip install present
```

## Usage

```bash
$ present slides.md
```

## Features

Slides can be formatted with Markdown, and each slide can be separated using `---`.

### Headers and normal text

```markdown
# present

A terminal presentation tool.
```

### Lists

```markdown
- Basic controls
    - Quit: q
    - Next slide: n, Right arrow
    - Previous slide: b, Left arrow
- Advance controls
```

### Code blocks

```python
>>> bin(termios.ICANON)
'0b10'
>>> bin(termios.ECHO)
'0b1000'
```

### Images

<img src="python.png" width="200" />

### Animations

```html
<!-- effect='explosions' -->
```
