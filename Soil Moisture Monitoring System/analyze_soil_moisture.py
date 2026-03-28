from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from statistics import mean

DATA_FILE = Path(__file__).parent / "data" / "soil_moisture_readings.csv"


def load_readings(file_path: Path) -> list[dict[str, str]]:
    with file_path.open("r", newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def summarize(readings: list[dict[str, str]]) -> dict[str, float | int | str]:
    moisture_values = [int(item["moisture_percent"]) for item in readings]
    raw_values = [int(item["sensor_raw"]) for item in readings]
    temperatures = [float(item["temperature_c"]) for item in readings]
    pump_on_count = sum(1 for item in readings if item["pump_state"] == "ON")

    timestamps = [datetime.strptime(item["timestamp"], "%Y-%m-%d %H:%M") for item in readings]
    first_sample = min(timestamps).strftime("%Y-%m-%d %H:%M")
    last_sample = max(timestamps).strftime("%Y-%m-%d %H:%M")

    average_moisture = round(mean(moisture_values), 2)
    moisture_state = "Good"
    if average_moisture < 40:
        moisture_state = "Dry"
    elif average_moisture > 65:
        moisture_state = "Too Wet"

    return {
        "samples": len(readings),
        "avg_moisture": average_moisture,
        "min_moisture": min(moisture_values),
        "max_moisture": max(moisture_values),
        "avg_sensor_raw": round(mean(raw_values), 2),
        "avg_temperature": round(mean(temperatures), 2),
        "pump_on_events": pump_on_count,
        "first_sample": first_sample,
        "last_sample": last_sample,
        "moisture_state": moisture_state,
    }


def main() -> None:
    readings = load_readings(DATA_FILE)
    if not readings:
        raise SystemExit("No readings found in soil_moisture_readings.csv")

    report = summarize(readings)
    print("Soil Moisture Project Summary")
    print("-" * 34)
    print(f"Time range         : {report['first_sample']} to {report['last_sample']}")
    print(f"Total samples      : {report['samples']}")
    print(f"Average moisture   : {report['avg_moisture']}% ({report['moisture_state']})")
    print(f"Moisture range     : {report['min_moisture']}% - {report['max_moisture']}%")
    print(f"Average raw sensor : {report['avg_sensor_raw']}")
    print(f"Average temp       : {report['avg_temperature']}°C")
    print(f"Pump ON events     : {report['pump_on_events']}")


if __name__ == "__main__":
    main()
