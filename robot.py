
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.parameters import Icon, Color, Button, Direction

# # Port A - Right color sensor
# # Port B - Right wheel
# # Port C - Medium motor - front
# # Port D - Medium motor - back
# # Port E - Left color sensor
# # Port F - Left wheel


class Robot:
    def __init__(self):
        self.hub = PrimeHub()
        self.left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.B)
        self.motor_front = Motor(Port.C)
        self.motor_back = Motor(Port.D)
        self.drive_base = DriveBase(self.left_motor, self.right_motor,57,10) 


    def drive_straight(
        self,
        speed, 
        distance_cm, 
        timeout_seconds, 
        stop_at_end,

    ):
        self.drive_base.drive(speed,0)
        self.drive_base.

    def drive_back(self, distance_cm, timeout_seconds, stop_at_end):
        pass
