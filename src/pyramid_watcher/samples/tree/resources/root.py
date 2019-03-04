from dataclasses import dataclass

from .base_resources import Folder

log = __import__('logging').getLogger(__name__)


@dataclass
class Root(Folder):
    """ This is a special kind of folder with parent of None """

    pass
