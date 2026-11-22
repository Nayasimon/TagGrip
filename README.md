# TagGrip
 
TagGrip is a DIY VR glove for picking up a cube in Unity. Each finger has a flex sensor, and the cube's position comes from a webcam tracking the AprilTags on its faces.
 
## How it works
 
```
Flex sensors ──► ESP32 ──(USB serial)──┐
                                       ├──► Python bridge ──(UDP)──► Unity
Physical cube ──► Webcam ──────────────┘
```
 
1. **Glove:** five flex sensors, one per finger, are read by an ESP32, which sends the values to the PC over USB.
2. **Python bridge:** reads the glove values, detects the cube's AprilTags (`tag36h11`, IDs 0–5) with OpenCV, solves the cube's pose, and sends everything to Unity over UDP.
3. **Unity:** bends the virtual hand's fingers, moves the virtual cube to match the real one, and lets the hand grab it.
## Files
 
| File | Description |
|---|---|
| `Tag0.png` … `Tag5.png` | AprilTags, one per cube face |
| `camera_test.py` | Webcam tag detection test (start of the Python bridge) |
 
## Hardware
 
- ESP32 (use ADC1 pins, GPIO 32–39)
- 5 flex sensors, each in a voltage divider with a fixed resistor (about 47 kΩ)
- Glove, webcam, and a cube with `Tag0`–`Tag5` printed at the same size
## Calibration
 
Record each finger's raw reading open ($r_{open}$) and in a fist ($r_{closed}$), then map each reading $r$ to a curl value:
 
$$c = \operatorname{clamp}\!\left(\frac{r - r_{open}}{r_{closed} - r_{open}},\ 0,\ 1\right)$$
 
## Quick start
 
```bash
pip install opencv-contrib-python
python camera_test.py
```
 
Change `CAMERA_INDEX` in `camera_test.py` if the wrong camera opens. Press **Q** to quit.
 
