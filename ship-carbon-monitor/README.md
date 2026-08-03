# 🚢 Marine Vessel Real-Time Carbon Emission Monitoring System

> An open-source IoT and AI-driven telemetry system engineered to measure, model, and monitor real-time carbon emissions from ship engines.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Status-Research%20Prototype-brightgreen)

---

## 📌 Project Overview

Maritime emissions contribute significantly to global greenhouse gases, yet high-cost monitoring solutions leave many vessel operators relying on manual estimates. 

This project provides an affordable, open-source hardware and software stack combining **IoT telemetry sensors** and **AI predictive modeling** to continuously track exhaust gas parameters and calculate real-time carbon footprints ($CO_2$ / $CO$ / particulate output).

*Built and architected with the assistance of **Claude Code**.*

---

## ✨ Key Features

- **Real-Time Sensor Telemetry:** Interface with exhaust gas sensors (MQ series, NDIR $CO_2$, temperature, engine RPM).
- **Edge Computing & Processing:** Microcontroller firmware designed for low-power edge data processing.
- **AI-Based Emission Estimator:** Machine learning models for predicting instantaneous carbon output based on engine load and fuel consumption.
- **Open Standards:** Open hardware schematics and extensible Python APIs for marine researchers.

---

## 🛠 Tech Stack

- **Hardware:** ESP32 / Raspberry Pi, NDIR $CO_2$ Sensors, Exhaust Gas Telemetry.
- **Software:** Python 3.10+, Pandas, NumPy, Scikit-learn.
- **Protocol:** MQTT / HTTP telemetry reporting.

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone [https://github.com/USERNAME_ANDA/ship-carbon-monitor.git](https://github.com/USERNAME_ANDA/ship-carbon-monitor.git)
cd ship-carbon-monitor