Smart Dustbin with Speech Feedback & Fullness Prediction 🗑️🧠🔊

An intelligent dustbin system that opens automatically, speaks to users, detects trash level, and predicts when it will be full based on usage patterns.

 🔧 Features
- Auto lid using IR sensor + servo motor
- Trash level detection with ultrasonic sensor
- Voice feedback using DFPlayer Mini
- Fullness prediction using RTC-based logging
- Expandable to cloud/Bluetooth

 🧰 Components
- Arduino UNO / ESP32
- Ultrasonic Sensor (HC-SR04)
- IR Sensor
- DFPlayer Mini MP3 Module + Speaker
- Servo Motor
- DS3231 RTC Module
- Wires, breadboard, 5V power supply

 ⚙️ Circuit Diagram
*(Insert circuit image here)*

 💬 Speech Samples
- `0001.mp3`: Welcome
- `0002.mp3`: Almost Full
- `0003.mp3`: Thank You

📈 Fullness Prediction
System calculates trash fill rate over time using timestamps and predicts when the bin will be 100% full.

🧪 How to Use
1. Upload `smart_dustbin.ino`
2. Add voice files to DFPlayer SD
3. Connect components as per diagram
4. Power up and test

 📦 Future Enhancements
- Mobile alerts via Bluetooth
- IoT support (Google Sheets, Blynk, Firebase)
- E-paper display for status

---

## Additional Projects in this Repo
- `Clock`
- `Line Follower Robot`
- `Automatic Street Light (with LDR)`
- `Soil Moisture Monitoring System` (new)

### Soil Moisture Monitoring System
Path: `Soil Moisture Monitoring System/`
- Arduino controller: `soil_moisture_monitor.ino`
- Dataset: `data/soil_moisture_readings.csv`
- Data analysis script: `analyze_soil_moisture.py`
