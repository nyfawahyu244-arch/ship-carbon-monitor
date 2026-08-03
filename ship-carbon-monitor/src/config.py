"""
Configuration & Environment Parameters Module
Centralized constants, sensor pins, thresholds, and operational limits.
"""

# Hardware & Telemetry Settings
BAUD_RATE = 115200
DEFAULT_SENSOR_PORT = "/dev/ttyUSB0"
TELEMETRY_INTERVAL_SECONDS = 2.0

# Engine & Emission Thresholds
MAX_RATED_RPM = 2500
CRITICAL_CO2_PPM_THRESHOLD = 2000.0
MAX_EXHAUST_TEMP_CELSIUS = 450.0

# MQTT Telemetry Broker Configuration
MQTT_BROKER_URL = "telemetry.marine-carbon.org"
MQTT_PORT = 1883
MQTT_TOPIC_EMISSIONS = "vessel/telemetry/emissions"

# Supported Marine Fuel Types
SUPPORTED_FUELS = {
    "HFO": "Heavy Fuel Oil",
    "MGO": "Marine Gas Oil",
    "LNG": "Liquefied Natural Gas"
}