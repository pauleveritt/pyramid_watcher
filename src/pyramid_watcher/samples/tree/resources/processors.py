"""

Handlers for file extensions.

Later, obviously, component lookups.

"""

from pathlib import Path

from ruamel.yaml import load, Loader
from mistletoe import markdown

from .document import Document

log = __import__('logging').getLogger(__name__)


def md(filename: Path, content_root: Path, siteroot) -> Document:
    """ Read the frontmatter and markdown """

    with filename.open() as f:
        file_content = f.read()
        yaml_string, markdown_string = file_content.split('---\n')

        # Handle the frontmatter
        frontmatter = (load(yaml_string, Loader=Loader) or {})

        # Parse the Markdown into HTML
        body = markdown(markdown_string)

        # Make and return a resource
        name = filename.relative_to(content_root).stem
        parent = siteroot
        resource = Document(__name__=name, __parent__=parent, body=body, **frontmatter)

        return resource


PROCESSORS = dict(
    md=md
)
