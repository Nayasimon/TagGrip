# TagGrip

TagGrip is a DIY VR glove for picking up a cube in a Unity simulation.

## Overview

- **Glove:** one flex sensor per finger, connected to an ESP32.
- **Cube:** a physical cube with an AprilTag on each face.
- **Unity:** a simulated hand that can pick up a cube.

## Files

| File | Description |
|---|---|
| `Tag0.png` … `Tag5.png` | AprilTags for the cube faces |
| `camera_test.py` | Detects the AprilTags from a webcam and shows their IDs |

## Running the camera test

```bash
pip install opencv-contrib-python
python camera_test.py
```

Change `CAMERA_INDEX` in `camera_test.py` if the wrong camera opens. Press **Q** to quit.
