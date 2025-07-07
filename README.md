
# Real Time Traffic Signal Control System Using AI

## Overview
This project implements an AI-driven real-time traffic control system designed to optimize urban traffic flow, reduce congestion, and minimize environmental impact. By leveraging artificial intelligence, real-time data, and advanced simulation techniques, this system dynamically adjusts traffic light timings and provides intelligent routing assistance to vehicles. The project includes both a comprehensive SUMO (Simulation of Urban MObility) simulation environment and a physical prototype built with Raspberry Pi and YOLO (You Only Look Once) for vehicle detection.

## Features
-   **AI-Powered Traffic Signal Optimization:** Dynamic adjustment of traffic light timings based on real-time traffic density and flow, utilizing machine learning algorithms.
-   **SUMO Simulation Environment:** A detailed simulation of a city network (based on Nairobi) with over 20 routes and interconnected intersections to test and validate AI algorithms under various traffic scenarios.
-   **Intelligent Vehicle Routing:** AI-assisted routing mechanisms that provide optimal path recommendations to drivers, minimizing travel time and avoiding congested areas.
-   **Physical Prototype:** A small-scale physical intersection model using Raspberry Pi 3B+, camera modules, and LED arrays to demonstrate real-time vehicle detection (YOLOv5s) and adaptive signal control at the edge.
-   **Communication Protocols:** Implementation of communication protocols (e.g., MQTT) for seamless data exchange and coordination between different components and intersections.
-   **Data Analysis and Visualization:** Tools and scripts for analyzing simulation results, traffic patterns, and system performance metrics.
-   **Incident Detection:** Automated reporting of simulated traffic incidents within the SUMO environment.

## Project Structure
```
real-time-traffic-signal-ai/
├── .github/
│   └── workflows/
│       └── main.yml  # CI/CD pipeline (optional, for future)
├── docs/
│   ├── ARCHITECTURE.md
│   ├── project_summary.md
│   └── ... (other documentation files)
├── src/
│   ├── simulation/
│   │   ├── sumo_config/
│   │   │   ├── nairobi.net.xml
│   │   │   ├── detectors.add.xml
│   │   │   ├── AI.sumocfg
│   │   │   └── main.sumocfg
│   │   ├── scripts/
│   │   │   ├── routes.py
│   │   │   └── dynamic_tls.py
│   │   └── data_analysis/
│   │       └── ... (scripts for data analysis and visualization)
│   ├── physical_prototype/
│   │   ├── raspberry_pi_code/
│   │   │   └── ... (Python scripts for YOLO, LED control)
│   │   └── hardware_setup/
│   │       └── ... (diagrams, instructions for physical setup)
│   └── common/
│       └── communication/
│           └── ... (MQTT or other communication protocol implementations)
├── .gitignore
├── LICENSE
├── README.md
├── CONTRIBUTING.md
├── requirements.txt
└── ... (any other top-level files)
```

## Getting Started

### Prerequisites
To run the simulations and potentially set up the physical prototype, you will need the following:

-   **SUMO (Simulation of Urban MObility):** Version 1.15.0 or later. Download from [SUMO Website](https://www.eclipse.org/sumo/downloads/).
-   **Python 3.x:** Recommended version 3.8 or higher.
-   **Python Libraries:** Install dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```
-   **Raspberry Pi (for physical prototype):** Raspberry Pi 3B+ or newer, Pi Camera Module, LED arrays, and a MicroSD card (32GB recommended).

### Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/real-time-traffic-signal-ai.git
    cd real-time-traffic-signal-ai
    ```
    *(Note: The original project repository is currently private. This is a placeholder for your public repository.)*

2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **SUMO Configuration:**
    -   Ensure SUMO is installed and accessible from your command line.
    -   The SUMO network and configuration files are located in `src/simulation/sumo_config/`.

4.  **Physical Prototype Setup (Optional):**
    -   Refer to `src/physical_prototype/hardware_setup/` for detailed instructions on setting up the Raspberry Pi, camera, and LED arrays.
    -   Flash Raspberry Pi OS Lite to your MicroSD card.
    -   Install necessary libraries on the Raspberry Pi: OpenCV, TensorFlow Lite, YOLOv5 nano (refer to `src/physical_prototype/raspberry_pi_code/` for specific instructions).

## Usage

### Running SUMO Simulations

1.  **Generate Routes (if needed):**
    Navigate to `src/simulation/scripts/` and run `routes.py` to generate traffic routes based on the `nairobi.net.xml` file. This script also simulates real-world traffic density data acquisition.
    ```bash
    python routes.py
    ```

2.  **Run Dynamic Traffic Light Simulation:**
    Execute `dynamic_tls.py` from `src/simulation/scripts/` to run the AI-driven adaptive traffic signal simulation. This script interacts with SUMO via TraCI.
    ```bash
    python dynamic_tls.py
    ```
    The simulation will run in the command line interface (CLI) for fair comparison and performance, without a graphical user interface (GUI) by default.

### Physical Prototype Operation

1.  **Deploy Code to Raspberry Pi:**
    Transfer the Python scripts from `src/physical_prototype/raspberry_pi_code/` to your Raspberry Pi.

2.  **Start Vehicle Detection and Signal Control:**
    Run the main detection script on your Raspberry Pi. This script will continuously capture frames from the camera, perform YOLOv5s object detection, classify vehicles, and control the LED traffic lights based on the AI's decisions.
    ```bash
    # Example command on Raspberry Pi
    python main_detection_script.py # Replace with actual script name
    ```
    *(Note: Due to hardware limitations of Raspberry Pi 3B+, there might be a processing delay. Consider upgrading to more powerful hardware like NVIDIA Jetson Nano for better real-time performance.)*

## Contributing
We welcome contributions to this project! Please see `CONTRIBUTING.md` for guidelines on how to submit issues, feature requests, and pull requests.

## License
This project is licensed under the [License Name] - see the `LICENSE` file for details.

## Acknowledgements
-   University of Nairobi, Faculty of Engineering, Department of Electrical and Information Engineering.
-   Supervisor: Dr. Gevira Omondi.
-   Examiners: Prof H A Ouma, Mr K Wachira.
-   The SUMO (Simulation of Urban MObility) team for providing a powerful simulation platform.
-   Ultralytics for the YOLOv5s model.

## Contact
For any inquiries, please contact [your-email@example.com] (replace with your actual email address or a project contact email).



