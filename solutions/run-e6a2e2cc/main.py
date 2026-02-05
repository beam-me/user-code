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
    # Use the variables defined above (e.g. drone_weight)
    
    # Calculate the total weight the drone needs to carry
    total_weight = drone_weight + payload_weight
    
    # Calculate the thrust-to-weight ratio
    motor_thrust = float(motor_specifications.split(' ')[0].replace('g', ''))
    thrust_to_weight_ratio = motor_thrust / total_weight
    
    # Calculate the energy required for the mission
    # Assume energy consumption is proportional to weight and distance
    energy_required = total_weight * target_distance * 0.1  # Arbitrary factor for energy consumption
    
    # Check if the battery capacity is sufficient
    battery_sufficient = battery_capacity >= energy_required
    
    # Calculate the drop precision based on wind speed and drop accuracy
    wind_factor = max_wind_speed / 10  # Arbitrary factor for wind impact
    drop_precision = drop_accuracy - wind_factor
    
    # Check if the drop precision meets the requirement
    precision_met = drop_precision >= precision_requirement
    
    # Simulate the environment and log results
    simulation_success = battery_sufficient and precision_met
    
    # Print the final result
    print(f"Calculated Result: {simulation_success}")
    return True

if __name__ == "__main__":
    solve()