Vision-Based Gesture Controlled IoT System

A real-time hand gesture control system that uses Python, OpenCV, and
MediaPipe to detect the number of fingers shown to a webcam and
wirelessly control LEDs connected to an ESP32-C6 over Wi-Fi.

How It Works

Webcam ↓ Python + OpenCV + MediaPipe ↓ Hand Gesture Detection ↓ Finger
Count (1–5) ↓ Wi-Fi ↓ ESP32-C6 ↓ LEDs

Features

-   Real-time hand gesture detection
-   Detects 1–5 fingers
-   Computer vision using MediaPipe
-   Image processing using OpenCV
-   Wireless communication using Wi-Fi
-   ESP32-C6 GPIO control
-   Multiple LED control based on detected gesture

Gesture Control

  Gesture     ESP32 Output
  ----------- -----------------------
  1 finger    LED 1
  2 fingers   LED 1 + 2
  3 fingers   LED 1 + 2 + 3
  4 fingers   LED 1 + 2 + 3 + 4
  5 fingers   LED 1 + 2 + 3 + 4 + 5

Hardware

-   ESP32-C6 Super Mini
-   5 LEDs
-   5 × 220Ω resistors
-   Breadboard
-   Jumper wires
-   Computer with webcam

GPIO Connections

  LED     ESP32-C6 GPIO
  ------- ---------------
  LED 1   GPIO 2
  LED 2   GPIO 3
  LED 3   GPIO 4
  LED 4   GPIO 5
  LED 5   GPIO 6

Each LED is connected through a 220Ω resistor to its GPIO pin, with the
other side connected to GND.

Software

-   Python
-   OpenCV
-   MediaPipe
-   Requests
-   Arduino IDE
-   ESP32-C6 Arduino Core

Installation

Install the required Python packages:

py -m pip install opencv-python mediapipe requests

Usage

1.  Upload gesture.ino to the ESP32-C6.
2.  Connect the ESP32-C6 and computer to the same Wi-Fi network.
3.  Note the ESP32 IP address from the Serial Monitor.
4.  Enter the ESP32 IP address in gesture.py.
5.  Run:

py gesture.py

6.  Show your hand to the webcam.

The number of LEDs turned on corresponds to the detected number of
fingers.
