# Four-Way Traffic Simulation

A modular, optimized, and event-driven simulation of a four-way intersection.
The project visualizes car movement, route switching, traffic-light cycling, and lane behavior using Pygame, with a clean architecture designed for extensibility, performance, and clarity.
## Features

- Circular queue–based traffic light rotation (Auto + Manual mode)
- Four-direction lane system using standalone **Lane** classes
- Timed automatic rotation using **pygame.time.set_timer**
- Sprite-based car rendering with modular movement functions
- Optimized asset folder structure (vertical/horizontal cars, center routes, atlas)
- Configurable constants via **config.py**
- Clean UI for Forward / Backward lane switching and Mode toggling
- Extensible resource management with atlas loading support
- Consistent OOP architecture (Car, Lane, TrafficController)
- Highly maintainable, test-friendly, and performance-oriented codebase

## Folder Structure

```
DSAWithPython/
│
├── src/
│   ├── main.py
│   ├── config.py
│   ├── car.py
│   ├── lane.py
│   ├── circularQueue.py
│   ├── resource.py
│   ├── trafficController.py
│   ├── ui.py
│
├── assets/
│   ├── car/
│   │   ├── vertical/
│   │   └── horizontal/
│   ├── center/
│   ├── atlas/
│
├── docs/
│   └── DSA Project.pptx
│
├── run.bat
├── requirements.txt
└── README.txt

```
## Tech Stack

**Languages**
- Python 3.x

**Libraries / Frameworks**
- Pygame (Rendering, Sprite Movement, Events)
- Pillow (optional: image optimization / atlas generation)

**Tools**
- Windows / Linux / macOS
- Virtual environment (venv)
## Run Locally

**Prerequisites:**
- Python 3.10+
- Pygame installed via requirements.txt

**Steps**

Windows (recommended)
- Open the root folder.
- Run:
    ```bash
    run.bat
    ```
This script:
- Creates a virtual environment if missing
- Installs dependencies
- Runs the game using src/main.py

**Manual run**

Windows

    ```bash
    python -m venv env
    env\Scripts\activate
    pip install -r requirements.txt
    python src/main.py
    ```

Linux / macOS

    ```bash
    python3 -m venv env
    source env/bin/activate
    pip3 install -r requirements.txt
    python3 src/main.py
    ```
## About the Project / Details

This project simulates traffic behavior at a four-way junction using a circular queue and event-driven logic. Each direction of movement is modeled as a separate Lane that contains its own spawn rules, movement functions, and exit conditions.

The **TrafficController** coordinates:

- Auto mode (automatic cycle every N seconds)
- Manual mode (user-controlled direction switching)
- Road state updates

Cars are rendered using **pygame.sprite.Sprite** for high performance and smooth movement. The visual assets are neatly organized into folders such as **car/vertical**, **car/horizontal**, and **center/**.

The architecture is built with scalability in mind:

- Easy to add new lanes
- Easy to modify traffic cycle logic
- Clean separation between visuals, logic, and configuration
- Supports using sprite atlases to reduce texture switching
## License
MIT


## Authors

- [@Niraj Pujari](https://github.com/NirajPujari)

