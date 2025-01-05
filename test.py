

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
        

    def drive_straight_pid(self, distance_cm, speed=450, direction=1, stop_at_end=True, timeout_seconds=None):
        """
        Drive straight using PID control for the DriveBase based on the IMU angle.
        :param distance_cm: Distance in centimeters.
        :param speed: Speed in degrees per second.
        :param direction: 1 for forward, -1 for backward.
        :param stop_at_end: Whether to stop the motors when finished.
        :param timeout_seconds: Timeout for the movement (optional).
        """
        pid = PIDController(kp=2, ki=0.01, kd=0.5)  # הגדרת פרמטרי PID
        target_distance = distance_cm * 10  # המרחק במילימטרים (המרה מ-ס"מ למ"מ)
        target_angle = 0

        # Reset motor angles to zero at the start
        self.drive_base.reset()

        timer = StopWatch()


        while True:
            # קבלת הזווית הנוכחית מה-DriveBase
            current_angle = self.drive_base.angle()

            # חישוב ההפרש בין הזווית הנוכחית לזווית היעד
            error = target_angle - current_angle
            pid_output = pid.compute(0, error)  # PID יחפש לתקן את ההפרש

            # הדפסת דיבוג
            print(f"Current angle: {current_angle}, Target angle: {target_angle}, PID Output: {pid_output}")

            # עדכון המהירות של ה-DriveBase לפי פלט ה-PID
            self.drive_base.drive(direction * speed , pid_output)

            # מחשבים את הזווית הכוללת על פי המנועים
            current_distance = self.drive_base.distance()

            # בדיקת תנאי סיום (כשהגענו למרחק הרצוי)
            if abs(target_distance - current_distance) < 5:  # מרחק שגיאה קטן מספיק להפסיק את הנהיגה
                if stop_at_end:
                    self.drive_base.stop()
                break

            # בדיקת זמן אם יש זמן פסק זמן
            if timeout_seconds and (timer.time() > timeout_seconds):
                self.drive_base.stop()
                break

            wait(10)

ilan = Robot()
# ilan.drive_straight(10)  # נסיעה 10 ס"מ
ilan.drive_straight_pid(50, 250, 1)