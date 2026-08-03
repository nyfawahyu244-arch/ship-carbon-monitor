"""
Sensor Data Collection Module
Handles reading and calibrating telemetry data from maritime IoT exhaust sensors.
"""

import time
import random

class ExhaustSensorReader:
    def __init__(self, sensor_id: str, port: str = "COM3"):
        self.sensor_id = sensor_id
        self.port = port
        self.is_connected = False

    def connect(self) -> bool:
        """Simulate hardware sensor connection."""
        self.is_connected = True
        return self.is_connected

    def read_co2_ppm(self) -> float:
        """Read instantaneous NDIR CO2 sensor data in ppm."""
        base_co2 = 650.0
        fluctuation = random.uniform(-50.0, 150.0)
        return max(400.0, base_co2 + fluctuation)

    def read_exhaust_temp_celsius(self) -> float:
        """Read exhaust temperature from thermocouple in Celsius."""
        return random.uniform(180.0, 350.0)

    def read_engine_rpm(self) -> int:
        """Read engine tachometer speed in RPM."""
        return random.randint(1200, 2200)

    def fetch_telemetry_payload(self) -> dict:
        """Collect all active sensor readings into a unified telemetry packet."""
        return {
            "sensor_id": self.sensor_id,
            "timestamp": time.time(),
            "co2_ppm": round(self.read_co2_ppm(), 2),
            "exhaust_temp_c": round(self.read_exhaust_temp_celsius(), 2),
            "engine_rpm": self.read_engine_rpm(),
        }