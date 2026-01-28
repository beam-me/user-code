import math
import os
import json

def get_inputs():
    defaults = {"radius": "10"}
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
    
    # --- MANDATORY CASTING BLOCK ---
    radius = float(inputs.get('radius', 10))
    # -------------------------------
    
    # --- CALCULATION SECTION ---
    area = math.pi * radius ** 2
    
    print(f"Calculated Result: {area}")
    return True

if __name__ == "__main__":
    solve()