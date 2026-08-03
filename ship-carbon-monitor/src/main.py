# Marine Carbon Emission Telemetry Prototype
import time
import random

def read_sensor_data():
    # Simulated NDIR CO2 and engine load reading
    co2_ppm = random.uniform(400, 1200)
    engine_rpm = random.randint(1000, 2500)
    return co2_ppm, engine_rpm

def calculate_carbon_footprint(co2_ppm, engine_rpm):
    # Simplified emission modeling algorithm
    estimated_emissions_kg_h = (co2_ppm * 0.001) * (engine_rpm / 1000) * 0.45
    return round(estimated_emissions_kg_h, 2)

if __name__ == "__main__":
    print("Starting Vessel Carbon Emission Telemetry Unit...")
    try:
        while True:
            co2, rpm = read_sensor_data()
            emission = calculate_carbon_footprint(co2, rpm)
            print(f"[Telemetry Data] Engine RPM: {rpm} | CO2 Sensor: {co2:.1f} ppm | Est. Emissions: {emission} kg/h")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")