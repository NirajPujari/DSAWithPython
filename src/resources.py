from pathlib import Path
import pygame
from config import ASSET_DIR, CAR_DIR, CENTER_DIR
from typing import List, Tuple

ASSET_DIR: Path = ASSET_DIR
CAR_DIR: Path = CAR_DIR
CENTER_DIR: Path = CENTER_DIR

def load_image(name: str) -> pygame.Surface:
    """Load an image from the public dir and return a Surface with alpha."""
    path = ASSET_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Missing asset: {path}")
    return pygame.image.load(str(path)).convert_alpha()


def load_car_collections() -> Tuple[List[pygame.Surface], List[pygame.Surface], List[pygame.Surface], List[pygame.Surface]]:
    pathV = CAR_DIR / "vertical/"
    pathH = CAR_DIR / "horizontal/"
    downCarImages = [load_image(pathV / "downCarRed.png"), load_image(pathV / "downCarGreen.png"), load_image(pathV / "downCarBlue.png")]
    rightCarImages = [load_image(pathH / "rightCarRed.png"), load_image(pathH / "rightCarGreen.png"), load_image(pathH / "rightCarBlue.png")]
    topCarImages = [load_image(pathV / "topCarRed.png"), load_image(pathV / "topCarGreen.png"), load_image(pathV / "topCarBlue.png")]
    leftCarImages = [load_image(pathH / "leftCarRed.png"), load_image(pathH / "leftCarGreen.png"), load_image(pathH / "leftCarBlue.png")]
    return downCarImages, rightCarImages, topCarImages, leftCarImages


def load_center_images() -> Tuple[pygame.Surface, pygame.Surface, pygame.Surface, pygame.Surface]:
    path = CENTER_DIR
    return (load_image(path / "route1.png"), load_image(path / "route2.png"), load_image(path / "route3.png"), load_image(path / "route4.png"))