import math
import os
import json

# Constants
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
    # Calculate the force experienced during a 4.2G punch-out
    acceleration_due_to_punch_out = 4.2 * gravity  # m/s^2
    force_on_frame = frame_mass * acceleration_due_to_punch_out  # N

    # Check if the frame can handle this force
    # Assuming a simple model where the tensile strength is the limiting factor
    # Convert frame dimensions from string to numerical values
    dimensions = list(map(float, frame_dimensions.split('x')))
    cross_sectional_area = dimensions[0] * dimensions[1]  # mm^2 to m^2 conversion needed

    # Convert mm^2 to m^2 for cross-sectional area
    cross_sectional_area_m2 = cross_sectional_area * 1e-6

    # Calculate the stress on the frame
    stress_on_frame = force_on_frame / cross_sectional_area_m2  # N/m^2

    # Check if the stress is within the tensile strength of the production material
    if stress_on_frame <= carbon_fiber_tensile_strength * 1e6:  # Convert MPa to N/m^2
        result = "Frame can handle the 4.2G punch-out acceleration."
    else:
        result = "Frame cannot handle the 4.2G punch-out acceleration."

    print(f"Calculated Result: {result}")
    return True

if __name__ == "__main__":
    solve()