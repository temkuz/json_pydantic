from __future__ import annotations

from typing import TypedDict


class ClassStruct(TypedDict):
    name: str
    args: dict[str, str]
    inner_classes: list[ClassStruct] | list
