from .extra import plugin_url, plugin_strikethrough
from .footnotes import plugin_footnotes
from .table import plugin_table


PLUGINS = {
    'url': plugin_url,
    'strikethrough': plugin_strikethrough,
    'footnotes': plugin_footnotes,
    'table': plugin_table,
}

__all__ = [
    'PLUGINS',
    'plugin_url', 'plugin_strikethrough',
    'plugin_footnotes',
    'plugin_table',
]
