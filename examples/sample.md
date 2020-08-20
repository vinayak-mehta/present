# present

A terminal presentation tool with colors and effects.

```bash
$ pip install present
```

---

## Markdown

Slides are made with Markdown.

Each slide is separated with a ---.

---

## Lists

These are the controls:

- Basic
    - Quit: q
    - Next slide: n, Right arrow
    - Previous slide: b, Left arrow
- Advanced
    - Please suggest them!

---

## Code blocks

Show me the:

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
![python](images/recurse.png)
```

![python](images/recurse.png)

---
<!-- fg=white bg=red -->

## Colors

You can add style with fg and bg colors!

Just add this to the top of your slide:

```html
<!-- fg=white bg=red -->
```

---
<!-- fg=black bg=yellow -->

## Effects

And there are effects:

- explosions
- matrix
- plasma
- stars
- more coming soon!

```html
<!-- effect=explosions -->
```

---
<!-- effect=explosions -->
