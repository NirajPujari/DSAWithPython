from typing import List

class CircularQueue:
    """Simple circular queue to rotate through named roads."""

    def __init__(self, items: List[str] | None = None) -> None:
        if items is None:
            items = ['R1', 'R2', 'R3', 'R4']
        self.list = items
        self.MAX_SIZE = len(self.list)
        self.head = 0
        self.tail = self.MAX_SIZE - 1
        self.road = self.list[self.head]
        self.mode = 'Auto'

    def forward(self) -> None:
        self.head = (self.head + 1) % self.MAX_SIZE
        self.tail = (self.tail + 1) % self.MAX_SIZE
        self.road = self.list[self.head]

    def backward(self) -> None:
        self.head = (self.head - 1) % self.MAX_SIZE
        self.tail = (self.tail - 1) % self.MAX_SIZE
        self.road = self.list[self.head]