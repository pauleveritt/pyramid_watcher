"""

A base dataclass for all resources. Helps in type hinting.

"""

from __future__ import annotations
from collections import Mapping
from dataclasses import dataclass
from typing import Optional, Iterable


@dataclass
class Resource:
    name: str
    parent: Resource
    title: str

    @property
    def __name__(self) -> str:
        return self.name

    @property
    def __parent__(self) -> Optional[Resource]:
        return self.parent


@dataclass
class Folder(Resource, Mapping):
    parent: Optional[Resource]
    title: str

    def __post_init__(self):
        """ Make this a dictionary-like object that can contain things """
        self._dict: Mapping[str, Resource] = {}

    def __getitem__(self, key: str) -> Resource:
        return self._dict[key]

    def __setitem__(self, key: str, value: Resource):
        self._dict[key] = value

    def __delitem__(self, key: str):
        del self._dict[key]

    def __iter__(self) -> Iterable[str]:
        return iter(self._dict)

    def __len__(self) -> int:
        return len(self._dict)
