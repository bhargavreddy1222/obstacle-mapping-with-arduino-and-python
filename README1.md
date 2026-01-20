# Ultrasonic Obstacle Mapping System

A real-time 2D obstacle mapping and visualization system built using Arduino UNO, an ultrasonic sensor mounted on a servo motor, and Python (Pygame) for live graphical display.

This project demonstrates how basic sensors can be used to scan an environment and generate a radar-like obstacle map using serial communication and coordinate transformation.

---

## 🔧 Hardware Components

- Arduino UNO  
- Ultrasonic Sensor (HC-SR04 or similar)  
- Servo Motor (SG90 or equivalent)  
- Jumper Wires  
- USB Cable  

---

## 💻 Software Stack

### Embedded Side
- Arduino IDE
- Servo.h library
- Ultrasonic ranging using pulse timing

### PC Side
- Python 3.x
- Pygame
- PySerial

---

## ⚙️ Working Principle

1. The servo motor rotates the ultrasonic sensor from 0° to 180°
2. At each angle, the ultrasonic sensor measures the distance to nearby objects
3. The Arduino sends angle-distance pairs to the PC via serial communication
4. Python receives the data and converts polar coordinates to Cartesian coordinates
5. Pygame renders the obstacle points in a radar-like 2D interface in real time

---

## 📐 Coordinate Mapping

The conversion from polar to Cartesian coordinates is done as:

x = r × cos(θ)  
y = r × sin(θ)

Where:
- r is the measured distance
- θ is the servo angle

---

## 🖥️ Visualization

The Python Pygame interface displays:
- A radar-style scanning view  
- Detected obstacles as points  
- Optional sweep line for realism  




## 🚀 Possible Improvements

- Replace ultrasonic sensor with ToF or LiDAR
- Add noise filtering (median / Kalman filter)
- Implement object clustering
- Migrate to ROS2 for robotic applications
- Use stepper motor for better angular precision


