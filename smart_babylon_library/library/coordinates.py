# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, Alexander Suvorov
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from dataclasses import dataclass
from typing import Dict, Any
import json

@dataclass(frozen=True)
class LibraryCoordinates:
    floor: int
    room: int
    cabinet: int
    shelf: int
    book: int
    page: int

    def __post_init__(self):
        if any(value < 0 for value in [self.floor, self.room, self.cabinet, self.shelf, self.book, self.page]):
            raise ValueError("All coordinates must be non-negative")

    @property
    def seed(self) -> str:
        return f"{self.floor}:{self.room}:{self.cabinet}:{self.shelf}:{self.book}:{self.page}"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'floor': self.floor,
            'room': self.room,
            'cabinet': self.cabinet,
            'shelf': self.shelf,
            'book': self.book,
            'page': self.page
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'LibraryCoordinates':
        return cls(
            floor=data['floor'],
            room=data['room'],
            cabinet=data['cabinet'],
            shelf=data['shelf'],
            book=data['book'],
            page=data['page']
        )

    @classmethod
    def from_json(cls, json_str: str) -> 'LibraryCoordinates':
        return cls.from_dict(json.loads(json_str))

    def __str__(self):
        return f"Floor{self.floor}/Room{self.room}/Cabinet{self.cabinet}/Shelf{self.shelf}/Book{self.book}/Page{self.page}"
