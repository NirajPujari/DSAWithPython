import pygame
from typing import Callable

class Car(pygame.sprite.Sprite):
    """
    Car sprite. `move_fn` is a callable that mutates the sprite (usually changes rect.x or rect.y).
    """

    def __init__(self, image: pygame.Surface, x: int, y: int, speed: int, move_fn: Callable[['Car'], None]) -> None:
        super().__init__()
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.move_fn = move_fn

    def update(self) -> None:
        """Called by sprite groups once per frame."""
        if callable(self.move_fn):
            self.move_fn(self)
