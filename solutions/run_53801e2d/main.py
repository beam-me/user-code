
# Beam.me Generated Code
# Problem: I need an I-beam that will hold 3000 pounds at one end, it's cantilevered, and it is 10 feet long. I'm looking for it to be made out of standard mild steel. 

# Plan: To determine if the I-beam can support the load, we will calculate the maximum bending stress using the formula: stress = (load * length) / moment_of_inertia. We will then compare this stress to the yield strength of the material to ensure it is within safe limits. Additionally, we will calculate the deflection at the end of the beam using the formula: deflection = (load * length^3) / (3 * youngs_modulus * moment_of_inertia) to ensure it is within acceptable limits.

import math
import numpy as np
import os
import json

def get_inputs():
    # Default inputs captured at generation time
    defaults = {"load": 3000, "length": 10, "yield_strength": 36000, "youngs_modulus": 29000000, "moment_of_inertia": 75}
    
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
    print(f"Solving: I need an I-beam that will hold 3000 pounds at one end, it's cantilevered, and it is 10 feet long. I'm looking for it to be made out of standard mild steel. 
")
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
