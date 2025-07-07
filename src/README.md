# Source Code Directory

This directory contains all the source code for the Real Time Traffic Signal Control System Using AI project.

## Directory Structure

### simulation/
Contains SUMO simulation environment and AI algorithms:
- `sumo_config/` - SUMO configuration files (network, routes, detectors)
- `scripts/` - Python scripts for traffic control and routing
- `data_analysis/` - Data analysis and visualization scripts

### physical_prototype/
Contains Raspberry Pi implementation:
- `raspberry_pi_code/` - Main detection scripts and YOLO model
- `hardware_setup/` - Hardware configuration documentation

### common/
Shared components:
- `communication/` - MQTT communication protocols

### images/
Generated diagrams and visualizations for documentation.

## Key Files

- `simulation/scripts/dynamic_tls.py` - Main AI-driven traffic light control
- `simulation/scripts/routes.py` - Route generation and traffic data
- `simulation/scripts/routing_incident.py` - Dynamic routing and incident handling
- `physical_prototype/raspberry_pi_code/main_detection_script.py` - Main Raspberry Pi script
- `physical_prototype/raspberry_pi_code/yolo_model.py` - YOLO vehicle detection
- `physical_prototype/raspberry_pi_code/led_control.py` - LED traffic light control
- `common/communication/mqtt_client.py` - MQTT communication client

## Usage

Refer to the main project README and SETUP.md in the docs/ directory for detailed instructions on running the simulation and physical prototype.

