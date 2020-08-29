.. _codio:

codio
=====

A codio is a pre-recorded code block which can be useful for live demos.

.. image:: _static/codio.gif

You can make a codio by writing some `yaml <https://en.wikipedia.org/wiki/YAML>`_ (shown below), and use it inside your Markdown slides just like an image: ``![codio](codio.yml)``. The image alt should be ``![codio]``, but filename can be anything.

.. code-block::

    speed: 2
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
