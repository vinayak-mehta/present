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
        "slides": directives.unchanged,
        "description": directives.unchanged,
    }

    def run(self):
        node = Node()
        node["src"] = self.options["src"]
        node["slides"] = self.options["slides"]
        node["description"] = self.options["description"]
        return [node]


def gallery_image_html(self, node):
    src = node["src"]
    slides = node["slides"]
    description = node["description"]

    template = f"""
    <div class="gallery">
      <a href="{slides}/index.html">
        <img src="{src}" width="600" height="400">
      </a>
      <div class="desc">{description}</div>
    </div>
    """
    self.body.append(template)

    raise SkipNode


def setup(app):
    app.add_node(Node, html=(gallery_image_html, None))
    app.add_directive("gallery_image", GalleryImage)
