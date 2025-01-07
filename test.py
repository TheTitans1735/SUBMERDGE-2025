from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait,StopWatch




class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.previous_error = 0
        self.integral = 0

    def compute(self, target, current):
        error = target - current
        self.integral += error
        derivative = error - self.previous_error
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.previous_error = error
        return output

class Robot:
    def __init__(self):
        self.hub = PrimeHub()
        self.left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.B)
        self.motor_front = Motor(Port.C)
        self.motor_back = Motor(Port.D)
        self.drive_base = DriveBase(self.left_motor, self.right_motor, 57, 11.2)  # הגדרת ה-DriveBase
        self.left_color_sensor = ColorSensor(Port.E)
        self.right_color_sensor = ColorSensor(Port.A)
        self.gyro_sensor = self.hub.imu
        

    def drive_straight_pid(
        self, 
        distance_cm, 
        target_speed=450, 
        stop_at_end=True, 
        timeout_seconds=None, 
        gradual_stop=True, 
        gradual_stop_distance=10,
        gradual_start=True,
        gradual_start_distance=10,
    ):
        """
        Drive straight using PID control for the DriveBase based on the drive base angle.
        Negative distance_cm values will drive backwards.
        :param distance_cm: Distance in centimeters.
        :param speed: Speed in degrees per second.
        :param stop_at_end: Whether to stop the motors when finished.
        :param timeout_seconds: Timeout for the movement (optional).
        """
        # Initialize PID controller
        # p = סטייה עכשיות 
        # i = מתקן לזווית 0
        # d = מחזיר למסלול המקורי
        pid = PIDController(kp=0.8, ki=0.13, kd=2.2)
        # Initialize the timer
        timer = StopWatch()
        # Calculate the target angle
        target_distance = distance_cm * 10
        #set the speed according to the distance
        if distance_cm < 0:
            target_speed = -target_speed
        # reset robot angle and distance
        self.drive_base.reset()
        direction = 1 if distance_cm > 0 else -1

        # Drive until the target distance is reached, correct angle using PID
        while True:
            # Calculate the current angle
            current_angle = self.drive_base.angle()
            # Calculate the correction
            correction = pid.compute(0, current_angle)
            # Calculate the speed if gradual start/stop is enabled according to distance
            if abs(self.drive_base.distance()) < target_distance / 2:
                speed = target_speed
                if gradual_start:
                    speed = target_speed * abs(self.drive_base.distance()) / (target_distance / 2)
            else:
                speed = target_speed
                if gradual_stop:
                    speed = target_speed * (target_distance - abs(self.drive_base.distance())) / (target_distance / 2)        
            #set minimum speed
            if abs(speed) < 100:
                speed = 100 * direction 
            # speed = target_speed
            # Set the motor speed
            self.drive_base.drive(speed, correction)
            # Check if the target distance is reached
            if abs(self.drive_base.distance()) >= abs(target_distance):
                break
            # Check if the timeout is reached
            if timeout_seconds is not None and timer.time() > timeout_seconds:
                break
            # Wait for the next iteration
            wait(10)
        # Stop the motors
        if stop_at_end:
            self.drive_base.stop()


ilan = Robot()
# ilan.drive_straight(10)  # נסיעה 10 ס"מ
ilan.drive_straight_pid(50, 250)