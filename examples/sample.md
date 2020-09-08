# present

A terminal-based presentation tool with colors and effects

```bash
$ pip install present
```

---

## Syntax

You can write slides in Markdown

Each slide should be separated with a ---

---

## Lists

Some controls:

- Basic
    - Quit: q
    - Previous slide: b, Left arrow, Page Up
    - Next slide: n, Space bar, Right arrow, Page Down

---

## Formatted text

As Kanye West said:

> We're living the future so
> the present is our past.

This is normal text

This is **bold text**

This is `inline code`

This is a [link](www.google.com)

---

## Code blocks

An explanation for the code below:

```python
import os

print(os.getcwd())
```

```python
import shutil

columns, rows = shutil.get_terminal_size()
```

---

## Images

```
![RC](images/recurse.png)
```

![RC](images/recurse.png)

---
<!-- fg=white bg=red -->

## Colors

You can style your slides with fg and bg colors!

Just add this to the top of your slide:

```html
<!-- fg=white bg=red -->
```

Colors: black, red, green, yellow, blue, magenta, cyan, white

---
<!-- fg=black bg=yellow -->

## Effects

You can also add effects!

Just add this to the top of your slide:

```html
<!-- effect=fireworks -->
```

Effects: fireworks, explosions, matrix, plasma, stars, more coming soon!

---
<!-- effect=fireworks -->

---
<!-- effect=explosions -->

---
<!-- effect=matrix -->

---
<!-- effect=stars -->

---
<!-- effect=plasma -->
