# Data Directory

This directory contains generated data files from simulations and analysis.

## Generated Files

### simulation_results.csv
Contains simulation output data with the following columns:
- `step` - Simulation time step
- `avg_waiting_time` - Average waiting time of vehicles (seconds)
- `avg_speed` - Average speed of vehicles (m/s)
- `vehicle_count` - Number of vehicles in the simulation

### routes.csv
Contains route and traffic density data:
- `edge_id` - Unique identifier for road segments
- `from_node` / `to_node` - Start and end nodes of the edge
- `length` - Length of the road segment (meters)
- `real_world_lat` / `real_world_lon` - GPS coordinates
- `traffic_density_hour_X` - Traffic density for each hour (0-23)

## Data Analysis

The data can be analyzed using the scripts in `src/simulation/data_analysis/`:
- Run `analyze_results.py` to generate visualizations
- Plots are saved to `src/simulation/data_analysis/plots/`

## Data Format

All CSV files use standard comma-separated format with headers. Data is generated automatically when running the simulation scripts.

## Usage in Research

This data can be used for:
- Performance comparison between AI and traditional traffic control
- Traffic pattern analysis
- Algorithm optimization
- Academic research and publications

## Data Privacy

All data is simulated and does not contain any real personal or vehicle information. The GPS coordinates are fictional and based on a simplified model of Nairobi city.

