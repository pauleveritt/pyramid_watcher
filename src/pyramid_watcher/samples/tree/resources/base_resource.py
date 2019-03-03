"""

A base dataclass for all resources. Helps in type hinting.

"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Resource:
    name: str
    parent: Resource
    title: str

    @property
    def __name__(self):
        return self.name

    @property
    def __parent__(self):
        return self.parent
