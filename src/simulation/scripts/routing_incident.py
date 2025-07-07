import os
import sys
import traci
import traci.constants as tc
import random

# SUMO_HOME environment variable must be set
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

# Path to your SUMO configuration file
SUMOCFG = "../sumo_config/AI.sumocfg" # Using the AI config for dynamic routing

def get_route_cost(route_id):
    """Calculates a cost for a given route based on current traffic conditions."""
    # This is a simplified cost function. In a real scenario, this would involve
    # predicting travel time, considering vehicle density, historical data, etc.
    # For now, we'll use the number of vehicles on the route's edges as a proxy.
    edges = traci.route.getEdges(route_id)
    total_vehicles = 0
    for edge_id in edges:
        total_vehicles += traci.edge.getLastStepVehicleNumber(edge_id)
    return total_vehicles

def reroute_vehicle(veh_id):
    """Reroutes a vehicle based on current traffic conditions."""
    current_route_id = traci.vehicle.getRouteID(veh_id)
    current_edge = traci.vehicle.getRoadID(veh_id)

    # Get all available routes for the vehicle's destination
    # This is a simplification; in a real scenario, you'd need to know the destination
    # and find alternative routes to it.
    # For demonstration, let's just pick a random alternative route if available.
    all_routes = traci.route.getIDList()
    alternative_routes = [r for r in all_routes if r != current_route_id]

    if alternative_routes:
        # Simple AI logic: choose the route with the lowest cost
        best_alternative_route = None
        min_cost = float('inf')

        for alt_route_id in alternative_routes:
            cost = get_route_cost(alt_route_id)
            if cost < min_cost:
                min_cost = cost
                best_alternative_route = alt_route_id
        
        if best_alternative_route:
            traci.vehicle.setRouteID(veh_id, best_alternative_route)
            print(f"Vehicle {veh_id} rerouted from {current_route_id} to {best_alternative_route}")

def add_incident(edge_id, duration=60):
    """Simulates an incident by closing a lane or reducing its speed."""
    try:
        # Reduce speed of the lane to simulate congestion/closure
        traci.lane.setMaxSpeed(f"{edge_id}_0", 1.0) # Assuming lane 0 exists
        print(f"Incident reported on edge {edge_id}. Lane speed reduced.")
        # In a real system, you'd also log this incident and potentially trigger alerts
    except traci.exceptions.TraCIException as e:
        print(f"Could not add incident on edge {edge_id}: {e}")

def run_simulation():
    """Runs the SUMO simulation with dynamic routing and incident reporting."""
    sumo_cmd = ["sumo", "-c", SUMOCFG, "--no-warnings", "--step-length", "1.0"]
    traci.start(sumo_cmd)

    step = 0
    vehicles_to_reroute = []
    incident_edges = []

    print("Starting simulation with dynamic routing and incident reporting...")

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()

        # Dynamic Routing Logic
        for veh_id in traci.simulation.getDepartedIDList():
            # For newly departed vehicles, decide if they need initial routing
            # Or, periodically check vehicles for rerouting opportunities
            if random.random() < 0.1: # 10% chance to consider rerouting
                vehicles_to_reroute.append(veh_id)
        
        for veh_id in list(vehicles_to_reroute): # Iterate over a copy to allow modification
            if veh_id in traci.vehicle.getIDList(): # Check if vehicle still exists
                reroute_vehicle(veh_id)
            vehicles_to_reroute.remove(veh_id)

        # Incident Reporting Logic (e.g., every 200 steps, add a random incident)
        if step > 0 and step % 200 == 0:
            all_edges = traci.edge.getIDList()
            if all_edges:
                incident_edge = random.choice(all_edges)
                if incident_edge not in incident_edges:
                    add_incident(incident_edge)
                    incident_edges.append(incident_edge)

        step += 1

    traci.close()
    sys.stdout.flush()
    print("Simulation with dynamic routing and incident reporting finished.")

if __name__ == "__main__":
    run_simulation()


