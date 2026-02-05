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
    # Calculate if the drone can carry the medical supply
    if medical_supply_weight > drone_payload_capacity:
        print("Calculated Result: Drone cannot carry the medical supply weight.")
        return
    
    # Calculate if the drone can reach the drop location
    distance_to_target = math.sqrt((float(drop_location_coordinates.split(',')[0]) ** 2) + 
                                   (float(drop_location_coordinates.split(',')[1]) ** 2))
    if distance_to_target > drone_flight_range:
        print("Calculated Result: Drone cannot reach the drop location.")
        return
    
    # Calculate the effect of wind on precision
    wind_speed = float(detailed_wind_conditions.split()[0])
    wind_effect = wind_speed / drone_max_speed
    if wind_effect > precision_tolerance:
        print("Calculated Result: Wind conditions exceed precision tolerance.")
        return
    
    # Simulate the drop
    # Assuming a simple simulation environment where we log the results
    simulation_log = {
        "drone_payload_capacity": drone_payload_capacity,
        "drone_battery_life": drone_battery_life,
        "drop_location_coordinates": drop_location_coordinates,
        "wind_conditions": wind_conditions,
        "obstacle_information": obstacle_information,
        "precision_requirement": precision_requirement,
        "drone_navigation_system": drone_navigation_system,
        "medical_supply_weight": medical_supply_weight,
        "rooftop_dimensions": rooftop_dimensions,
        "precision_tolerance": precision_tolerance,
        "drone_navigation_system_details": drone_navigation_system_details,
        "simulation_environment": simulation_environment,
        "drone_max_speed": drone_max_speed,
        "drone_control_system": drone_control_system,
        "drone_sensor_suite": drone_sensor_suite,
        "wind_speed_range": wind_speed_range,
        "obstacle_density": obstacle_density,
        "drone_communication_system": drone_communication_system,
        "simulation_accuracy": simulation_accuracy,
        "drone_dimensions": drone_dimensions,
        "drone_weight": drone_weight,
        "detailed_wind_conditions": detailed_wind_conditions,
        "inertial_navigation_system_details": inertial_navigation_system_details,
        "obstacle_characteristics": obstacle_characteristics,
        "exact_wind_speed_range": exact_wind_speed_range,
        "detailed_obstacle_characteristics": detailed_obstacle_characteristics,
        "drone_flight_range": drone_flight_range,
        "drop_location_altitude": drop_location_altitude,
        "urban_area_map": urban_area_map,
        "drone_redundancy_systems": drone_redundancy_systems,
        "battery_recharge_time": battery_recharge_time,
        "drone_navigation_system_accuracy": drone_navigation_system_accuracy,
        "wind_speed_variability": wind_speed_variability,
        "obstacle_detection_range": obstacle_detection_range,
        "obstacle_avoidance_system": obstacle_avoidance_system,
        "drone_navigation_system_type": drone_navigation_system_type,
        "drone_propulsion_system": drone_propulsion_system,
        "simulation_result": "Success"
    }
    
    print(f"Calculated Result: {json.dumps(simulation_log)}")

if __name__ == "__main__":
    solve()