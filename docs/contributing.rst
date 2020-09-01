.. _contributing:

Contributor's Guide
===================

Thanks for taking the time to contribute! This doc will help you get started with contributing issues, documentation, code, and tests. If you have any questions, feel free to reach out to `Vinayak Mehta`_, the author and maintainer.

.. _Vinayak Mehta: https://github.com/vinayak-mehta

Filing Issues
-------------

``present`` uses `GitHub issues`_ to keep track of all issues and pull requests. Before opening an issue (which asks a question or reports a bug), please use the issue search feature to look for existing issues (both open and closed) that may be similar. When opening an issue:

.. _GitHub issues: https://github.com/vinayak-mehta/present/issues

1. List the steps you used to install ``present``.

2. Make sure you include your operating system name, terminal emulator name, Python version number, and ``present`` version number. You can use the following code snippet to find most of this information::

    >>> import platform; print(platform.platform())
    >>> import sys; print('Python', sys.version)
    >>> import present; print(present.__version__)

3. Make sure you provide a suitable amount of information to work with. For example, the Markdown for the slide causing the issue in a `code block`_ (you can replace sensitive text with `lorem ipsum`_), what you expected to happen, and what actually happened.

.. _lorem ipsum: https://www.lipsum.com/

4. When filing bug reports about exceptions or tracebacks, please include the complete traceback in a `code block`_, along with everything from 2.

5. When suggesting enhancements, please use a clear and descriptive title, along with a very detailed description of the suggested enhancement.

.. _code block: https://help.github.com/articles/creating-and-highlighting-code-blocks/

Contributing Docs and Code
--------------------------

Setting up the development environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To install the dependencies needed for development, you can use pip::

    $ pip install "present[dev]"

Alternatively, you can clone the project repository, and install using pip::

    $ pip install ".[dev]"

Writing Documentation
^^^^^^^^^^^^^^^^^^^^^

Writing documentation, function docstrings, examples and tutorials is a great way to start contributing to free and open-source software! The documentation lies in the ``docs/`` directory of the project repository.

The documentation (including this page) is written in `reStructuredText`_, with `Sphinx`_ used to generate these lovely HTML files that you're currently reading (unless you're reading this on GitHub). You can edit the documentation using any text editor and then generate the HTML output by running ``make html`` in the ``docs/`` directory.

.. _reStructuredText: https://en.wikipedia.org/wiki/ReStructuredText
.. _Sphinx: http://www.sphinx-doc.org/en/master/

Contributing Code
^^^^^^^^^^^^^^^^^

Another great way to start contributing to ``present`` is to pick an issue tagged with the `help wanted`_ or the `good first issue`_ tags. If you're unable to find a good first issue, feel free to contact the maintainer.

.. _help wanted: https://github.com/vinayak-mehta/present/labels/help%20wanted
.. _good first issue: https://github.com/vinayak-mehta/present/labels/good%20first%20issue

Pull Requests
-------------

Submitting your pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The preferred workflow for contributing to ``present`` is to fork the `project repository`_ on GitHub, clone, develop on a branch and then finally submit a pull request. Here are the steps:

.. _project repository: https://github.com/vinayak-mehta/present

1. Fork the project repository. Click on the ‘Fork’ button near the top of the page. This creates a copy of the code under your account on the GitHub.

2. Clone your fork of ``present`` from your GitHub account::

    $ git clone https://www.github.com/[username]/present

3. Create a branch to hold your changes::

    $ git checkout -b my-feature

Always branch out from ``master`` to work on your contribution. It's good practice to never work on the ``master`` branch!

.. note:: ``git stash`` is a great way to save the work that you haven't committed yet, to move between branches.

4. Work on your contribution. Add changed files using ``git add`` and then ``git commit`` them::

    $ git add modified_files
    $ git commit

5. Finally, push them to your GitHub fork::

    $ git push -u origin my-feature

Now it's time to go to the your fork of ``present`` and create a pull request! You can `follow these instructions`_ to do that.

.. _follow these instructions: https://help.github.com/articles/creating-a-pull-request-from-a-fork/

Working on your pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's recommended that your pull request complies with the following guidelines:

- Make sure your code follows `pep8`_. You can also run `black`_ on your code since ``present`` follows ``black`` code style.

.. _pep8: http://pep8.org
.. _black: https://black.readthedocs.io/en/stable/

- In case your pull request contains function docstrings, make sure you follow the `numpydoc`_ format.

.. _numpydoc: https://numpydoc.readthedocs.io/en/latest/format.html

- Make sure your commit messages follow `the seven rules of a great git commit message`_:
    - Separate subject from body with a blank line
    - Limit the subject line to 50 characters
    - Capitalize the subject line
    - Do not end the subject line with a period
    - Use the imperative mood in the subject line
    - Wrap the body at 72 characters
    - Use the body to explain what and why vs. how

.. _the seven rules of a great git commit message: https://chris.beams.io/posts/git-commit/

- If the contribution is complete and ready for a detailed review, prefix your title of your pull request with ``[MRG]`` (Ready for Merge). An incomplete pull request's title should be prefixed with ``[WIP]`` (to indicate work in progress), and changed to ``[MRG]`` when it's complete. A good `task list`_ in the PR description will ensure that other people get a fair idea of what it proposes to do, which will also increase collaboration.

.. _task list: https://blog.github.com/2013-01-09-task-lists-in-gfm-issues-pulls-comments/
