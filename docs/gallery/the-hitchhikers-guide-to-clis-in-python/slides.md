<!-- fg=white bg=blue -->

## The Hitchhiker's Guide to CLIs in Python

Vinayak Mehta

@vortex_ape

---

$ whoami

https://github.com/vinayak-mehta

---

![camelot](images/camelot.png)

https://github.com/camelot-dev

---

![rc](images/recurse-center.png)

www.recurse.com

---

In the beginning ...

---

Typewriter 📝

---

.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--

---

Teletypewriter 📞 📝

---

Computers 💻

---

Friden Flexowriter 📞 📝

---

Teletype Model 33 📞 📝

---

Video terminals 📺 📝

---

Terminal emulators 💻 📝

---

teletype

---

(t)ele(ty)pe

---

tty

---

shell

---

```
 keyboard
         \
          \ input
           \
         (terminal)- - - - - - - - - -(process)
           /
          / output
         /
 display
```

---

```
 keyboard
         \
          \ input
           \
         (terminal)- - -(termios)- - -(process)
           /
          / output
         /
 display
```

---

```
$ man termios
```

---

```
$ stty -a
speed 38400 baud; rows 34; columns 166; line = 0;
intr = ^C; quit = ^\; erase = ^?; kill = ^U; eof = ^D;
-ignbrk brkint -ignpar -parmrk -inpck -istrip -inlcr -igncr
opost -olcuc -ocrnl onlcr -onocr -onlret -ofill -ofdel nl0 cr0
isig icanon iexten echo echoe echok -echonl -noflsh -xcase -tostop
```

---

```
$ man termios
...
   ICANON Enable canonical mode (described below).
...
```

---

```
$ stty -icanon
```

---

![codio](codios/icanon.yml)

---

```
$ man termios
...
   ONLCR  (XSI) Map NL to CR-NL on output.
...
```

---

![codio](codios/progress-bar.yml)

---

```
$ stty -onlcr
```

---

![codio](codios/onlcr.yml)

---

```
$ man termios
...
   ECHO   Echo input characters.
...
```

---

```
$ stty -echo
```

---

![codio](codios/echo.yml)

---

```
$ reset
```

---

```
import termios
```

---

Signals

---

In-band signaling

---

Control characters

---

Control characters

- ^H - backspace
- ^J - newline
- ^C - interrupt the running process
- ^D - end text input or exit the shell

---

Escape sequences

---

Escape sequences

- \u001b[2J - clear screen
- \u001b[1m - make text bold
- \u001b[31m - make text red
- \u001b[{n}A - moves cursor up by n

---

Streams

---

stdin

---

stdout and stderr

---

Redirection

---

```
$ echo "hello" > file
$ echo "world" >> file
```

---

```
$ echo "hello" | cat
hello
```

---

Terminals ❤️

---
<!-- fg=white bg=blue -->

Command-line interfaces

---

Command-line interfaces

```
Prompt
```

---

Command-line interfaces

```
Prompt command
```

---

Command-line interfaces

```
Prompt command option1 option2
```

---

Command-line interfaces

```
Prompt command option1 option2 argument1 argument2 <Enter>
```

---

Command-line interfaces

```
Prompt command option1 option2 argument1 argument2 <Enter>
Output
```

---

Arguments

---

Arguments

```
$ cp src dst
```

---

Options

---

Options

```
$ cp -r src dst
```

---

Help

---

Help

```
$ cp --help
```

---

Man pages

```
$ man termios
```

---

Standards

---

POSIX

---

XDG base directory specification

---

XDG base directory specification

- $XDG_CONFIG_HOME=$HOME/.config
- $XDG_DATA_HOME=$HOME/.local/share
- $XDG_CACHE_HOME=$HOME/.cache

---
<!-- fg=white bg=blue -->

CLIs in Python

---

smol-pip 🐤

---

```
$ smol-pip install --upgrade package_name
```

---

Standard library

---

sys

---

sys.argv

---

```
import sys

help = "Pip Installs Packages."

if __name__ == "__main__":
    arguments = sys.argv
```

---

```
import sys

help = "Pip Installs Packages."

if __name__ == "__main__":
    arguments = sys.argv
    if arguments[1] in ["-h", "--help"]:
        print(help)
```

---

```
import sys

help = "Pip Installs Packages."

if __name__ == "__main__":
    arguments = sys.argv
    if arguments[1] in ["-h", "--help"]:
        print(help)
    elif arguments[1] in ["-v", "--version"]:
        print("0.1.0")
```

---

```
import sys

help = "Pip Installs Packages."

if __name__ == "__main__":
    arguments = sys.argv
    ...
    else:
        print(arguments)
        # ['smol-pip', 'install', '--upgrade', 'Click']
        if arguments[1] == "install":
            # dispatch to install / upgrade code
        else:
            raise ValueError("Unknown subcommand!")
```

---

optparse

---

PEP 389

---

argparse

---

argparse

- -pf
- -file
- +f
- +rgb
- /f
- /file

---

argparse

- pip install
- pip freeze
- pip search

---

```
import argparse

parser = argparse.ArgumentParser(
    description="Pip Installs Packages."
)
```

---

```
import argparse

parser = argparse.ArgumentParser(
   description="Pip Installs Packages."
)
parser.add_argument(
    "-v",
    "--version",
    action="version",
    version="0.1.0"
)
```

---

```
subparsers = parser.add_subparsers(dest="subparser_name")
install = subparsers.add_parser("install")
```

---

```
subparsers = parser.add_subparsers(dest="subparser_name")
install = subparsers.add_parser("install")
install.add_argument(
    "-u",
    "--upgrade",
    action="store_true",
    help="Upgrade package to the newest available version.",
)
install.add_argument("package_name")
```

---

```
if __name__ == "__main__":
    arguments = parser.parse_args()
    print(arguments)
    # Namespace(package_name='Click', upgrade=True)
```

---

```
if __name__ == "__main__":
    arguments = parser.parse_args()
    print(arguments)
    # Namespace(package_name='Click', upgrade=True)
    if arguments.subparser_name == "install":
        # dispatch to install / upgrade code
    else:
        raise ValueError("Unknown subcommand!")
```

---

```
$ smol-pip --help
usage: smol-pip [-h] [-v] {install} ...

Pip Installs Packages.

positional arguments:
{install}

optional arguments:
-h, --help     show this help message and exit
-v, --version  show program's version number and exit
```

---

Python Package Index

---

docopt

---

```
help = """Pip Installs Packages.

Usage:
smol-pip install PACKAGE_NAME
smol-pip install --upgrade PACKAGE_NAME

Options:
-h --help     Show this screen.
--version     Show version.
"""
```

---

```
from docopt import docopt

if __name__ == "__main__":
    arguments = docopt(help, version="0.1.0")
    print(arguments)
    # {'--upgrade': True,
    #  'PACKAGE_NAME': 'Click',
    #  'install': True}
```

---

```
from docopt import docopt

if __name__ == "__main__":
    arguments = docopt(help, version="0.1.0")
    print(arguments)
    # {'--upgrade': True,
    #  'PACKAGE_NAME': 'Click',
    #  'install': True}
    if arguments["install"]:
        # dispatch to install / upgrade code
    else:
        raise ValueError("Unknown subcommand!")
```

---

<!-- effect=matrix -->

---
<!-- fg=white bg=blue -->

click

---

```
import click

def cli(*args, **kwargs):
    """Pip Installs Packages."""
    pass
```

---

```
import click

@click.group("pip")
def cli(*args, **kwargs):
    """Pip Installs Packages."""
    pass
```

---

```
import click

@click.group("pip")
@click.version_option("0.1.0")
def cli(*args, **kwargs):
    """Pip Installs Packages."""
    pass
```

---

```
def install(*args, **kwargs):
    """Install packages."""
    # install / upgrade package_name
```

---

```
@cli.command("install")
def install(*args, **kwargs):
    """Install packages."""
    # install / upgrade package_name
```

---

```
@cli.command("install")
@click.option(
    "-u",
    "--upgrade",
    is_flag=True,
    help="Upgrade package to the newest available version.",
)
def install(*args, **kwargs):
    """Install packages."""
    # install / upgrade package_name
```

---

```
@cli.command("install")
@click.option(
    "-u",
    "--upgrade",
    is_flag=True,
    help="Upgrade package to the newest available version.",
)
@click.argument("package_name")
def install(*args, **kwargs):
    """Install packages."""
    # install / upgrade package_name
```

---

```
if __name__ == "__main__":
    cli()
```

---

```
@cli.command("install")
@click.option(
    "-u",
    "--upgrade",
    is_flag=True,
    help="Upgrade package to the newest available version.",
)
@click.argument("package_name")
def install(*args, **kwargs):
    """Install packages."""
    print(kwargs)
    # {'upgrade': True, 'package_name': 'Click'}
    # install / upgrade package_name
```

---

```
$ smol-pip --help
Usage: smol-pip [OPTIONS] COMMAND [ARGS]...

Pip Installs Packages.

Options:
--version  Show the version and exit.
--help     Show this message and exit.

Commands:
install  Install packages.
```

---

click

---

smol-git 🐤

---

```
$ smol-git --help
Usage: smol-git [OPTIONS] COMMAND [ARGS]...

smol-git - the stupid content tracker

Options:
--version  Show the version and exit.
--help     Show this message and exit.

Commands:
clone   Clone a repository into a new directory.
commit  Record changes to the repository.
config  Get and set repository or global options.
log     Show commit logs.
push    Update remote refs along with associated objects.
status  Show the working tree status.
```

---

```
import click

@click.group("smol-git")
@click.version_option("0.1.0")
def cli(*args, **kwargs):
    """smol-git - the stupid content tracker"""
    pass
```

---

Progress bars

---

```
@cli.command()
@click.argument("src")
@click.argument("dest", required=False)
def clone(src, dest):
    ...
    with click.progressbar(files) as _files:
        for file in _files:
            # download file
```

---

![codio](codios/git-clone.yml)

---

Application folders

---

```
@cli.command()
@click.argument("key")
@click.argument("value")
def config(key, value):
    app_dir = click.get_app_dir("smol_git")
    if not os.path.exists(app_dir):
        os.makedirs(app_dir)
    cfg = os.path.join(app_dir, "config")
    # set repository or global options
```

---

![codio](codios/git-config.yml)

---

Paged output

---

```
@cli.command()
def log():
    ...
    click.echo_via_pager(log_string)
```

---

![codio](codios/git-log.yml)

---

Colored text

---

```
@cli.command()
def status():
    ...
    for file in files:
        file_status = "new file" if file.added else "modified"
        status += click.style(
            f"\t{file_status}:   {file.name}\n",
            fg="green",
            bold=True
        )
    click.echo(status_string)
```

---

![codio](codios/git-status.yml)

---

Launching editors

---

```
@cli.command()
@click.option("-m", "--message", help="The commit message.")
def commit(*args, **kwargs):
    if kwargs["message"] is None:
        commit_message = click.edit()
    else:
        commit_message = kwargs["message"]
    # commit changes
```

---

![codio](codios/git-commit.yml)

---

User prompts

---

```
@cli.command()
@click.argument("repository")
@click.argument("branch")
def push(repository, branch):
    username = click.prompt("Username for 'https://github.com'")
    password = click.prompt(
        f"Password for 'https://{username}@github.com'",
        hide_input=True
    )
    # push changes
```

---

![codio](codios/git-push.yml)

---

```
$ smol-git --help
Usage: smol-git [OPTIONS] COMMAND [ARGS]...

smol-git - the stupid content tracker

Options:
--version  Show the version and exit.
--help     Show this message and exit.

Commands:
clone   Clone a repository into a new directory.
commit  Record changes to the repository.
config  Get and set repository or global options.
log     Show commit logs.
push    Update remote refs along with associated objects.
status  Show the working tree status.
```

---

Testing click code

---

```
from click.testing import CliRunner
from smol_git.cli import cli

def test_git_log():
    runner = CliRunner()
    result = runner.invoke(cli, ['log'])
    assert result.exit_code == 0
    assert result.output == expected_output_log
```

---

https://click.palletsprojects.com

---
<!-- fg=white bg=blue -->

Packaging the CLI

---

```
.
├── setup.py
└── smol_git
    ├── cli.py
    ├── __init__.py
    ├── utils.py
    └── __version__.py
```

---

```
from setuptools import setup

setup(
    ...
    name="smol-git",
    entry_points={
        "console_scripts": [
            "smol-git = smol_git.cli:cli"
        ]
    },
    ...
)
```

---

Pushing to PyPI

---

```
$ python setup.py sdist bdist_wheel
$ twine upload dist/*
```

---
<!-- fg=white bg=blue -->

User experience

---

Unix philosophy

- Write programs that do one thing and do it well.
- Write programs to work together.
- Write programs to handle text streams, because that is a universal interface.

---

Make features discoverable

- Persistent history
- History search
- Auto-completion

---

## prompt-toolkit

- ipython
- dbcli

---

Resources

- Slides: https://vinayak.io/talks
- Code: https://github.com/vinayak-mehta/smol-git
- The TTY demystified
- What is the exact difference between a terminal, a shell, a tty and a console?
- Brandon Rhodes' keynote at North Bay Python 2017
- Terminal whispering by Thomas Ballinger at PyCon 2015
- Writing Command Line Applications that Click by Dave Forgac at PyCon 2019
- Awesome CLI Tools by Amjith Ramanujam at PyCon 2017
- Fish shell design document

---
<!-- effect=fireworks -->

@vortex_ape / vinayak.io

Made with ❤️ using 'present'

https://github.com/vinayak-mehta/present

---

![pyconline-au](images/pyconline-au.jpg)
