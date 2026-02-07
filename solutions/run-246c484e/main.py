import math
import os
import json

# Constants
GRAVITY = 9.81  # m/s^2

def get_inputs() -> dict:
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
    # Calculate the total thrust
    total_thrust = max_thrust * number_of_motors
    
    # Calculate the required force to withstand a 4.2G punch-out
    required_force = frame_mass * 4.2 * GRAVITY
    
    # Check if the frame can handle the required force
    can_withstand = required_force <= material_strength
    
    # Print the result
    print(f"Calculated Result: {'Can withstand' if can_withstand else 'Cannot withstand'}")
    
    return True

if __name__ == "__main__":
    solve()