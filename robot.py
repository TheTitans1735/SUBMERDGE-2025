# -*- coding: utf-8 -*-
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
from pybricks.parameters import Icon, Color, Button, Direction
from pybricks.pupdevices import Motor, ColorSensor


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
        self.drive_base = DriveBase(self.left_motor, self.right_motor,57,11.2) 
        self.left_color_sensor = ColorSensor(Port.E)    
        self.right__color_sensor = ColorSensor(Port.A)       
            # self.drive_base.use_gyro(True)

    def drive_straight(
        self,
        distance_cm, 
        speed=450, 
    
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
        speed=450, 
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

    def run_front_motor(self, speed, angle, wait= True):

        self.motor_front.reset_angle(angle=0)
        self.motor_front.run_target(speed, target_angle=angle, then=Stop.HOLD, wait=wait)
        
    def run_back_motor(
            self,
            speed,
            angle,
            wait= True
    ):
        self.motor_back.reset_angle(angle=0)
        self.motor_back.run_target(speed, target_angle=angle, then=Stop.HOLD, wait=wait)

    def arc_turn(self, radius_cm, angle_deg, speed=150):
        """
        Moves the robot in an arc with a specified radius (in cm) and angle (in degrees).
        The radius is measured from the center of the robot to the midpoint between the wheels.
        """
        # Robot dimensions
        wheel_diameter_mm = 57  # Diameter of the wheel in mm
        axle_track_cm = 11.2  # Distance between the wheels in cm
        gyro_offset_cm = 3.5  # Distance of gyro from wheel center
        wheel_circumference_mm = wheel_diameter_mm * 3.14159  # Circumference of the wheel in mm

        # Adjust the radius to account for the gyro's offset
        effective_radius_cm = radius_cm - gyro_offset_cm

        # Calculate the path lengths for the inner and outer wheels
        outer_radius_cm = effective_radius_cm + (axle_track_cm / 2)
        inner_radius_cm = effective_radius_cm - (axle_track_cm / 2)

        # Circumferences of the outer and inner arcs
        outer_arc_length_cm = (2 * 3.14159 * outer_radius_cm) * (angle_deg / 360)  # outer circumference * number of rounds
        inner_arc_length_cm = (2 * 3.14159 * inner_radius_cm) * (angle_deg / 360)  # inner circumference * number of rounds

        # Convert arc lengths to wheel rotations
        outer_rotations = (outer_arc_length_cm * 10) / wheel_circumference_mm  # in rotations
        inner_rotations = (inner_arc_length_cm * 10) / wheel_circumference_mm  # in rotations

        # Calculate speed ratio
        if outer_rotations != 0:  # Prevent division by zero
            speed_ratio = inner_rotations / outer_rotations
        else:
            speed_ratio = 0

        # Ensure both motors complete their movements together
        if radius_cm > 0:  # Turning right
            self.right_motor.run_angle(speed * speed_ratio, inner_rotations * 360, wait=False)  # Inner wheel
            self.left_motor.run_angle(speed, outer_rotations * 360, wait=True)  # Outer wheel
        else:  # Turning left
            self.left_motor.run_angle(speed * speed_ratio, inner_rotations * 360, wait=False)  # Inner wheel
            self.right_motor.run_angle(speed, outer_rotations * 360, wait=True)  # Outer wheel

        # Stop the motors
        self.left_motor.brake()
        self.right_motor.brake()

        print(f"Completed arc turn: Radius = {radius_cm} cm, Angle = {angle_deg}° (Adjusted for gyro offset).")

    def turn(self, target_angle, speed=150):    
        # Reset the built-in gyro sensor to 0 (start angle)
        self.hub.imu.reset_heading(0)

        # Get the current angle
        current_angle = self.hub.imu.heading()

        # Calculate the difference between target and current angle
        angle_diff = target_angle - current_angle
        
        # If the difference is positive, turn right, if negative, turn left
        if angle_diff > 0:
            self.left_motor.run(speed)
            self.right_motor.run(-speed)
        else:
            self.left_motor.run(-speed)
            self.right_motor.run(speed)

        # Keep turning until we reach the target angle
        while abs(self.hub.imu.heading() - target_angle) > 2:  # Tolerance of 2 degrees
            wait(20)  # Wait a little before checking again

        # Stop the motors once we reach the target angle

    def wait_for_button(self,debug = True):
        if not debug:
            return
        self.hub.light.blink(Color.MAGENTA,[1000])
        while not self.hub.buttons.pressed():
            wait(100)
        self.hub.light.on(Color.BLUE)
    
    def drive_until_both_on_line(self, threshold=20, speed=200):
      
        self.left_motor.run(speed)
        self.right_motor.run(speed)

        while True:
            left_intensity = self.left_color_sensor.reflection()        # קריאת חיישן שמאלי
            right_intensity = self.right__color_sensor.reflection()     # קריאת חיישן ימני            
            print(f"Left: {left_intensity}, Right: {right_intensity}")  # דיבוג

            if left_intensity < threshold: 
                self.left_motor.stop()
            if right_intensity < threshold:
                self.right_motor.stop()

            # אם שני החיישנים מזהים קו (ערכים מתחת לסף)
            if left_intensity < threshold and right_intensity < threshold:
                print("Both sensors detected the line!")
                break

    def align_to_line(self, threshold=20, speed=100):
        """
        יישור הרובוט כך ששני החיישנים נמצאים על הקו.
        :param threshold: ערך זיהוי הקו.
        :param speed: מהירות התנועה.
        """
        while True:
            left_intensity = self.left_color_sensor.reflection()
            right_intensity = self.right__color_sensor.reflection()

            # אם החיישן השמאלי לא מזהה קו, הנע את המנוע השמאלי
            if left_intensity >= threshold:
                self.left_motor.run(speed)
            else:
                self.left_motor.stop()

            # אם החיישן הימני לא מזהה קו, הנע את המנוע הימני
            if right_intensity >= threshold:
                self.right_motor.run(speed)
            else:
                self.right_motor.stop()

            if left_intensity < threshold and right_intensity < threshold:
                print("Aligned to the line!")
                break
