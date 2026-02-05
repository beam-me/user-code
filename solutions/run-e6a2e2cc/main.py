import math
import numpy as np
import os
import json

def get_inputs():
    defaults = {"drone_weight": "4", "payload_weight": "1", "battery_capacity": "4993", "max_wind_speed": "15", "obstacle_detection_range": "3", "drop_accuracy": "4", "simulation_environment": "Gazebo", "drone_dimensions": ".5x.5.1", "motor_specifications": "1000g thrust", "flight_control_system": "px4", "environmental_conditions": "25C 100% humidity", "communication_system": "2.4ghz radio", "camera_system": "lidar", "target_distance": "100", "rooftop_height": "10", "precision_requirement": "-4"}
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
    drone_weight = float(inputs.get('drone_weight', 4))
    payload_weight = float(inputs.get('payload_weight', 1))
    battery_capacity = float(inputs.get('battery_capacity', 4993))
    max_wind_speed = float(inputs.get('max_wind_speed', 15))
    obstacle_detection_range = float(inputs.get('obstacle_detection_range', 3))
    drop_accuracy = float(inputs.get('drop_accuracy', 4))
    simulation_environment = str(inputs.get('simulation_environment', 'Gazebo'))
    drone_dimensions = str(inputs.get('drone_dimensions', '.5x.5.1'))
    motor_specifications = str(inputs.get('motor_specifications', '1000g thrust'))
    flight_control_system = str(inputs.get('flight_control_system', 'px4'))
    environmental_conditions = str(inputs.get('environmental_conditions', '25C 100% humidity'))
    communication_system = str(inputs.get('communication_system', '2.4ghz radio'))
    camera_system = str(inputs.get('camera_system', 'lidar'))
    target_distance = float(inputs.get('target_distance', 100))
    rooftop_height = float(inputs.get('rooftop_height', 10))
    precision_requirement = float(inputs.get('precision_requirement', -4))
    # -----------------------------------------------
    
    # --- CALCULATION SECTION ---
    # Calculate the total weight the drone needs to carry
    total_weight = drone_weight + payload_weight
    
    # Calculate the thrust required to lift the drone
    thrust_per_motor = 1000  # in grams, from motor_specifications
    num_motors = 4  # Assuming a quadcopter
    total_thrust = thrust_per_motor * num_motors  # in grams
    
    # Check if the drone can lift the total weight
    can_lift = total_thrust >= total_weight * 1000  # Convert kg to grams
    
    # Calculate the battery usage for the flight
    # Assuming a simple model where battery usage is proportional to weight and distance
    battery_usage = (total_weight * target_distance) / battery_capacity
    
    # Calculate the effect of wind on precision
    wind_effect = max_wind_speed / 10  # Arbitrary scaling factor for wind effect
    
    # Calculate the drop precision
    actual_drop_precision = drop_accuracy - wind_effect
    
    # Check if the precision requirement is met
    meets_precision_requirement = actual_drop_precision <= precision_requirement
    
    # Determine if the mission is feasible
    mission_feasible = can_lift and battery_usage < 1 and meets_precision_requirement
    
    # Print the result
    print(f"Calculated Result: {mission_feasible}")
    return True

if __name__ == "__main__":
    solve()