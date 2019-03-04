"""

Handlers for file extensions.

Later, obviously, component lookups.

"""

from pathlib import Path
from typing import Optional

from ruamel.yaml import load, Loader
from mistletoe import markdown

from .base_resources import Resource
from .document import Document
from .base_resources import Folder

log = __import__('logging').getLogger(__name__)


def md(target: Path, parent: Resource) -> Optional[Document]:
    """ Read the frontmatter and markdown """

    file_content = target.open().read()
    if '---\n' in file_content:
        yaml_string, markdown_string = file_content.split('---\n')

        # Handle the frontmatter
        frontmatter = (load(yaml_string, Loader=Loader) or {})

        # Parse the Markdown into HTML
        body = markdown(markdown_string)

        # Make and return a resource. If the name is 'index', make a
        # Folder.
        name = str(target.stem)
        if name == 'index':
            # make a folder
            resource = Folder(name=name, parent=parent, body=body, **frontmatter)
        else:
            resource = Document(name=name, parent=parent, body=body, **frontmatter)

        return resource


PROCESSORS = dict(
    md=md
)
