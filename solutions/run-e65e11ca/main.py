import math
import numpy as np
import os
import json

def get_inputs():
    defaults = {"base_length": "12", "base_width": "5", "slant_height": "4"}
    env_input = os.environ.get("BEAM_INPUTS")
    if env_input:
        try:
            overrides = json.loads(env_input)
            defaults.update(overrides)
        except Exception:
            pass
    return defaults

def solve():
    inputs = get_inputs()
    
    # --- MANDATORY CASTING BLOCK (DO NOT MODIFY) ---
    base_length = float(inputs.get('base_length', 12))
    base_width = float(inputs.get('base_width', 5))
    slant_height = float(inputs.get('slant_height', 4))
    # -----------------------------------------------
    
    # --- CALCULATION SECTION ---
    # Calculate the area of the pyramid
    base_area = base_length * base_width
    perimeter = 2 * (base_length + base_width)
    lateral_area = 0.5 * perimeter * slant_height
    total_area = base_area + lateral_area
    
    print(f"Calculated Result: {total_area}")
    return True

if __name__ == "__main__":
    solve()