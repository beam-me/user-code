import math
import os
import json
from typing import Dict, Any

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
    # Calculate the acceleration during a 4.2G punch-out
    acceleration = 4.2 * gravity  # m/s^2
    
    # Calculate the force experienced by the frame
    force = frame_mass * acceleration  # N (Newton)
    
    # Calculate the stress on the frame
    # Assuming a simple rectangular frame for stress calculation
    width, height, depth = map(float, frame_dimensions.split('x'))
    cross_sectional_area = width * frame_thickness  # mm^2
    stress = force / (cross_sectional_area * 1e-6)  # Convert mm^2 to m^2 for stress in Pascals
    
    # Check if the material can withstand the stress
    can_withstand = stress <= material_strength
    
    # Print the result
    result = "Pass" if can_withstand else "Fail"
    print(f"Calculated Result: {result}")
    
    return True

if __name__ == "__main__":
    solve()