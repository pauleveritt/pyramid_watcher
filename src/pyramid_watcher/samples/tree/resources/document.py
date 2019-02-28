"""

An HTML-oriented resource with frontmatter and a rendered
HTML body. Can originate from ``.md`` files.

"""

from dataclasses import dataclass


@dataclass
class Document:
    __parent__: str
    title: str
    body: str
    __name__: str = ''
