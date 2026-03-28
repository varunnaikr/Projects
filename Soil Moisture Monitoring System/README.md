# Soil Moisture Monitoring System 🌱💧

This project reads soil moisture values from a sensor, controls a water pump relay, and logs sample data for analysis.

## Features
- Real-time soil moisture monitoring using analog sensor values.
- Automatic pump control when soil becomes dry.
- Moisture percentage estimation for easier interpretation.
- Example dataset for trend checks and reports.
- Python script that summarizes moisture, temperature, pump usage, and sample time range.

## Project Files
- `soil_moisture_monitor.ino` → Arduino sketch for moisture reading + pump control.
- `data/soil_moisture_readings.csv` → Sample recent readings.
- `analyze_soil_moisture.py` → Data summary script.

## Hardware
- Arduino UNO / Nano
- Capacitive or resistive soil moisture sensor
- Relay module + mini water pump
- Jumper wires + 5V power source

## How to Use
1. Upload `soil_moisture_monitor.ino` to your Arduino.
2. Connect moisture sensor signal to `A0` and relay input to pin `8`.
3. Open Serial Monitor at `9600 baud`.
4. Run data analysis:
   ```bash
   python3 analyze_soil_moisture.py
   ```

## Calibration Note
Sensor values vary by sensor type and soil conditions. Adjust `dryThreshold` and `wetThreshold` in the Arduino sketch based on your readings.
