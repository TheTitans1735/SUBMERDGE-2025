from re import M
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.parameters import Icon, Color, Button

# # Port A - Right color sensor
# # Port B - Right wheel
# # Port C - Medium motor - front
# # Port D - Medium motor - back
# # Port E - Left color sensor
# # Port F - Left wheel

hub = PrimeHub()
left_motor = Motor(Port.F)
right_motor = Motor(Port.B)
motor_front = Motor(Port.C)
motor_back = Motor(Port.D)
drive_base = DriveBase(left_motor,right_motor,57,10) 
# current_direction = None
# counter = 0
# while True:
#     if current_direction is not None and (
#         Button.LEFT in hub.buttons.pressed() or
#         Button.RIGHT in hub.buttons.pressed()
#     ):
#         left_motor.hold()
#     elif Button.LEFT in hub.buttons.pressed():
#         # Hello - בדיקה
#         counter = 0
#         left_motor.dc(100)
#         current_direction = "LEFT"
#     elif Button.RIGHT in hub.buttons.pressed():
#         # Hello - בדיקה
#         counter = 0
#         left_motor.dc(-100)
#         current_direction = "RIGHT"
#     if counter == 20:
#         left_motor.hold()
#     counter += 1
#     wait(250)









def drive():
    drive_base.straight(100)

def reverse_drive():
    drive_base.straight(-100)










runs = [

    ("1-drive",drive),
    ("2-reverse_drive",reverse_drive)
]
current_run = 0
hub.display.text(runs[current_run][0])
while True:
        if (Button.LEFT in hub.buttons.pressed()):
             current_run += 1
        if current_run >= len(runs):
            current_run = 0
            hub.display.text(runs[current_run][0])
        if (Button.RIGHT in hub.buttons.pressed()):
            