import math
import numpy as np
import os
import json

def get_inputs():
    defaults = {"drone_payload_capacity": "5", "drone_battery_life": "30", "drop_location_coordinates": "0,0", "wind_conditions": "variable", "obstacle_information": "particularly unknown", "precision_requirement": "3", "drone_navigation_system": "inertial value", "medical_supply_weight": "1", "rooftop_dimensions": "10x10", "precision_tolerance": "0.5", "drone_navigation_system_details": "basic stuffs", "simulation_environment": "Gazebo", "drone_max_speed": "10", "drone_control_system": "PID", "drone_sensor_suite": "Lidar", "wind_speed_range": "0 m/s", "obstacle_density": ".1", "drone_communication_system": "RF", "simulation_accuracy": ".01", "drone_dimensions": "1.x1x.08", "drone_weight": "2", "detailed_wind_conditions": "10 m/s", "inertial_navigation_system_details": "basic IMU", "obstacle_characteristics": "nothing", "exact_wind_speed_range": "10 m/s", "detailed_obstacle_characteristics": "Trees", "drone_flight_range": "10", "drop_location_altitude": "50", "urban_area_map": "None", "drone_redundancy_systems": "None", "battery_recharge_time": "60", "drone_navigation_system_accuracy": ".1", "wind_speed_variability": "5", "obstacle_detection_range": "20", "obstacle_avoidance_system": "Basic", "drone_navigation_system_type": "Inertial", "drone_propulsion_system": "Quadcopter"}
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
    drone_payload_capacity = float(inputs.get('drone_payload_capacity', 5))
    drone_battery_life = float(inputs.get('drone_battery_life', 30))
    drop_location_coordinates = str(inputs.get('drop_location_coordinates', '0,0'))
    wind_conditions = str(inputs.get('wind_conditions', 'variable'))
    obstacle_information = str(inputs.get('obstacle_information', 'particularly unknown'))
    precision_requirement = float(inputs.get('precision_requirement', 3))
    drone_navigation_system = str(inputs.get('drone_navigation_system', 'inertial value'))
    medical_supply_weight = float(inputs.get('medical_supply_weight', 1))
    rooftop_dimensions = str(inputs.get('rooftop_dimensions', '10x10'))
    precision_tolerance = float(inputs.get('precision_tolerance', 0.5))
    drone_navigation_system_details = str(inputs.get('drone_navigation_system_details', 'basic stuffs'))
    simulation_environment = str(inputs.get('simulation_environment', 'Gazebo'))
    drone_max_speed = float(inputs.get('drone_max_speed', 10))
    drone_control_system = str(inputs.get('drone_control_system', 'PID'))
    drone_sensor_suite = str(inputs.get('drone_sensor_suite', 'Lidar'))
    wind_speed_range = str(inputs.get('wind_speed_range', '0 m/s'))
    obstacle_density = float(inputs.get('obstacle_density', .1))
    drone_communication_system = str(inputs.get('drone_communication_system', 'RF'))
    simulation_accuracy = float(inputs.get('simulation_accuracy', .01))
    drone_dimensions = str(inputs.get('drone_dimensions', '1.x1x.08'))
    drone_weight = float(inputs.get('drone_weight', 2))
    detailed_wind_conditions = str(inputs.get('detailed_wind_conditions', '10 m/s'))
    inertial_navigation_system_details = str(inputs.get('inertial_navigation_system_details', 'basic IMU'))
    obstacle_characteristics = str(inputs.get('obstacle_characteristics', 'nothing'))
    exact_wind_speed_range = str(inputs.get('exact_wind_speed_range', '10 m/s'))
    detailed_obstacle_characteristics = str(inputs.get('detailed_obstacle_characteristics', 'Trees'))
    drone_flight_range = float(inputs.get('drone_flight_range', 10))
    drop_location_altitude = float(inputs.get('drop_location_altitude', 50))
    urban_area_map = str(inputs.get('urban_area_map', 'None'))
    drone_redundancy_systems = str(inputs.get('drone_redundancy_systems', 'None'))
    battery_recharge_time = float(inputs.get('battery_recharge_time', 60))
    drone_navigation_system_accuracy = float(inputs.get('drone_navigation_system_accuracy', .1))
    wind_speed_variability = float(inputs.get('wind_speed_variability', 5))
    obstacle_detection_range = float(inputs.get('obstacle_detection_range', 20))
    obstacle_avoidance_system = str(inputs.get('obstacle_avoidance_system', 'Basic'))
    drone_navigation_system_type = str(inputs.get('drone_navigation_system_type', 'Inertial'))
    drone_propulsion_system = str(inputs.get('drone_propulsion_system', 'Quadcopter'))
    # -----------------------------------------------
    
    # --- CALCULATION SECTION ---
    # Use the variables defined above (e.g. drone_payload_capacity)
    
    # Calculate if the drone can carry the medical supply
    can_carry_supply = medical_supply_weight <= drone_payload_capacity
    
    # Calculate if the drone has enough battery life to reach the drop location and return
    distance_to_drop = np.linalg.norm(np.array([float(coord) for coord in drop_location_coordinates.split(',')]))
    total_flight_time = (distance_to_drop / drone_max_speed) * 2  # to drop and return
    has_enough_battery = total_flight_time <= drone_battery_life
    
    # Check if the drone can operate within the wind conditions
    max_wind_speed = float(detailed_wind_conditions.split()[0])
    can_operate_in_wind = max_wind_speed <= wind_speed_variability
    
    # Check if the precision requirement can be met
    can_meet_precision = precision_tolerance <= precision_requirement
    
    # Final decision
    is_mission_feasible = all([can_carry_supply, has_enough_battery, can_operate_in_wind, can_meet_precision])
    
    print(f"Calculated Result: {is_mission_feasible}")
    return True

if __name__ == "__main__":
    solve()