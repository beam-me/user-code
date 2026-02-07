import math
import numpy as np
import os
import json

# Constants
GRAVITY = 9.81  # m/s^2

def get_inputs() -> dict:
    defaults = {
        "frame_dimensions": "150x150x50",
        "prototype_material": "PLA",
        "production_material": "carbon fiber",
        "material_properties": "Tensile strength: 500",
        "assembly_method": "snap fit",
        "drone_weight": "250",
        "max_thrust": "1000",
        "frame_thickness": "2",
        "material_yield_strength": "500",
        "material_density": "1600",
        "arm_length": "100",
        "arm_width": "10",
        "tensile_strength_production": "500",
        "yield_strength_production": "500",
        "simulation_method": "Finite element checks",
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
    frame_dimensions = str(inputs.get('frame_dimensions', '150x150x50'))
    prototype_material = str(inputs.get('prototype_material', 'PLA'))
    production_material = str(inputs.get('production_material', 'carbon fiber'))
    material_properties = str(inputs.get('material_properties', 'Tensile strength: 500'))
    assembly_method = str(inputs.get('assembly_method', 'snap fit'))
    drone_weight = float(inputs.get('drone_weight', 250))
    max_thrust = float(inputs.get('max_thrust', 1000))
    frame_thickness = float(inputs.get('frame_thickness', 2))
    material_yield_strength = float(inputs.get('material_yield_strength', 500))
    material_density = float(inputs.get('material_density', 1600))
    arm_length = float(inputs.get('arm_length', 100))
    arm_width = float(inputs.get('arm_width', 10))
    tensile_strength_production = float(inputs.get('tensile_strength_production', 500))
    yield_strength_production = float(inputs.get('yield_strength_production', 500))
    simulation_method = str(inputs.get('simulation_method', 'Finite element checks'))
    gravity = float(inputs.get('gravity', 9.81))
    # -----------------------------------------------
    
    # --- CALCULATION SECTION ---
    # Calculate the force experienced during a 4.2G punch-out
    acceleration_due_to_thrust = 4.2 * GRAVITY  # m/s^2
    force_due_to_thrust = drone_weight * acceleration_due_to_thrust  # N

    # Calculate the cross-sectional area of the frame arms
    arm_cross_sectional_area = arm_width * frame_thickness  # mm^2
    arm_cross_sectional_area_m2 = arm_cross_sectional_area * 1e-6  # convert mm^2 to m^2

    # Calculate stress on the frame arms
    stress_on_arms = force_due_to_thrust / arm_cross_sectional_area_m2  # Pa

    # Check if the stress is within the yield strength of the production material
    if stress_on_arms <= yield_strength_production:
        result = "Frame can handle the 4.2G punch-out acceleration."
    else:
        result = "Frame cannot handle the 4.2G punch-out acceleration."

    print(f"Calculated Result: {result}")
    return True

if __name__ == "__main__":
    solve()