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

    