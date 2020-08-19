# -*- coding: utf-8 -*-

VERSION = (0, 2, 0)
PRERELEASE = None  # alpha, beta or rc
REVISION = None


def generate_version(version, prerelease=None, revision=None):
    version_parts = [".".join(map(str, version))]
    if prerelease is not None:
        version_parts.append("-{}".format(prerelease))
    if revision is not None:
        version_parts.append(".{}".format(revision))
    return "".join(version_parts)


__title__ = "present"
__description__ = "A terminal-based presentation tool."
__url__ = "https://github.com/vinayak-mehta/present"
__version__ = generate_version(VERSION, prerelease=PRERELEASE, revision=REVISION)
__author__ = "Vinayak Mehta"
__author_email__ = "vmehta94@gmail.com"
__license__ = "Apache 2.0"
