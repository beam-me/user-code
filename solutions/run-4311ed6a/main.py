import math
import numpy as np
import os
import json

GRAVITY = 9.81  # m/s^2

def get_inputs() -> dict:
    defaults = {
        "frame_dimensions": "150x150x5",
        "prototype_material": "PLA",
        "production_material": "carbon fiber",
        "max_thrust": "494",
        "motor_count": "4",
        "assembly_method": "interlocking joints",
        "frame_mass": "250",
        "interlocking_joint_design": "basic slot and tab",
        "carbon_fiber_tensile_strength": "600",
        "carbon_fiber_modulus_of_elasticity": "70",
        "mass_distribution": "evenly",
        "structural_design_details": "standard beam thickness with reinforced joints",
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
    frame_dimensions = str(inputs.get('frame_dimensions', '150x150x5'))
    prototype_material = str(inputs.get('prototype_material', 'PLA'))
    production_material = str(inputs.get('production_material', 'carbon fiber'))
    max_thrust = float(inputs.get('max_thrust', 494))
    motor_count = float(inputs.get('motor_count', 4))
    assembly_method = str(inputs.get('assembly_method', 'interlocking joints'))
    frame_mass = float(inputs.get('frame_mass', 250))
    interlocking_joint_design = str(inputs.get('interlocking_joint_design', 'basic slot and tab'))
    carbon_fiber_tensile_strength = float(inputs.get('carbon_fiber_tensile_strength', 600))
    carbon_fiber_modulus_of_elasticity = float(inputs.get('carbon_fiber_modulus_of_elasticity', 70))
    mass_distribution = str(inputs.get('mass_distribution', 'evenly'))
    structural_design_details = str(inputs.get('structural_design_details', 'standard beam thickness with reinforced joints'))
    gravity = float(inputs.get('gravity', 9.81))
    # -----------------------------------------------
    
    # --- CALCULATION SECTION ---
    # Calculate the total thrust
    total_thrust = max_thrust * motor_count
    
    # Calculate the maximum acceleration the frame should withstand
    max_acceleration = 4.2 * GRAVITY  # 4.2G punch-out acceleration
    
    # Calculate the force exerted on the frame during max acceleration
    force_on_frame = frame_mass * max_acceleration
    
    # Check if the frame can handle the force without failing
    can_withstand_force = total_thrust >= force_on_frame
    
    # Print the result
    print(f"Calculated Result: {can_withstand_force}")
    
    return True

if __name__ == "__main__":
    solve()