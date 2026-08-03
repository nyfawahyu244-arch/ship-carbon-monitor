"""
Example Execution Script for Ship Carbon Monitor System
Demonstrates reading telemetry and running predictive carbon models.
"""

import sys
import os
import time

# Add src folder to module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sensors import ExhaustSensorReader
from src.models import CarbonEmissionModel
from src.config import TELEMETRY_INTERVAL_SECONDS, CRITICAL_CO2_PPM_THRESHOLD

def main():
    print("==================================================")
    print(" 🚢 Ship Carbon Monitor - Real-Time Demo ")
    print("==================================================\n")

    # Initialize sensor reader & ML prediction model
    sensor = ExhaustSensorReader(sensor_id="VESSEL-TEST-01")
    model = CarbonEmissionModel(fuel_type="Marine Heavy Fuel Oil (HFO)")

    if sensor.connect():
        print("[INFO] Sensors successfully connected and calibrated.\n")

    # Simulate running 5 real-time telemetry polling loops
    total_co2_kg = 0.0
    iterations = 5

    for i in range(1, iterations + 1):
        telemetry = sensor.fetch_telemetry_payload()
        emissions = model.estimate_instantaneous_emission(telemetry)

        print(f"--- Telemetry Sample #{i} ---")
        print(f"  • Engine Speed : {telemetry['engine_rpm']} RPM")
        print(f"  • CO2 Reading  : {telemetry['co2_ppm']} ppm")
        print(f"  • Exhaust Temp : {telemetry['exhaust_temp_c']} °C")
        print(f"  • CO2 Emission : {emissions['co2_kg_per_hour']} kg/hr")
        print(f"  • Fuel Burn    : {emissions['estimated_fuel_burn_lph']} L/hr")

        if telemetry['co2_ppm'] > CRITICAL_CO2_PPM_THRESHOLD:
            print("  ⚠️ [ALERT] High CO2 concentration threshold exceeded!")

        total_co2_kg += emissions['co2_kg_per_hour'] / 3600.0 * TELEMETRY_INTERVAL_SECONDS
        time.sleep(1)

    print("\n--------------------------------------------------")
    # Predict 24-hour voyage footprint using average emission rate
    avg_emission_rate = emissions['co2_kg_per_hour']
    voyage_footprint_tons = model.predict_voyage_footprint(avg_emission_rate, duration_hours=24.0)

    print(f"📈 Estimated 24-Hour Voyage Footprint: {voyage_footprint_tons} Metric Tons CO2")
    print("==================================================")

if __name__ == "__main__":
    main()