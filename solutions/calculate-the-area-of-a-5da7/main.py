import math
import os
import json

def get_inputs() -> dict:
    defaults = {"base_length": 10.0, "base_width": 10.0, "slant_height": 5.0}
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
    base_length = float(inputs.get('base_length', 10.0))
    base_width = float(inputs.get('base_width', 10.0))
    slant_height = float(inputs.get('slant_height', 5.0))
    # -----------------------------------------------
    
    # --- CALCULATION SECTION ---
    # Calculate the lateral surface area of the pyramid
    lateral_area = base_length * slant_height + base_width * slant_height
    
    # Calculate the base area of the pyramid
    base_area = base_length * base_width
    
    # Total surface area of the pyramid
    total_area = lateral_area + base_area
    
    print(f"Calculated Result: {total_area}")
    return True

if __name__ == "__main__":
    solve()