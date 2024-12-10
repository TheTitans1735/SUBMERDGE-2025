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

hub = PrimeHub()
left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
motor_front = Motor(Port.C)
motor_back = Motor(Port.D)
drive_base = DriveBase(left_motor,right_motor,57,10) 


def drive():   
    drive_base.drive(100)


def reverse_drive():
    drive_base.drive(-100, 0)

def turn_left():
    drive_base.turn(-360,wait=False)

def turn_right():
    drive_base.turn(360,wait=False)

def front_motor():
    motor_front.dc(50)

def back_motor():
    motor_back.dc(50)

def front_motor_reverse():
    motor_front.dc(-50)
    
def back_motor_reverse():
    motor_back.dc(-50)

def stop_all():
    drive_base.stop()
    motor_back.stop()
    motor_front.stop()

def nigg():
    
    drive_base.straight(-320.50)
    wait(1)
    motor_back.dc(-123)
    wait(1)
    drive_base.straight(-20)
    wait(1)  
    drive_base.straight(350)



runs = [
    ("5", drive, Icon.ARROW_LEFT),
    ("6", reverse_drive, Icon.ARROW_RIGHT),
    ("7", turn_left, Icon.ARROW_LEFT_DOWN),
    ("8", turn_right, Icon.ARROW_LEFT_UP),
    ("1", front_motor),
    ("2", back_motor),
    ("3", front_motor_reverse),
    ("4", back_motor_reverse),
    ("5", nigg, Icon.CIRCLE),
    
]
current_run = 0
print("current", hub.battery.current(), "voltage", hub.battery.voltage())
# hub.display.icon(runs[current_run][2])
# hub.display.char(runs[current_run][0])
while True:
    try:
        if (Button.LEFT in hub.buttons.pressed()):
            current_run += 1
            if current_run >= len(runs):
                current_run = 0
            hub.display.char(runs[current_run][0])
            hub.display.icon(runs[current_run][2])

        elif (Button.RIGHT in hub.buttons.pressed()):
            runs[current_run][1]()
        else:
            stop_all()
    except:
         pass
    finally:
        wait(100)
