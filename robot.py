

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Stop
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
        # self.drive_base.use_gyro(True)


    def drive_straight(
        self,
        distance_cm, 
        speed=800, 
        timeout_seconds=None,   # TODO: Support drive by seconds
        stop_at_end=True,
        acceleration_rate=400,
        deceleration_rate=400,
    ):
        self.drive_base.settings(
            straight_speed=speed, 
            straight_acceleration=(acceleration_rate, deceleration_rate), 
            turn_rate=None, 
            turn_acceleration=None,
        )
        self.drive_base.straight(
            distance=distance_cm*10,
            then=Stop.HOLD if stop_at_end else Stop.NONE,
            wait=True,
        )

    def drive_back(
        self,
        distance_cm, 
        speed=800, 
        timeout_seconds=None,   # TODO: Support drive by seconds
        stop_at_end=True,
        acceleration_rate=400,
        deceleration_rate=400,
    ):
        self.drive_straight(
            distance_cm=-1*distance_cm, 
            speed=speed,
            timeout_seconds=timeout_seconds,
            stop_at_end=stop_at_end,
            acceleration_rate=acceleration_rate,
            deceleration_rate=deceleration_rate,
        )

    def run_front_motor(self, speed, angle):

        self.motor_front.reset_angle(angle=0)
        self.motor_front.run_target(speed, target_angle=angle, then=Stop.HOLD, wait=True)
    def run_back_motor(
            self,
            speed,
            angle,
    ):
        self.motor_back.reset_angle(angle=0)
        self.motor_back.run_target(speed, target_angle=angle, then=Stop.HOLD, wait=True)