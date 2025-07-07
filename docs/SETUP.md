# Setup Instructions

This document provides step-by-step instructions for setting up and running the Real Time Traffic Signal Control System Using AI project.

## Prerequisites

### Software Requirements
- Python 3.8 or higher
- SUMO (Simulation of Urban Mobility) 1.12.0 or higher
- Git

### Hardware Requirements (for Physical Prototype)
- Raspberry Pi 3B+ or higher
- Camera module compatible with Raspberry Pi
- LED arrays for traffic light simulation
- Breadboard and jumper wires
- MicroSD card (32GB recommended)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/username/real-time-traffic-control.git
cd real-time-traffic-control
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install SUMO
#### Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install sumo sumo-tools
```

#### Windows:
Download and install SUMO from: https://www.eclipse.org/sumo/

#### macOS:
```bash
brew install sumo
```

### 4. Set Environment Variables
```bash
export SUMO_HOME="/usr/share/sumo"  # Linux
# or
export SUMO_HOME="/path/to/sumo"    # Custom installation
```

## Running the Simulation

### 1. Generate Routes and Traffic Data
```bash
cd src/simulation/scripts/
python routes.py
```

### 2. Run the AI-Driven Traffic Control Simulation
```bash
python dynamic_tls.py
```

### 3. Analyze Results
```bash
cd ../data_analysis/
python analyze_results.py
```

## Physical Prototype Setup

### 1. Raspberry Pi Configuration
1. Flash Raspberry Pi OS to the microSD card
2. Enable camera interface: `sudo raspi-config` → Interface Options → Camera
3. Install required packages:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-opencv python3-pip
   pip3 install -r requirements.txt
   ```

### 2. Hardware Connections
- Connect camera module to CSI port
- Connect LED arrays to GPIO pins as defined in `led_control.py`
- Ensure proper power supply for all components

### 3. Run the Physical Prototype
```bash
cd src/physical_prototype/raspberry_pi_code/
python main_detection_script.py
```

## Project Structure

```
real-time-traffic-control/
├── src/
│   ├── simulation/
│   │   ├── sumo_config/          # SUMO configuration files
│   │   ├── scripts/              # Python scripts for simulation
│   │   └── data_analysis/        # Analysis and visualization
│   ├── physical_prototype/
│   │   ├── raspberry_pi_code/    # Raspberry Pi implementation
│   │   └── hardware_setup/       # Hardware documentation
│   ├── common/
│   │   └── communication/        # MQTT communication
│   └── images/                   # Generated diagrams and images
├── data/                         # Generated data files
├── presentation/                 # Project presentation slides
├── docs/                         # Additional documentation
├── README.md
├── requirements.txt
├── LICENSE
└── SETUP.md
```

## Troubleshooting

### Common Issues

1. **SUMO not found error**
   - Ensure SUMO is properly installed and SUMO_HOME is set
   - Check PATH includes SUMO binaries

2. **TraCI connection errors**
   - Verify SUMO configuration files are valid
   - Check network file format and syntax

3. **Camera module not detected (Raspberry Pi)**
   - Ensure camera is properly connected
   - Enable camera interface in raspi-config
   - Check camera permissions

4. **GPIO permission errors**
   - Run scripts with sudo or add user to gpio group
   - Ensure proper GPIO pin configuration

### Performance Optimization

1. **For better simulation performance:**
   - Reduce simulation step size
   - Limit number of vehicles
   - Use headless mode (sumo instead of sumo-gui)

2. **For Raspberry Pi optimization:**
   - Use TensorFlow Lite models
   - Reduce camera resolution if needed
   - Optimize GPIO operations

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Search existing GitHub issues
3. Create a new issue with detailed description and logs

## License

This project is licensed under the MIT License - see the LICENSE file for details.

