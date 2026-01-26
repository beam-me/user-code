
# Beam.me Generated Code
# Problem: Calculate torque on a shaft
# Plan: To calculate the torque on a shaft, use the formula: Torque (T) = Force (F) * Distance (d). Here, the force is 10 N and the distance (lever arm) is 0.5 m. Multiply these values to find the torque.

import math
import numpy as np
import os
import json

def get_inputs():
    # Default inputs captured at generation time
    defaults = {"force": 10.0, "distance": 0.5}
    
    # Runtime overrides via environment variable
    env_input = os.environ.get("BEAM_INPUTS")
    if env_input:
        try:
            overrides = json.loads(env_input)
            defaults.update(overrides)
            print(f"Loaded runtime inputs: {overrides.keys()}")
        except Exception as e:
            print(f"Warning: Failed to parse BEAM_INPUTS: {e}")
    
    return defaults

def solve():
    print(f"Solving: Calculate torque on a shaft")
    inputs = get_inputs()
    print(f"Using inputs: {inputs}")
    
    # Mock Calculation Logic
    # (In a real system, the LLM generates specific physics logic here)
    vals = [float(v) for k,v in inputs.items() if isinstance(v, (int, float, str)) and str(v).replace('.','',1).isdigit()]
    
    if len(vals) >= 2:
        result = vals[0] * vals[1]
        print(f"Calculated Result: {result:.4f}")
    elif len(vals) == 1:
        result = vals[0] * 2
        print(f"Calculated Result: {result:.4f}")
    else:
        print("Simulation Complete (No numeric inputs to calc)")
    
    return True

if __name__ == "__main__":
    solve()
