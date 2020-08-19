from ..scanner import escape_url
from ..inline_parser import ESCAPE

__all__ = ["plugin_url", "plugin_strikethrough"]


#: url link like: ``https://lepture.com/``
URL_LINK_PATTERN = r"""(https?:\/\/[^\s<]+[^<.,:;"')\]\s])"""


def parse_url_link(self, m, state):
    return "link", escape_url(m.group(0))


def plugin_url(md):
    md.inline.register_rule("url_link", URL_LINK_PATTERN, parse_url_link)
    md.inline.rules.append("url_link")


#: strike through syntax looks like: ``~~word~~``
STRIKETHROUGH_PATTERN = (
    r"~~(?=[^\s~])(" r"(?:\\~|[^~])*" r"(?:" + ESCAPE + r"|[^\s~]))~~"
)


def parse_strikethrough(self, m, state):
    text = m.group(1)
    return "strikethrough", self.render(text, state)


def render_html_strikethrough(text):
    return "<del>" + text + "</del>"


def plugin_strikethrough(md):
    md.inline.register_rule("strikethrough", STRIKETHROUGH_PATTERN, parse_strikethrough)

    index = md.inline.rules.index("codespan")
    if index != -1:
        md.inline.rules.insert(index + 1, "strikethrough")
    else:  # pragma: no cover
        md.inline.rules.append("strikethrough")

    if md.renderer.NAME == "html":
        md.renderer.register("strikethrough", render_html_strikethrough)
