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
        "screwless_assembly_method": "Interlocking parts",
        "max_thrust": "1000",
        "number_of_motors": "4",
        "frame_mass": "250",
        "interlocking_part_dimensions": "10x10x5",
        "material_strength": "500",
        "frame_geometry": "X shaped",
        "carbon_fiber_strength": "500",
        "gravity": 9.81
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
    screwless_assembly_method = str(inputs.get('screwless_assembly_method', 'Interlocking parts'))
    max_thrust = float(inputs.get('max_thrust', 1000))
    number_of_motors = float(inputs.get('number_of_motors', 4))
    frame_mass = float(inputs.get('frame_mass', 250))
    interlocking_part_dimensions = str(inputs.get('interlocking_part_dimensions', '10x10x5'))
    material_strength = float(inputs.get('material_strength', 500))
    frame_geometry = str(inputs.get('frame_geometry', 'X shaped'))
    carbon_fiber_strength = float(inputs.get('carbon_fiber_strength', 500))
    gravity = float(inputs.get('gravity', 9.81))
    # -----------------------------------------------
    
    # --- CALCULATION SECTION ---
    # Calculate the force experienced during a 4.2G punch-out
    acceleration_due_to_punch_out = 4.2 * GRAVITY  # m/s^2
    force_on_frame = frame_mass * acceleration_due_to_punch_out  # Newtons

    # Check if the frame can handle the force
    # Assume the production material is Carbon Fiber for final production
    if production_material == "Carbon Fiber":
        material_strength = carbon_fiber_strength

    can_withstand_force = force_on_frame <= material_strength

    # Print the result
    print(f"Calculated Result: {can_withstand_force}")
    return True

if __name__ == "__main__":
    solve()