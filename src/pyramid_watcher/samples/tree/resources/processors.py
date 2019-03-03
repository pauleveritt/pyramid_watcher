"""

Handlers for file extensions.

Later, obviously, component lookups.

"""

from pathlib import Path

from ruamel.yaml import load, Loader
from mistletoe import markdown

from .document import Document

log = __import__('logging').getLogger(__name__)


def md(target: Path, content_root: Path, parent) -> Document:
    """ Read the frontmatter and markdown """

    file_content = target.open().read()
    yaml_string, markdown_string = file_content.split('---\n')

    # Handle the frontmatter
    frontmatter = (load(yaml_string, Loader=Loader) or {})

    # Parse the Markdown into HTML
    body = markdown(markdown_string)

    # Make and return a resource
    name = target.relative_to(content_root).stem
    resource = Document(__name__=name, __parent__=parent, body=body, **frontmatter)

    return resource


PROCESSORS = dict(
    md=md
)
