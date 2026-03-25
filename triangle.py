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
    
    