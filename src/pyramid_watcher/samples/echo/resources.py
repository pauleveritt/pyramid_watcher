from dataclasses import dataclass
from typing import Optional


@dataclass()
class SiteRoot:
    title: str
    __name__: str = ''
    __parent__: Optional[str] = None


def bootstrap(request):
    root = SiteRoot(title='Home Page')

    return root
