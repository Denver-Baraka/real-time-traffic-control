# Physical Prototype Implementation

This directory contains the Raspberry Pi implementation of the traffic signal control system using computer vision and hardware control.

## Directory Contents

### raspberry_pi_code/
- `main_detection_script.py` - **Main script** for vehicle detection and traffic control
- `yolo_model.py` - YOLOv5 vehicle detection and classification
- `led_control.py` - LED traffic light control via GPIO

### hardware_setup/
- `README.md` - Hardware setup instructions and wiring diagrams

## Hardware Requirements

- **Raspberry Pi 3B+** or higher
- **Camera Module** compatible with Raspberry Pi
- **LED Arrays** for traffic light simulation (Red, Yellow, Green)
- **Breadboard and Jumper Wires**
- **MicroSD Card** (32GB recommended)
- **Power Supply** for Raspberry Pi and LEDs

## Software Requirements

- Raspberry Pi OS
- Python 3.8+
- OpenCV for Python
- GPIO libraries
- Camera interface enabled

## Key Features

### Vehicle Detection
- **YOLOv5 Model**: Optimized for Raspberry Pi using TensorFlow Lite
- **Vehicle Classification**: Cars, buses, trucks, ambulances, fire trucks
- **Real-time Processing**: 5-10 FPS on Raspberry Pi 3B+
- **Accuracy**: 92% on test dataset

### Traffic Control
- **GPIO Control**: Direct control of LED arrays via Raspberry Pi GPIO pins
- **Signal Timing**: AI-driven adaptive signal timing
- **Emergency Priority**: Special handling for emergency vehicles

### Communication
- **MQTT Protocol**: Wireless communication between intersections
- **Data Sharing**: Real-time traffic density and signal status
- **Coordination**: Multi-intersection traffic optimization

## Quick Start

1. Set up Raspberry Pi with camera and LEDs
2. Install dependencies: `pip install -r requirements.txt`
3. Enable camera interface: `sudo raspi-config`
4. Run main script: `python main_detection_script.py`

## GPIO Pin Configuration

Default pin assignments (can be modified in `led_control.py`):
- North Green: GPIO 17
- North Yellow: GPIO 27
- North Red: GPIO 22
- East Green: GPIO 23
- East Yellow: GPIO 24
- East Red: GPIO 25

## Performance Optimization

- Use TensorFlow Lite for faster inference
- Reduce camera resolution if needed (640x480 recommended)
- Optimize GPIO operations for real-time response
- Consider using hardware PWM for LED brightness control

