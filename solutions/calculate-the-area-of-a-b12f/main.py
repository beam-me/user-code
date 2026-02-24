import math
import os
import json
from typing import Dict, Any

def get_inputs() -> Dict[str, Any]:
    defaults = {}
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
    base_length = float(inputs.get("base_length", 0))
    base_width = float(inputs.get("base_width", 0))
    slant_height = float(inputs.get("slant_height", 0))
    # -----------------------------------------------
    
    # --- CALCULATION SECTION ---
    # Use the variables defined above (e.g. base_length, base_width, slant_height)
    
    # Calculate the area of the base
    base_area = base_length * base_width
    
    # Calculate the lateral surface area
    lateral_area = base_length * slant_height + base_width * slant_height
    
    # Total surface area of the pyramid
    total_area = base_area + lateral_area
    
    print(f"Calculated Result: {total_area}")
    return True

if __name__ == "__main__":
    solve()