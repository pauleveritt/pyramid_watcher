"""

An HTML-oriented resource with frontmatter and a rendered
HTML body. Can originate from ``.md`` files.

"""

from dataclasses import dataclass

from .base_resource import Resource


@dataclass
class Document(Resource):
    body: str
