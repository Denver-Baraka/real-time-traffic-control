# Hardware Setup for Physical Prototype

This directory contains instructions and diagrams for setting up the physical prototype of the Real Time Traffic Signal Control System Using AI.

## Components Needed:
-   Raspberry Pi 3B+ (or newer)
-   Pi Camera Module (or compatible USB camera/smartphone camera interfaced as IP camera)
-   MicroSD Card (32GB recommended)
-   LED Arrays (to simulate traffic lights)
-   Jumper Wires
-   Breadboard (optional, for prototyping LED connections)
-   Power Supply for Raspberry Pi
-   Dummy Vehicles (for testing object detection)

## Setup Instructions:

1.  **Raspberry Pi OS Installation:**
    -   Download Raspberry Pi OS Lite (or Desktop version if you prefer a GUI) from the official Raspberry Pi website.
    -   Use Raspberry Pi Imager to flash the OS onto your MicroSD card.
    -   Enable SSH for headless access (recommended).

2.  **Wiring LED Arrays:**
    -   Connect the LED arrays to the GPIO pins of your Raspberry Pi. Refer to the `led_wiring_diagram.png` (placeholder) for specific pin assignments.
    -   Ensure proper resistors are used with LEDs to prevent damage.

3.  **Camera Module Setup:**
    -   **For Pi Camera Module:** Connect the camera module to the CSI port on your Raspberry Pi.
    -   **For USB Camera:** Connect the USB camera to any USB port on your Raspberry Pi.
    -   **For Smartphone Camera (IP Camera):**
        -   Install an IP Camera app on your smartphone.
        -   Connect both your Raspberry Pi and smartphone to the same local network (Wi-Fi).
        -   Note down the IP address and port provided by the IP Camera app. This will be used in the `main_detection_script.py` to access the video feed.

4.  **Software Installation on Raspberry Pi:**
    -   After booting up your Raspberry Pi, ensure it has internet access.
    -   Install necessary Python libraries:
        ```bash
        sudo apt update
        sudo apt install python3-pip
        pip3 install opencv-python numpy tensorflow-lite-runtime # Adjust based on your TensorFlow Lite installation
        # You might need to install specific versions of tensorflow-lite-runtime for your Pi
        ```
    -   Clone this repository to your Raspberry Pi or transfer the `raspberry_pi_code` directory.

## Diagrams (Placeholders):
-   `led_wiring_diagram.png`: Diagram showing how to wire the LEDs to the Raspberry Pi GPIO pins.
-   `prototype_assembly.png`: Overall assembly diagram of the physical prototype.

*(Note: Actual diagrams will be added here.)*

