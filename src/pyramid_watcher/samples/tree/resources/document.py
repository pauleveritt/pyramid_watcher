"""

An HTML-oriented resource with frontmatter and a rendered
HTML body. Can originate from ``.md`` files.

"""

from dataclasses import dataclass

from .base_resources import Resource


@dataclass
class Document(Resource):
    body: str
