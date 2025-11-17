from pathlib import Path

# Window & rendering
WINDOW_WIDTH: int = 1500
WINDOW_HEIGHT: int = 1000
FPS: int = 60

# Gameplay / simulation
CAR_SPEED: int = 3
AUTO_DURATION_SECONDS: float = 3.0  # seconds between auto-rotations

# Assets
BASE_DIR: Path = Path(__file__).parent
PUBLIC_DIR: Path = BASE_DIR / "public"

# Spawn config
SPAWN_CHANCE_INV: int = 100  # 1 in 100 chance per tick

# UI / layout constants
HORIZONTAL_ROAD_RECT = (0, 405, 1500, 220)
VERTICAL_ROAD_RECT = (650, 0, 200, 1000)
