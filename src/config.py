from pathlib import Path

WINDOW_WIDTH: int = 1500
WINDOW_HEIGHT: int = 1000
FPS: int = 60
CAR_SPEED: int = 3
AUTO_DURATION_SECONDS: float = 3.0  # seconds between auto-rotations
BASE_DIR = Path(__file__).resolve().parent.parent
ASSET_DIR = BASE_DIR / "assets"
SPAWN_CHANCE_INV: int = 100  # 1 in 100 chance per tick
HORIZONTAL_ROAD_RECT = (0, 405, 1500, 220)
VERTICAL_ROAD_RECT = (650, 0, 200, 1000)
CAR_DIR = ASSET_DIR / "car"
CENTER_DIR = ASSET_DIR / "center"