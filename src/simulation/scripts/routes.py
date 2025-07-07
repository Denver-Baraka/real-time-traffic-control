import os
import sys
import pandas as pd
import random

# SUMO_HOME environment variable must be set for traci to work, but sumolib.net.readNet is causing issues.
# For demonstration purposes, we will simulate network loading and route generation.
# In a real scenario, a properly generated .net.xml from SUMO tools (like netconvert) would be used.

# Path to your SUMO network file (placeholder, as we are not fully parsing it here)
NET_FILE = "../sumo_config/nairobi.net.xml"
ROUTES_CSV = "../../data/routes.csv"

# TomTom API Key (Replace with your actual key)
TOMTOM_API_KEY = "YOUR_TOMTOM_API_KEY"

def get_tomtom_traffic_density(latitude, longitude, hour):
    """Simulates fetching traffic density from TomTom API for a given location and hour."""
    # Dummy traffic density based on hour for demonstration (0-100)
    if 7 <= hour <= 9 or 16 <= hour <= 18: # Peak hours
        return min(100, 70 + (hour % 10) * 5 + (latitude * longitude * 100 % 20)) # Simulate some variability
    else:
        return max(0, 30 - (hour % 10) * 2 + (latitude * longitude * 100 % 10)) # Simulate some variability

def generate_routes_and_traffic_data():
    """Generates dummy edges/routes data and populates simulated traffic density."""
    print("Simulating network loading and route generation...")

    # Instead of parsing a complex .net.xml, we'll create some dummy edges
    # This is to allow the script to run and generate the CSV and .rou.xml
    num_edges = 50 # Simulate 50 edges
    edges_data = []
    for i in range(num_edges):
        edge_id = f"edge_{i}"
        from_node = f"node_{i}"
        to_node = f"node_{(i+1) % num_edges}"
        length = random.uniform(100, 1000) # Random length
        
        # Dummy coordinates for demonstration
        mid_x = random.uniform(-1000, 1000)
        mid_y = random.uniform(-1000, 1000)
        real_world_lat = mid_y / 100000.0 + 1.28
        real_world_lon = mid_x / 100000.0 + 36.82

        # Populate hourly traffic densities (simulated for 24 hours)
        hourly_densities = {}
        for hour in range(24):
            hourly_densities[f'traffic_density_hour_{hour}'] = get_tomtom_traffic_density(real_world_lat, real_world_lon, hour)

        edges_data.append({
            'edge_id': edge_id,
            'from_node': from_node,
            'to_node': to_node,
            'length': length,
            'mid_x': mid_x,
            'mid_y': mid_y,
            'real_world_lat': real_world_lat,
            'real_world_lon': real_world_lon,
            **hourly_densities
        })

    df = pd.DataFrame(edges_data)

    # Ensure the data directory exists
    os.makedirs(os.path.dirname(ROUTES_CSV), exist_ok=True)
    df.to_csv(ROUTES_CSV, index=False)
    print(f"Routes and traffic data saved to {ROUTES_CSV}")

    # Generate a dummy routes.rou.xml for SUMO simulation
    # This will create routes using the dummy edges generated above.
    with open("../sumo_config/routes.rou.xml", "w") as f:
        f.write("<routes>\n")
        f.write("    <vType id=\"car\" accel=\"0.8\" decel=\"4.5\" sigma=\"0.5\" length=\"5\" maxSpeed=\"70\" />\n")
        # Add some dummy vehicles for simulation
        for i in range(200): # More vehicles for better simulation
            start_edge_idx = random.randint(0, num_edges - 1)
            end_edge_idx = random.randint(0, num_edges - 1)
            # Ensure start and end edges are different for a valid route
            while start_edge_idx == end_edge_idx:
                end_edge_idx = random.randint(0, num_edges - 1)
            
            start_edge = edges_data[start_edge_idx]["edge_id"]
            end_edge = edges_data[end_edge_idx]["edge_id"]
            
            # For a simple route, just connect start and end directly. 
            # In a real SUMO setup, you'd use duarouter or osmWebWizard to generate complex routes.
            f.write(f"    <route id=\"route_{i}\" edges=\"{start_edge} {end_edge}\" />\n")
            f.write(f"    <vehicle id=\"veh_{i}\" type=\"car\" route=\"route_{i}\" depart=\"{i}\" />\n")
        f.write("</routes>")
    print("Dummy routes.rou.xml generated.")

if __name__ == "__main__":
    generate_routes_and_traffic_data()


