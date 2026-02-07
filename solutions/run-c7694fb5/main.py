import math
import os
import json
from typing import Dict, Any

# Constants
GRAVITY = 9.81

def get_inputs() -> Dict[str, Any]:
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
    punch_out_acceleration = 4.2 * GRAVITY
    force_during_punch_out = drone_weight * punch_out_acceleration
    
    # Check if the frame can handle the force without failing
    frame_cross_sectional_area = arm_width * frame_thickness
    stress_on_frame = force_during_punch_out / frame_cross_sectional_area
    
    # Compare the stress with the yield strength of the production material
    if stress_on_frame < yield_strength_production:
        result = "Frame can handle the punch-out acceleration without failing."
    else:
        result = "Frame cannot handle the punch-out acceleration; redesign needed."
    
    print(f"Calculated Result: {result}")
    return True

if __name__ == "__main__":
    solve()