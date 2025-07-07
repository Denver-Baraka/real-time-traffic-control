import os
import sys
import traci
import traci.constants as tc
import pandas as pd
import numpy as np

# SUMO_HOME environment variable must be set
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

# Path to your SUMO configuration file
SUMOCFG = "../sumo_config/AI.sumocfg"

# Output file for simulation results
RESULTS_CSV = "../../data/simulation_results.csv"

# Define a simple cost metric for traffic lights
def calculate_cost(lane_id):
    waiting_time = traci.lane.getWaitingTime(lane_id)
    # You can add more factors here, e.g., vehicle count, queue length, emergency vehicles
    return waiting_time

def get_lane_occupancy(lane_id):
    """Returns the occupancy of a given lane (number of vehicles)."""
    return traci.lane.getLastStepVehicleNumber(lane_id)

def get_lane_queue_length(lane_id):
    """Returns the queue length of a given lane.""" 
    return traci.lane.getLastStepHaltingNumber(lane_id)

def get_total_waiting_time(lane_id):
    """Returns the total waiting time of vehicles on a given lane."""
    return traci.lane.getWaitingTime(lane_id)

def get_priority_score(lane_id):
    """Calculates a priority score for a lane based on multiple factors."""
    occupancy = get_lane_occupancy(lane_id)
    queue_length = get_lane_queue_length(lane_id)
    waiting_time = get_total_waiting_time(lane_id)

    # A simple heuristic: prioritize lanes with more waiting vehicles and longer queues
    # Weights can be tuned based on desired traffic flow characteristics
    score = (waiting_time * 0.6) + (queue_length * 0.3) + (occupancy * 0.1)
    return score

def run_simulation():
    """Runs the SUMO simulation with AI-driven traffic light control."""
    # Start SUMO as a subprocess
    sumo_cmd = ["sumo", "-c", SUMOCFG, "--no-warnings", "--step-length", "1.0"]
    # If you want to run with GUI, change "sumo" to "sumo-gui"
    # sumo_cmd = ["sumo-gui", "-c", SUMOCFG, "--no-warnings", "--step-length", "1.0"]

    traci.start(sumo_cmd)

    step = 0
    traffic_lights = traci.trafficlight.getIDList()
    results = []

    print("Starting simulation...")

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()

        for tls_id in traffic_lights:
            controlled_lanes = traci.trafficlight.getControlledLanes(tls_id)
            if not controlled_lanes:
                continue

            # Get the current traffic light program and phases
            logic = traci.trafficlight.getCompleteRedYellowGreenDefinition(tls_id)
            if not logic:
                continue
            current_program = logic[0] # Assuming only one program

            best_phase_index = -1
            max_priority_score = -1

            # Iterate through all possible phases to find the best one
            for i, phase in enumerate(current_program.phases):
                # Calculate a cumulative priority score for this phase
                # A phase might allow movement for multiple lanes/approaches
                phase_score = 0
                for lane in controlled_lanes:
                    # Check if this lane is green in the current phase
                    # This requires mapping the lane to its corresponding signal in the phase state string
                    # For simplicity, we'll assume a direct check for 'g' or 'G' in the phase state
                    # A more robust solution would involve parsing the phase.state string and
                    # checking the specific signal for the lane's link.
                    if 'g' in phase.state or 'G' in phase.state: # Very generic check
                        phase_score += get_priority_score(lane)
                
                if phase_score > max_priority_score:
                    max_priority_score = phase_score
                    best_phase_index = i
            
            # Apply the best phase if it's different from the current one
            current_phase = traci.trafficlight.getPhase(tls_id)
            if best_phase_index != -1 and current_phase != best_phase_index:
                traci.trafficlight.setPhase(tls_id, best_phase_index)
                # Set a dynamic duration based on the priority score or other factors
                # For now, a fixed minimum green time to avoid rapid switching
                traci.trafficlight.setPhaseDuration(tls_id, 5) # 5 seconds minimum green

        # Collect data for analysis
        avg_waiting_time = traci.simulation.getWaitingTime()
        avg_speed = traci.simulation.getMeanSpeed()
        vehicle_count = traci.vehicle.getIDCount()

        results.append({
            'step': step,
            'avg_waiting_time': avg_waiting_time,
            'avg_speed': avg_speed,
            'vehicle_count': vehicle_count
        })

        step += 1

    traci.close()
    sys.stdout.flush()

    df_results = pd.DataFrame(results)
    os.makedirs(os.path.dirname(RESULTS_CSV), exist_ok=True)
    df_results.to_csv(RESULTS_CSV, index=False)
    print(f"Simulation results saved to {RESULTS_CSV}")

if __name__ == "__main__":
    run_simulation()


