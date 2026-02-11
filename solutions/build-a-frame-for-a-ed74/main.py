import math
import os
import json
from typing import Dict, Any

# Constants
GRAVITY = 9.81  # m/s^2, gravitational constant
DT = 0.01  # s, time step for simulations

def get_inputs() -> Dict[str, Any]:
    defaults = {
        "frame_material": "carbon_fiber",
        "arm_length": 125.0,  # mm
        "arm_thickness": 4.0,  # mm
        "frame_weight": 100.0  # grams
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
    frame_material = inputs.get("frame_material")
    arm_length = float(inputs.get("arm_length"))
    arm_thickness = float(inputs.get("arm_thickness"))
    frame_weight = float(inputs.get("frame_weight"))
    # -----------------------------------------------
    
    # --- CALCULATION SECTION ---
    # Calculate the moment of inertia for the arms
    # Assuming the arms are rectangular beams
    arm_length_m = arm_length / 1000.0  # convert mm to meters
    arm_thickness_m = arm_thickness / 1000.0  # convert mm to meters
    
    # Moment of inertia for a rectangular beam: I = (1/12) * width * height^3
    # Assuming width is equal to thickness for simplicity
    moment_of_inertia = (1/12) * arm_thickness_m * (arm_thickness_m ** 3)
    
    # Calculate the total weight of the frame in Newtons
    frame_weight_newtons = frame_weight * GRAVITY / 1000.0  # convert grams to kg
    
    # Print the calculated result
    result = {
        "moment_of_inertia": moment_of_inertia,
        "frame_weight_newtons": frame_weight_newtons
    }
    print(f"Calculated Result: {result}")
    return True

if __name__ == "__main__":
    solve()