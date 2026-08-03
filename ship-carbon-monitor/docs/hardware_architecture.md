# Hardware & System Architecture

This document details the physical hardware setup and sensor integration for the **Ship Carbon Monitor** system.

---

## 🔌 Sensor & Hardware Components

| Component | Model / Specification | Function / Purpose |
| :--- | :--- | :--- |
| **Microcontroller** | ESP32-WROOM-32U / Raspberry Pi 4 | Central processing, Wi-Fi/4G telemetry transmission, and local buffering. |
| **NDIR CO2 Sensor** | MH-Z19C or Senseair S8 | Non-dispersive infrared detection of exhaust CO2 concentration (0–5000 ppm). |
| **Temperature Sensor** | MAX6675 Thermocouple Module | High-temperature measurement of engine exhaust gases (up to 1000°C). |
| **Engine Tachometer** | Hall Effect Sensor / Optical Pickup | Measures engine flywheel rotation (RPM) to compute engine load factor. |
| **Power Supply** | 12V-24V DC to 5V 3A Buck Converter | Marine battery / vessel power interface with surge protection. |

---

## 📐 Wiring & Interface Diagram