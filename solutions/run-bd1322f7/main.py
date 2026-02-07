import math
import os
import json
from typing import Dict, Any

# Constants
GRAVITY = 9.81  # m/s^2

def get_inputs() -> Dict[str, Any]:
    defaults = {
        "frame_dimensions": "150x150x10",
        "prototype_material": "PLA",
        "production_material": "Carbon Fiber",
        "material_density": "1600",
        "max_thrust": "500",
        "frame_mass": "250",
        "frame_thickness": "10",
        "material_strength": "500",
        "joining_method": "snap-fit",
        "gravity": GRAVITY
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
    frame_dimensions = str(inputs.get('frame_dimensions', '150x150x10'))
    prototype_material = str(inputs.get('prototype_material', 'PLA'))
    production_material = str(inputs.get('production_material', 'Carbon Fiber'))
    material_density = float(inputs.get('material_density', 1600))
    max_thrust = float(inputs.get('max_thrust', 500))
    frame_mass = float(inputs.get('frame_mass', 250))
    frame_thickness = float(inputs.get('frame_thickness', 10))
    material_strength = float(inputs.get('material_strength', 500))
    joining_method = str(inputs.get('joining_method', 'snap-fit'))
    gravity = float(inputs.get('gravity', 9.81))
    # -----------------------------------------------
    
    # --- CALCULATION SECTION ---
    # Calculate the acceleration due to thrust
    thrust_acceleration = max_thrust / frame_mass  # in m/s^2
    
    # Calculate the total acceleration during a 4.2G punch-out
    punch_out_acceleration = 4.2 * gravity  # in m/s^2
    
    # Ensure the frame can handle the punch-out acceleration
    can_handle_punch_out = punch_out_acceleration <= material_strength / material_density
    
    # Print the result
    print(f"Calculated Result: {can_handle_punch_out}")
    
    return True

if __name__ == "__main__":
    solve()