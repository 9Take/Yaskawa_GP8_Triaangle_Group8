
# 🤖 Yaskawa GP8 Triangle Trajectory

> Robot arm control service for tracing an equilateral triangle — built with **Python + Yaskawa SDK (HSES)**, featuring real-time kinematic simulation and joint pulse tracking.

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Yaskawa](https://img.shields.io/badge/Yaskawa-SDK-0055A5?logo=yaskawa)](https://github.com/UnderAutomation/Yaskawa.py)
[![NumPy](https://img.shields.io/badge/NumPy-2.4.3-013243?logo=numpy)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.8-11557c?logo=plotly)](https://matplotlib.org/)

---

## 🚀 Overview

This script acts as the **"Controller"** within a robotic workcell — processing trajectory calculations and returning precise Cartesian and Joint movements via the **High Speed Ethernet Server (HSES) protocol**.

The program commands a Yaskawa industrial robot (e.g., YRC1000micro) to draw a **150mm equilateral triangle** in the vertical (Y-Z) plane while strictly locking the wrist orientation to prevent unwanted twisting.

### Key Features

| Feature | Description | Purpose |
|---------|-----------|---------|
| `Cartesian Path` | Y-Z Plane Tracking | Verifies the physical trajectory of the triangle. |
| `Orientation Lock` | Rx, Ry, Rz Monitoring | Ensures wrist angles remain perfectly constant. |
| `Joint Tracking` | S, L, U, R, B, T Pulses | Analyzes individual servo motor behavior over time. |

---

## 🏗️ Architecture

The Python script communicates directly with the Yaskawa Controller over a local network.

```text
Operator PC (Python Script)
      │
      ▼  LAN (e.g., 192.168.10.XX)
┌─────────────────────────┐
│  Yaskawa Controller     │  ◄── YRC1000 / YRC1000micro
│  (HSES Protocol)        │      Port: UDP 10040 (Default)
└────────────┬────────────┘
             │  Servo Commands & Feedback
      ┌──────┴──────┐
      ▼             ▼
┌──────────┐  ┌───────────┐
│ Cartesian│  │   Joint   │  ◄── GP8 Robot Arm
│ Movement │  │  Feedback │      (S, L, U, R, B, T)
└──────────┘  └───────────┘
```

---

## 📦 Prerequisites

Ensure the following are prepared before running the script:

- **Software:**
  - [Python 3.8+](https://www.python.org/downloads/)
  - [Git](https://git-scm.com/)
- **Hardware/Network:**
  - A physical LAN connection to the Yaskawa Controller.
  - PC set to a Static IP on the same subnet (e.g., `192.168.10.100` if the robot is `192.168.10.101`).
- **Robot State:**
  - Controller must be in **Remote Mode**.
  - System must be clear of alarms and capable of turning **Servo ON**.

---

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/UnderAutomation/Yaskawa.py
git clone <your-repository-url>
cd <your-project-folder>
```
Before do next step make sure you already following the requirements of [Yaskawa](https://github.com/UnderAutomation/Yaskawa.py)

### 2. Configure Virtual Environment (Recommended)

Create and activate a Python virtual environment to keep dependencies isolated:

```bash
python -m venv .yaskava_env

# For Linux/Mac:
source .yaskava_env/bin/activate  

# For Windows:
.yaskava_env\Scripts\activate 
```

### 3. Install Dependencies

install them:
```bash
pip install -r requirements.txt
```
> *Note: The robot control library is based on [UnderAutomation/Yaskawa.py](https://github.com/UnderAutomation/Yaskawa.py).*

### 4. Launch the Script
```bash
python triangle.py
```

---

## ⚙️ Configuration

Inside the main script (`triangle.py`), you will find a configuration section at the top of the `main()` function. Adjust these variables before running based on your testing phase:

| Variable | Default | Description |
|----------|---------|-------------|
| `SIMULATION_MODE` | `True` | Set to `True` to preview plots safely. Set to `False` to move the physical robot. |
| `ROBOT_SPEED` | `10` | Cartesian movement speed (%). |
| `STEP_SIZE` | `80` | Distance (mm) between interpolated trajectory points. |
| `DELAY_BETWEEN_STEPS`| `1` | Pause duration (seconds) to allow the robot to finish a segment (prevents "Manipulator Operating" errors). |

---

## 📊 Output Graphs Explained

Upon successful execution (in either Simulation or Real Robot mode), a Matplotlib window with 3 graphs will appear:

1. **Left (Y-Z Plane):** A front-view visualization of the End-Effector tracing the equilateral triangle.
2. **Center (Orientation):** Displays the Rx (180°), Ry (-8.976°), and Rz (0°) angles as flat horizontal lines, proving the wrist orientation is locked.
3. **Right (Joint Pulses):** Shows the pulse values of the 6 motors (S, L, U, R, B, T axes) over time, allowing you to analyze how each joint contributes to the linear Cartesian movement.

---

## ⚠️ Safety Warning

**CRITICAL: Industrial robots move at high speeds and with significant force.**

- **Clear the Area:** Before changing `SIMULATION_MODE = False`, physically verify that the robot's workspace is completely clear of people, cables, and obstacles.
- **Hold the Pendant:** The Operator **MUST** hold the Teach Pendant in their hands and be ready to press the **Emergency Stop (E-Stop)** button at all times while this script is executing.
- **First Run:** Always test with `SIMULATION_MODE = True` first to verify the mathematical trajectory before sending commands to the servo motors.

---

## 👥 Team

**Group 8** — Yaskawa GP8 Triangle Trajectory
- Thanpisit Banyam (6601023611035)
- Putthakhun Horthong (6601023621022)
- Teetawat Songsaard (6601023621065)

---

## Results



*Python · Yaskawa SDK · HSES Protocol*