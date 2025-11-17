import pygame
import random
from dataclasses import dataclass
from typing import Callable, Tuple
from car import Car
from config import SPAWN_CHANCE_INV, CAR_SPEED

@dataclass
class SpawnConfig:
    """Configuration for spawning cars in a lane."""
    spawn_chance_inv: int = SPAWN_CHANCE_INV  # 1 in spawn_chance_inv every tick
    start_pos: Tuple[int, int] = (0, 0)       # (x, y)
    move_fn: Callable[['Car'], None] = lambda c: None
    image_pool: list = None

class Lane:
    """Represents a lane: owns a sprite group, spawn rules and exit-check."""

    def __init__(self, spawn_config: SpawnConfig, exit_check: Callable[[Car], bool]):
        self.config = spawn_config
        self.group = pygame.sprite.Group()
        self.exit_check = exit_check

    def maybe_spawn(self) -> None:
        if self.config.image_pool is None:
            return
        if random.randint(1, self.config.spawn_chance_inv) == 1:
            image = random.choice(self.config.image_pool)
            x, y = self.config.start_pos
            c = Car(image, x, y, CAR_SPEED, self.config.move_fn)
            self.group.add(c)

    def update(self) -> None:
        self.group.update()
        # remove any sprites that meet exit condition
        for car in list(self.group):
            if self.exit_check(car):
                self.group.remove(car)

    def draw(self, surface: pygame.Surface) -> None:
        for car in self.group:
            surface.blit(car.image, car.rect)
