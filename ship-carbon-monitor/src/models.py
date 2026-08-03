"""
AI & Emission Predictive Modeling Module
Processes IoT telemetry to estimate and forecast ship carbon output.
"""

from typing import Dict, Any

class CarbonEmissionModel:
    def __init__(self, fuel_type: str = "Marine Heavy Fuel Oil (HFO)"):
        self.fuel_type = fuel_type
        # Default emission factor (kg CO2 per liter fuel equivalent)
        self.emission_factor = 3.114 if "HFO" in fuel_type else 2.68

    def estimate_instantaneous_emission(self, telemetry_data: Dict[str, Any]) -> Dict[str, float]:
        """
        Calculate instantaneous CO2 emissions (kg/hr) based on RPM and CO2 sensor readings.
        """
        rpm = telemetry_data.get("engine_rpm", 0)
        co2_ppm = telemetry_data.get("co2_ppm", 400.0)
        temp_c = telemetry_data.get("exhaust_temp_c", 200.0)

        # Empirical estimation model for marine diesel engines
        load_factor = rpm / 2500.0  # Normalize against max rated RPM
        flow_rate_factor = 1.0 + (temp_c / 1000.0)
        
        # Estimated emissions in kilograms of CO2 per hour (kg/h)
        co2_kg_per_hour = (co2_ppm * 0.0008) * (load_factor ** 1.5) * flow_rate_factor * self.emission_factor * 10.0

        return {
            "co2_kg_per_hour": round(co2_kg_per_hour, 3),
            "estimated_fuel_burn_lph": round(co2_kg_per_hour / self.emission_factor, 2),
            "engine_load_pct": round(load_factor * 100, 1)
        }

    def predict_voyage_footprint(self, avg_emission_kg_h: float, duration_hours: float) -> float:
        """Predict total carbon footprint for a projected voyage duration in Metric Tons."""
        total_kg = avg_emission_kg_h * duration_hours
        return round(total_kg / 1000.0, 3)