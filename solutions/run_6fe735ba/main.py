import math
import numpy as np
import os
import json

def get_inputs():
    defaults = {"force": 10.0, "distance": 1.0}
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
    force = inputs["force"]
    distance = inputs["distance"]
    
    # Calculate torque
    torque = force * distance
    
    print(f"Calculated Result: {torque}")
    return True

if __name__ == "__main__":
    solve()