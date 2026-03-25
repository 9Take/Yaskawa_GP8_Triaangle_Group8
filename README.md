# Yaskawa_GP8_Triaangle_Group8
# 🤖 Yaskawa Robot - Y-Z Plane Triangle Trajectory

This project controls a **Yaskawa industrial robot arm** using Python via the High Speed Ethernet Server (HSES) protocol. It commands the End-Effector to draw an **"equilateral triangle"** trajectory in the vertical plane (Y-Z Plane) while strictly maintaining a constant wrist orientation (no wrist twisting).

It includes a built-in Simulation Mode and generates 3 distinct plots to analyze the robot's kinematic behavior:
1. **Cartesian Path (Y-Z Plane):** The physical trajectory of the triangle.
2. **End-Effector Orientation:** Verifies that the wrist angles (Rx, Ry, Rz) remain completely locked.
3. **Joint Angles:** Tracks the movement of all 6 individual servo motors (S, L, U, R, B, T axes) in Pulses.

---

## ⚙️ Prerequisites

- Python 3.8 or higher.
- A physical LAN connection between your PC and the Yaskawa Controller. (Your PC must be set to a Static IP on the same subnet, e.g., `192.168.10.XX`).
- The robot controller must be set to **Remote Mode** and capable of turning **Servo ON**.

## 📦 Installation

1. Clone and do the requirements this repository to your local machine:
    ```bash
    git clone <your-repository-url>
    cd <your-project-folder>

2. (Recommended) Create and activate a Virtual Environment:
    python -m venv .yaskava_env

    # For Linux/Mac:
    source .yaskava_env/bin/activate  

    # For Windows:
    .yaskava_env\Scripts\activate

3. Install all required dependencies using requirements.txt:
    pip install -r requirements.txt

Gemini said
Here is the README.md and the instructions for setting up your requirements.txt file in English. I've included the project details, configuration instructions, and crucial safety warnings so it is ready for your lab report or GitHub repository!

📝 1. Setting up requirements.txt
Create a new file named requirements.txt in the same directory as your Python script, and paste the following content into it:

Plaintext
# Yaskawa Robot SDK (Based on https://github.com/UnderAutomation/Yaskawa.py)
underautomation.yaskawa

# Data Science & Plotting Libraries
numpy==2.4.3
matplotlib==3.10.8
📝 2. The README.md File
You can copy and paste the Markdown below to create the README.md file for your project:

Markdown
# 🤖 Yaskawa Robot - Y-Z Plane Triangle Trajectory

This project controls a **Yaskawa industrial robot arm (YRC1000micro)** using Python via the High Speed Ethernet Server (HSES) protocol. It commands the End-Effector to draw an **"equilateral triangle"** trajectory in the vertical plane (Y-Z Plane) while strictly maintaining a constant wrist orientation (no wrist twisting).

It includes a built-in Simulation Mode and generates 3 distinct plots to analyze the robot's kinematic behavior:
1. **Cartesian Path (Y-Z Plane):** The physical trajectory of the triangle.
2. **End-Effector Orientation:** Verifies that the wrist angles (Rx, Ry, Rz) remain completely locked.
3. **Joint Angles:** Tracks the movement of all 6 individual servo motors (S, L, U, R, B, T axes) in Pulses.

---

## ⚙️ Prerequisites

- Python 3.8 or higher.
- A physical LAN connection between your PC and the Yaskawa Controller. (Your PC must be set to a Static IP on the same subnet, e.g., `192.168.10.XX`).
- The robot controller must be set to **Remote Mode** and capable of turning **Servo ON**.

## 📦 Installation

1. Clone this repository to your local machine:
   ```bash
   git clone <your-repository-url>
   cd <your-project-folder>
(Recommended) Create and activate a Virtual Environment:

Bash
python -m venv .yaskava_env

# For Linux/Mac:
source .yaskava_env/bin/activate  

# For Windows:
.yaskava_env\Scripts\activate 
Install all required dependencies using requirements.txt:

Bash
pip install -r requirements.txt
Note: The robot control library is based on UnderAutomation/Yaskawa.py.

🚀 Usage
Inside the main script (e.g., triangle.py), you will find a configuration section at the top of the main() function. You can adjust these variables before running:

SIMULATION_MODE = True    # Set to True to preview graphs without moving the real robot.
ROBOT_SPEED = 10          # The movement speed of the robot (%).
STEP_SIZE = 80            # The distance between trajectory points (helps prevent 'Manipulator Operating' errors).
DELAY_BETWEEN_STEPS = 1   # Pause duration (in seconds) to allow the robot to finish each step.

Gemini said
Here is the README.md and the instructions for setting up your requirements.txt file in English. I've included the project details, configuration instructions, and crucial safety warnings so it is ready for your lab report or GitHub repository!

📝 1. Setting up requirements.txt
Create a new file named requirements.txt in the same directory as your Python script, and paste the following content into it:

Plaintext
# Yaskawa Robot SDK (Based on https://github.com/UnderAutomation/Yaskawa.py)
underautomation.yaskawa

# Data Science & Plotting Libraries
numpy==2.4.3
matplotlib==3.10.8
📝 2. The README.md File
You can copy and paste the Markdown below to create the README.md file for your project:

Markdown
# 🤖 Yaskawa Robot - Y-Z Plane Triangle Trajectory

This project controls a **Yaskawa industrial robot arm (YRC1000micro)** using Python via the High Speed Ethernet Server (HSES) protocol. It commands the End-Effector to draw an **"equilateral triangle"** trajectory in the vertical plane (Y-Z Plane) while strictly maintaining a constant wrist orientation (no wrist twisting).

It includes a built-in Simulation Mode and generates 3 distinct plots to analyze the robot's kinematic behavior:
1. **Cartesian Path (Y-Z Plane):** The physical trajectory of the triangle.
2. **End-Effector Orientation:** Verifies that the wrist angles (Rx, Ry, Rz) remain completely locked.
3. **Joint Angles:** Tracks the movement of all 6 individual servo motors (S, L, U, R, B, T axes) in Pulses.

---

## ⚙️ Prerequisites

- Python 3.8 or higher.
- A physical LAN connection between your PC and the Yaskawa Controller. (Your PC must be set to a Static IP on the same subnet, e.g., `192.168.10.XX`).
- The robot controller must be set to **Remote Mode** and capable of turning **Servo ON**.

## 📦 Installation

1. Clone this repository to your local machine:
   ```bash
   git clone <your-repository-url>
   cd <your-project-folder>
(Recommended) Create and activate a Virtual Environment:

Bash
python -m venv .yaskava_env

# For Linux/Mac:
source .yaskava_env/bin/activate  

# For Windows:
.yaskava_env\Scripts\activate 
Install all required dependencies using requirements.txt:

Bash
pip install -r requirements.txt
Note: The robot control library is based on UnderAutomation/Yaskawa.py.

🚀 Usage
Inside the main script (e.g., triangle.py), you will find a configuration section at the top of the main() function. You can adjust these variables before running:

Python
SIMULATION_MODE = True    # Set to True to preview graphs without moving the real robot.
ROBOT_SPEED = 10          # The movement speed of the robot (%).
STEP_SIZE = 80            # The distance between trajectory points (helps prevent 'Manipulator Operating' errors).
DELAY_BETWEEN_STEPS = 1   # Pause duration (in seconds) to allow the robot to finish each step.
To run the program:

Bash
python triangle.py

📊 Output Graphs Explained
Upon successful execution (in either Simulation or Real Robot mode), a window with 3 graphs will appear:

Left (Y-Z Plane): A front-view visualization of the End-Effector drawing the equilateral triangle.

Center (Orientation): Displays the Rx (180°), Ry (-8.976°), and Rz (0°) angles as flat horizontal lines, proving the wrist orientation is locked.

Right (Joint Pulses): Shows the pulse values of the 6 motors (S, L, U, R, B, T) over time, allowing you to analyze how each joint contributes to the linear Cartesian movement.

⚠️ Safety Warning
Robot Hazard: Industrial robots move at high speeds and with significant force.

Before changing SIMULATION_MODE = False, physically verify that the robot's workspace is completely clear of people, cables, and obstacles.

The Operator MUST hold the Teach Pendant in their hands and be ready to press the Emergency Stop (E-Stop) button at all times while this script is executing.


Group 8:
Thanpisit Banyam    6601023611035
Putthakhun Horthong 6601023621022
Teetawat Songsaard  6601023621065