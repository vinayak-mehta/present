# -*- coding: utf-8 -*-

from docutils.nodes import Body, Element, SkipNode
from docutils.parsers.rst import Directive, directives


class Node(Body, Element):
    pass


class GalleryImage(Directive):
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "src": directives.unchanged,
        "stub": directives.unchanged,
        "description": directives.unchanged,
    }

    def run(self):
        node = Node()
        node["src"] = self.options["src"]
        node["stub"] = self.options["stub"]
        node["description"] = self.options["description"]
        return [node]


def gallery_image_html(self, node):
    src = node["src"]
    stub = node["stub"]
    description = node["description"]

    template = f"""
    <div class="gallery">
      <a href="{stub}/index.html">
        <img src="https://present.readthedocs.io/en/latest/{src}" width="600" height="400">
        <div class="desc">{description}</div>
      </a>
    </div>
    """
    self.body.append(template)

    raise SkipNode


def setup(app):
    app.add_node(Node, html=(gallery_image_html, None))
    app.add_directive("gallery_image", GalleryImage)
