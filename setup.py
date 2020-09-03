# -*- coding: utf-8 -*-

import os
from setuptools import find_packages


here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, "present", "__version__.py"), "r") as f:
    exec(f.read(), about)

with open("README.md", "r") as f:
    readme = f.read()

requires = [
    "asciimatics>=1.11.0",
    "Click>=7.0",
    "mistune>=2.0.0a4",
    "pyfiglet>=0.8.post1",
    "PyYAML>=5.3.1",
]
dev_requires = ["black>=20.8b1", "Sphinx>=2.2.1"]
dev_requires = dev_requires + requires


def setup_package():
    metadata = dict(
        name=about["__title__"],
        version=about["__version__"],
        description=about["__description__"],
        long_description=readme,
        long_description_content_type="text/markdown",
        license=about["__license__"],
        classifiers=[
            # Trove classifiers
            # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
            "Environment :: Console",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3 :: Only",
        ],
        url=about["__url__"],
        project_urls={
            "Documentation": "https://present.readthedocs.io",
            "Source": "https://github.com/vinayak-mehta/present",
            "Changelog": "https://github.com/vinayak-mehta/present/blob/master/HISTORY.md",
        },
        author=about["__author__"],
        author_email=about["__author_email__"],
        packages=find_packages(exclude=("tests",)),
        entry_points={"console_scripts": ["present = present.cli:cli"]},
        install_requires=requires,
        extras_require={"dev": dev_requires},
        python_requires=">=3.7",
    )

    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
