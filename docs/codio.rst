.. _codio:

codio
=====

A codio is a pre-recorded playable code block which can be useful for live demos. During the presentation, and on the slide with a codio, you can press ``r`` to reset the codio so that it starts playing again from the first line.

.. image:: _static/codio.gif

You can make a codio by writing all the input and output as plaintext in a `YAML <https://en.wikipedia.org/wiki/YAML>`_ file (shown below), and use it inside your Markdown slides just like an image: ``![codio](codio.yml)``. The image alt should be ``![codio]``, but filename can be anything.

.. code-block:: yaml

    speed: 10
    lines:
    - prompt: $
      in: touch a.txt
    - prompt: $
      in: smol-git status
    - out: 'On branch master'
    - out: 'Changes to be committed:'
    - out: '  (use "git reset HEAD ..." to unstage)'
    - out: '    '
    - out: '        new file:   a.txt'
      color: green
      bold: True
    - out: '    '
    - prompt: $
      in: smol-git add a.txt
    - prompt: $
      in: 'smol-git commit -m "Add a.txt"'
    - out: '[master b0faa5a] Save progress'
    - prompt: $
      in: smol-git push origin master
      out: "Pushing to 'origin'..."
    - progress: true
      progressChar: █
    - prompt: $

Let's deconstruct this YAML.

You can set the speed for your codio by specifying its value in a top-level key called ``speed``. It can be between 1 (very slow) to 10 (very fast).

.. code-block:: yaml

    speed: 10

You can specify each line in your code block as a prompt, input, and output item in the ``lines`` list. Input gets printed one character at a time, and output all at once.

.. code-block:: yaml

    lines:
    - prompt: '>>>'
      in: 'os.getcwd()'
      out: '/home/vinayak/dev'

You can also choose to skip output for some lines.

.. code-block:: yaml

    lines:
    - prompt: '>>>'
      in: 'import os'

To show a multi-line output (like in the first example), you can just specify one output per line.

.. code-block:: yaml

    lines:
    - out: 'On branch master'
    - out: 'Changes to be committed:'
    - out: '  (use "git reset HEAD ..." to unstage)'
    - out: '    '
    - out: '        new file:   a.txt'

Notice the ``out: '    '`` to print an empty line.

You can add colors and styles to your output like this:

.. code-block:: yaml

    lines:
    - out: '        new file:   a.txt'
      color: green
      bold: true

Currently, these colors are supported: ``black``, ``red``, ``green``, ``yellow``, ``blue``, ``magenta``, ``cyan``, ``white``. And these styles are supported: ``bold`` and ``underline``. (``italics`` coming soon!)

You can add progress bars too. To add one, just set ``progress`` to ``true`` and add a progress character for your progress bar using ``progressChar``. The default ``progressChar`` is ``█``.

.. code-block:: yaml

    lines:
    - progress: true
      progressChar: #

In the end, you can also print just a prompt again!

.. code-block:: yaml

    lines:
    - prompt: $
