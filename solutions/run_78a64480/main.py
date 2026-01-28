import math
import numpy as np
import os
import json

def get_inputs():
    defaults = {"radius": "50"}
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
    # CAST VARIABLES HERE
    radius = float(inputs.get("radius", 0))
    
    # LOGIC HERE
    area = math.pi * radius**2
    print(f"Calculated Result: {area}")
    return True

if __name__ == "__main__":
    solve()