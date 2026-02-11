import math
import os
import json

def get_inputs() -> dict:
    defaults = {"radius": "5"}
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
    radius = float(inputs.get('radius', 5))
    # -----------------------------------------------
    
    # --- CALCULATION SECTION ---
    # Use the variables defined above (e.g. radius)
    
    # Calculate the volume of a sphere (orange) using the formula V = 4/3 * π * r^3
    volume = (4/3) * math.pi * radius**3
    
    print(f"Calculated Result: {volume}")
    return True

if __name__ == "__main__":
    solve()