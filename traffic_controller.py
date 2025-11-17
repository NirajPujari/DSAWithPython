import pygame
from circular_queue import CircularQueue
from enum import Enum
from typing import Callable
from config import AUTO_DURATION_SECONDS

class Mode(Enum):
    AUTO = "Auto"
    MANUAL = "Manual"

class TrafficController:
    """
    Central controller for traffic mode, road rotation and timer handling.
    Uses pygame timers to rotate automatically.
    """

    ROTATE_EVENT = pygame.USEREVENT + 1

    def __init__(self, on_rotate: Callable[[], None]) -> None:
        """
        on_rotate: callback that should be called whenever a rotation occurs.
        """
        self.queue = CircularQueue()
        self.mode = Mode.AUTO
        self.on_rotate = on_rotate
        # Register timer for auto rotation
        pygame.time.set_timer(TrafficController.ROTATE_EVENT, int(AUTO_DURATION_SECONDS * 1000))

    @property
    def road(self) -> str:
        return self.queue.road

    def toggle_mode(self) -> None:
        self.mode = Mode.MANUAL if self.mode == Mode.AUTO else Mode.AUTO
        # toggle timer based on mode
        if self.mode == Mode.AUTO:
            pygame.time.set_timer(TrafficController.ROTATE_EVENT, int(AUTO_DURATION_SECONDS * 1000))
        else:
            pygame.time.set_timer(TrafficController.ROTATE_EVENT, 0)  # stop timer

    def handle_event(self, event: pygame.event.Event) -> None:
        """Process pygame events relevant to traffic (auto-rotate)."""
        if event.type == TrafficController.ROTATE_EVENT and self.mode == Mode.AUTO:
            self.queue.forward()
            if callable(self.on_rotate):
                self.on_rotate()

    def forward(self) -> None:
        self.queue.forward()

    def backward(self) -> None:
        self.queue.backward()
