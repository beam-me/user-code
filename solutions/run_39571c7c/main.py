import math
import numpy as np
import os
import json

def get_inputs():
    defaults = {"radius": 1.0}
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
    radius = inputs["radius"]
    area = math.pi * radius**2
    print(f"Calculated Result: {area}")
    return True

if __name__ == "__main__":
    solve()