from pathlib import Path
import pygame
from config import PUBLIC_DIR
from typing import List, Tuple

PUBLIC_DIR: Path = PUBLIC_DIR  # alias for local use

def load_image(name: str) -> pygame.Surface:
    """Load an image from the public dir and return a Surface with alpha."""
    path = PUBLIC_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Missing asset: {path}")
    return pygame.image.load(str(path)).convert_alpha()

def load_car_collections() -> Tuple[List[pygame.Surface], List[pygame.Surface], List[pygame.Surface], List[pygame.Surface]]:
    V_car_images = [load_image('V_car_red.png'), load_image('V_car_green.png'), load_image('V_car_blue.png')]
    H_car_images = [load_image('H_car_red.png'), load_image('H_car_green.png'), load_image('H_car_blue.png')]
    V1_car_images = [load_image('V1_car_red.png'), load_image('V1_car_green.png'), load_image('V1_car_blue.png')]
    H1_car_images = [load_image('H1_car_red.png'), load_image('H1_car_green.png'), load_image('H1_car_blue.png')]
    return V_car_images, H_car_images, V1_car_images, H1_car_images

def load_center_images() -> Tuple[pygame.Surface, pygame.Surface, pygame.Surface, pygame.Surface]:
    return load_image('R1.png'), load_image('R2.png'), load_image('R3.png'), load_image('R4.png')
