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

def calculate_hover_power(gross_weight_kg: float, propeller_disc_area_m2: float) -> float:
    # Calculate the hover power required in watts
    hover_power_watts = (gross_weight_kg * GRAVITY) ** 1.5 / math.sqrt(2 * AIR_DENSITY * propeller_disc_area_m2)
    hover_power_kw = hover_power_watts / 1000  # Convert to kilowatts
    return hover_power_kw

def calculate_aerodynamic_drag(cruise_speed_mps: float, drag_coefficient: float, frontal_area_m2: float) -> float:
    # Calculate the aerodynamic drag force in newtons
    drag_force = 0.5 * AIR_DENSITY * cruise_speed_mps**2 * drag_coefficient * frontal_area_m2
    return drag_force

def calculate_dynamic_pressure(cruise_speed_mps: float) -> float:
    # Calculate the dynamic pressure in pascals
    dynamic_pressure = 0.5 * AIR_DENSITY * cruise_speed_mps**2
    return dynamic_pressure

def solve() -> bool:
    inputs = get_inputs()
    
    # --- MANDATORY CASTING BLOCK (DO NOT MODIFY) ---
    gross_weight_lbs = inputs["gross_weight_lbs"]
    propeller_disc_area_ft2 = inputs["propeller_disc_area_ft2"]
    cruise_speed_mph = inputs["cruise_speed_mph"]
    # -----------------------------------------------
    
    # Convert inputs to SI units
    gross_weight_kg = gross_weight_lbs * 0.453592
    propeller_disc_area_m2 = propeller_disc_area_ft2 * 0.092903
    cruise_speed_mps = cruise_speed_mph * 0.44704
    
    # --- CALCULATION SECTION ---
    hover_power_kw = calculate_hover_power(gross_weight_kg, propeller_disc_area_m2)
    
    # Assume a drag coefficient and frontal area for the quadcopter
    drag_coefficient = 1.0  # Assumed value
    frontal_area_m2 = 0.5  # Assumed value in square meters
    
    aerodynamic_drag = calculate_aerodynamic_drag(cruise_speed_mps, drag_coefficient, frontal_area_m2)
    dynamic_pressure = calculate_dynamic_pressure(cruise_speed_mps)
    
    # Print results
    print(f"Calculated Result: Hover Power = {hover_power_kw:.2f} kW")
    print(f"Calculated Result: Aerodynamic Drag = {aerodynamic_drag:.2f} N")
    print(f"Calculated Result: Dynamic Pressure = {dynamic_pressure:.2f} Pa")
    
    return True

if __name__ == "__main__":
    solve()