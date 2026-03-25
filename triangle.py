import time
import math
import numpy as np
import matplotlib.pyplot as plt

from underautomation.yaskawa.connect_parameters import ConnectParameters
from underautomation.yaskawa.high_speed_e_server.alarm_reset_type import AlarmResetType
from underautomation.yaskawa.yaskawa_robot import YaskawaRobot
from underautomation.yaskawa.high_speed_e_server.on_off_command_type import OnOffCommandType
from underautomation.yaskawa.high_speed_e_server.position_command_type import PositionCommandType
from underautomation.yaskawa.high_speed_e_server.position_command_classification import PositionCommandClassification
from underautomation.yaskawa.high_speed_e_server.position_command_operation_coordinate import PositionCommandOperationCoordinate

def main():
    # =========================================================
    # ⚙️ ส่วนตั้งค่าการทำงาน 
    # =========================================================
    SIMULATION_MODE = TRUE   # รันหุ่นจริง!
    
    ROBOT_SPEED = 10         
    STEP_SIZE =  80    
    DELAY_BETWEEN_STEPS = 1 
    
    fixed_x = 299.859
    home_y = 0.000
    home_z = 128.600
    
    fixed_rx = 180.000
    fixed_ry = -8.976
    fixed_rz = 0.000
    
    L = 150.0 
    h = L * (math.sqrt(3) / 2) 
    
    pt_bottom = (home_y, home_z)                           
    pt_top_right = (home_y - (L / 2), home_z + h)          
    pt_top_left = (home_y + (L / 2), home_z + h)           
    
    cy = (pt_bottom[0] + pt_top_right[0] + pt_top_left[0]) / 3.0
    cz = (pt_bottom[1] + pt_top_right[1] + pt_top_left[1]) / 3.0
    
    triangle_waypoints = [pt_bottom, pt_top_right, pt_top_left, pt_bottom]
    trajectory_points = []

    for i in range(len(triangle_waypoints)-1):
        y1, z1 = triangle_waypoints[i]
        y2, z2 = triangle_waypoints[i+1]
        
        dist = math.hypot(y2 - y1, z2 - z1)
        num_steps = max(1, int(dist / STEP_SIZE))
        
        for j in range(num_steps):
            y = y1 + (y2 - y1) * (j / num_steps)
            z = z1 + (z2 - z1) * (j / num_steps)
            trajectory_points.append((fixed_x, y, z, fixed_rx, fixed_ry, fixed_rz))
            
    trajectory_points.append((fixed_x, pt_bottom[0], pt_bottom[1], fixed_rx, fixed_ry, fixed_rz))

    # =========================================================
    # ส่วนควบคุมหุ่นยนต์
    # =========================================================
    recorded_y, recorded_z, recorded_rx, recorded_ry, recorded_rz = [], [], [], [], []
    recorded_j1, recorded_j2, recorded_j3 = [], [], []
    recorded_j4, recorded_j5, recorded_j6 = [], [], []

    if not SIMULATION_MODE:
        
    else:
        print("--- RUNNING IN SIMULATION MODE ---")
        # (ส่วนจำลอง โค้ดยังเหมือนเดิม)
        pass

    # =========================================================
    # พล็อตกราฟ
    # =========================================================
    if len(recorded_y) > 0: # ป้องกัน Error ตอนพล็อตกราฟถ้าหุ่นเดินไม่จบ
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))
        
        # 1. กราฟ Y-Z
        ax1.plot(recorded_y, recorded_z, 'b.-', markersize=4, label='End Effector Path')
        ax1.plot(cy, cz, 'r*', markersize=12, label=f'Center ({cy:.1f}, {cz:.1f})')
        ax1.plot(pt_bottom[0], pt_bottom[1], 'go', markersize=8, label='Home (Bottom Center)')
        ax1.set_title("Equilateral Triangle (Y-Z Plane)")
        ax1.set_xlabel("Y (mm) [Left-Right]")
        ax1.set_ylabel("Z (mm) [Up-Down]")
        ax1.axis('equal') 
        ax1.grid(True)
        ax1.legend()

       # 2. กราฟมุม Rx, Ry, Rz
        # สร้าง Time Steps ให้ถูกต้อง (0, 1, 2, ...)
        time_steps = np.arange(len(recorded_rx))
        
        ax2.plot(time_steps, recorded_rx, 'g-', linewidth=2, label='Rx Angle (180.0)')
        ax2.plot(time_steps, recorded_ry, 'm-', linewidth=2, label='Ry Angle (-8.976)')
        ax2.plot(time_steps, recorded_rz, 'c-', linewidth=2, label='Rz Angle (0.0)')
        
        ax2.set_title("End-Effector Orientation")
        ax2.set_xlabel("Time Step")
        ax2.set_ylabel("Angle (Degrees)")
        
        # ⚠️ เอา ax2.set_ylim() ออกไป เพื่อให้กราฟโชว์ค่าได้ตั้งแต่ -10 ถึง 190 อัตโนมัติ
        
        ax2.grid(True)
        ax2.legend(loc='center right') # ย้าย Legend ไปหลบทางขวาเพื่อไม่ให้บังเส้น Rz

        # 3. กราฟ Joint Angles ทั้ง 6 แกน (Pulse)
        if len(recorded_j1) > 0:
            ax3.plot(time_steps, recorded_j1, 'r-', label='Axis 1 (S)')
            ax3.plot(time_steps, recorded_j2, 'g-', label='Axis 2 (L)')
            ax3.plot(time_steps, recorded_j3, 'b-', label='Axis 3 (U)')
            ax3.plot(time_steps, recorded_j4, 'm-', label='Axis 4 (R)')
            ax3.plot(time_steps, recorded_j5, 'c-', label='Axis 5 (B)')
            ax3.plot(time_steps, recorded_j6, 'y-', label='Axis 6 (T)')
            ax3.set_title("Robot Joint Angles Trajectory")
            ax3.set_xlabel("Time Step")
            ax3.set_ylabel("Position (Pulse)")
            ax3.grid(True)
            ax3.legend(loc='best', fontsize='small')

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    main()