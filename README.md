# Mini Projects Collection (Arduino + Embedded Systems)

A cleaned-up and production-ready collection of beginner-to-intermediate embedded projects.

## Included Projects

| Project | Status | Highlights |
|---|---|---|
| Smart Dustbin with Speech Feedback and Fullness Prediction | ✅ Refined | Auto lid, ultrasonic fill level, DFPlayer voice prompts, cooldown/debounce logic |
| Line Follower Robot | ✅ Refined | Stable turn behavior, helper functions, configurable motor speed |
| Automatic Street Light (with LDR) | ✅ Refined | Smoothed sensor reading, hysteresis thresholding, serial debug output |
| Clock (RTC + I2C LCD) | ✅ Refined | Better formatting, leading zeros, RTC power-loss recovery, LCD line cleanup |

---

## Repo Layout

> Note: project source files are stored with descriptive file names at the repository root.

- `Smart Dustbin with Speech Feedback and Fullness Prediction`
- `Line Follower Robot`
- `Automatic Street Light (with LDR)`
- `Clock`

---

## Quick Start

1. Open the relevant project file in **Arduino IDE**.
2. Select your board and COM port.
3. Install required libraries (if applicable):
   - `RTClib`
   - `LiquidCrystal_I2C`
   - `Servo`
   - `SoftwareSerial`
4. Upload code and open Serial Monitor for diagnostics where supported.

---

## Debug and Quality Improvements Added

- Improved readability (named constants, helper functions, comments).
- Added noise handling / anti-flicker behavior where sensor values can fluctuate.
- Added safer defaults and state tracking for moving parts (e.g., servo lid state).
- Added clearer serial diagnostics to simplify physical debugging on hardware.

---

## Suggested Next Steps

- Split each project into its own folder with `*.ino` and project-specific `README.md`.
- Add wiring diagrams and photos.
- Add calibration notes per sensor/module for reproducible builds.
