import math
import os
import json

# Constants
GRAVITY = 9.81  # m/s^2
AIR_DENSITY = 1.225  # kg/m^3 at sea level

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
    
    # --- CALCULATION SECTION ---
    # Convert units
    gross_weight_kg = gross_weight_lbs * 0.453592
    propeller_disc_area_m2 = propeller_disc_area_ft2 * 0.092903
    cruise_speed_mps = cruise_speed_mph * 0.44704
    
    # Calculate Hover Power
    hover_power_watts = (gross_weight_kg * GRAVITY) ** 1.5 / math.sqrt(2 * AIR_DENSITY * propeller_disc_area_m2)
    hover_power_kw = hover_power_watts / 1000  # Convert to kW
    
    # Calculate Dynamic Pressure
    dynamic_pressure = 0.5 * AIR_DENSITY * cruise_speed_mps ** 2
    
    # Estimate Aerodynamic Drag
    drag_coefficient = 1.0  # Assumed value for a quadcopter
    drag_force = drag_coefficient * dynamic_pressure * propeller_disc_area_m2
    
    # Print results
    print(f"Calculated Result: Hover Power = {hover_power_kw:.2f} kW")
    print(f"Calculated Result: Dynamic Pressure = {dynamic_pressure:.2f} Pa")
    print(f"Calculated Result: Aerodynamic Drag = {drag_force:.2f} N")
    
    return True

if __name__ == "__main__":
    solve()