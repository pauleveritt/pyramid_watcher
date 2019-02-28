"""

Handlers for file extensions.

Later, obviously, component lookups.

"""

from pathlib import Path

log = __import__('logging').getLogger(__name__)


def md(filename: Path) -> None:
    """ Read the frontmatter and markdown """

    with filename.open() as f:
        file_content = f.read()
        yaml_string, markdown_string = file_content.split('---\n')
        log.info('\n' + yaml_string + '\n' + markdown_string)

    return


PROCESSORS = dict(
    md=md
)
