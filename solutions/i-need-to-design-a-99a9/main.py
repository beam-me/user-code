import math
import numpy as np
import os
import json

# Constants
GRAVITY = 9.81  # m/s^2
AIR_DENSITY = 1.225  # kg/m^3 at sea level
FT_TO_M = 0.3048  # conversion factor from feet to meters
LBS_TO_KG = 0.453592  # conversion factor from pounds to kilograms
MPH_TO_MPS = 0.44704  # conversion factor from mph to m/s

def get_inputs() -> dict:
    defaults = {
        "gross_weight_lbs": 25,
        "propeller_disc_area_ft2": 8.0,
        "cruise_speed_mph": 50
    }
    env_input = os.environ.get("BEAM_INPUTS")
    if env_input:
        try:
            overrides = json.loads(env_input)
            defaults.update(overrides)
        except Exception:
            pass
    return defaults

def solve() -> bool:
    inputs = get_inputs()
    
    # --- MANDATORY CASTING BLOCK (DO NOT MODIFY) ---
    gross_weight_lbs = inputs["gross_weight_lbs"]
    propeller_disc_area_ft2 = inputs["propeller_disc_area_ft2"]
    cruise_speed_mph = inputs["cruise_speed_mph"]
    # -----------------------------------------------
    
    # Convert inputs to SI units
    gross_weight_kg = gross_weight_lbs * LBS_TO_KG
    propeller_disc_area_m2 = propeller_disc_area_ft2 * (FT_TO_M ** 2)
    cruise_speed_mps = cruise_speed_mph * MPH_TO_MPS
    
    # --- CALCULATION SECTION ---
    
    # 1. Calculate the required Hover Power (kW)
    hover_power_watts = (gross_weight_kg * GRAVITY) ** 1.5 / math.sqrt(2 * AIR_DENSITY * propeller_disc_area_m2)
    hover_power_kw = hover_power_watts / 1000  # Convert to kW
    
    # 2. Estimate the Aerodynamic Drag at 50 mph
    drag_coefficient = 1.0  # Assumed drag coefficient for a quadcopter
    frontal_area_m2 = 0.5  # Assumed frontal area in m^2
    drag_force_newtons = 0.5 * AIR_DENSITY * cruise_speed_mps**2 * drag_coefficient * frontal_area_m2
    
    # 3. Calculate the Dynamic Pressure (q)
    dynamic_pressure = 0.5 * AIR_DENSITY * cruise_speed_mps**2
    
    # Print results
    print(f"Calculated Result: Hover Power = {hover_power_kw:.2f} kW")
    print(f"Calculated Result: Aerodynamic Drag = {drag_force_newtons:.2f} N")
    print(f"Calculated Result: Dynamic Pressure = {dynamic_pressure:.2f} Pa")
    
    return True

if __name__ == "__main__":
    solve()