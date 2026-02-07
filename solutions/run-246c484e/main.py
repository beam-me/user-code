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
    # Calculate the required thrust to achieve 4.2G acceleration
    required_thrust = frame_mass * (4.2 * GRAVITY)
    
    # Check if the total thrust from all motors can achieve this acceleration
    total_available_thrust = max_thrust * number_of_motors
    
    # Determine if the frame can handle the required thrust
    can_handle_thrust = total_available_thrust >= required_thrust
    
    # Calculate the stress on the frame using the production material
    stress_on_frame = required_thrust / (float(frame_dimensions.split('x')[0]) * float(frame_dimensions.split('x')[1]))
    
    # Check if the material strength is sufficient
    is_material_sufficient = stress_on_frame <= carbon_fiber_strength
    
    # Final result: Can the frame handle the 4.2G acceleration without failing?
    result = can_handle_thrust and is_material_sufficient
    
    print(f"Calculated Result: {result}")
    return True

if __name__ == "__main__":
    solve()