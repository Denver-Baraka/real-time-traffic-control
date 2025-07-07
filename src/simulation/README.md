# SUMO Simulation Environment

This directory contains the SUMO (Simulation of Urban Mobility) implementation of the AI-driven traffic control system.

## Directory Contents

### sumo_config/
- `nairobi.net.xml` - SUMO network file defining roads and intersections
- `routes.rou.xml` - Vehicle routes and traffic demand (generated)
- `detectors.add.xml` - Traffic detectors configuration
- `AI.sumocfg` - Main SUMO configuration file
- `main.sumocfg` - Alternative configuration file

### scripts/
- `dynamic_tls.py` - **Main script** for AI-driven traffic light control
- `routes.py` - Generates routes and traffic data from network
- `routing_incident.py` - Implements dynamic routing and incident reporting

### data_analysis/
- `analyze_results.py` - Analyzes simulation results and generates visualizations

## Quick Start

1. Ensure SUMO is installed and SUMO_HOME is set
2. Generate routes: `python scripts/routes.py`
3. Run AI simulation: `python scripts/dynamic_tls.py`
4. Analyze results: `python data_analysis/analyze_results.py`

## Key Features

- **Adaptive Traffic Signals**: AI algorithms adjust signal timing based on real-time traffic
- **Dynamic Routing**: Vehicles are rerouted based on current traffic conditions
- **Incident Detection**: System detects and responds to traffic incidents
- **Performance Metrics**: Comprehensive data collection for analysis

## Configuration

The system uses a 5-layer architecture:
1. **Sensor Layer**: Traffic detectors and cameras
2. **Data Layer**: Data collection and preprocessing
3. **AI Layer**: Traffic prediction and optimization
4. **Control Layer**: Signal control implementation
5. **Management Layer**: Monitoring and coordination

## Output

Simulation results are saved to `../../data/simulation_results.csv` and include:
- Average waiting time per simulation step
- Average vehicle speed
- Vehicle count
- Traffic flow metrics

