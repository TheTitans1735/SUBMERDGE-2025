from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.parameters import Icon, Color, Button, Direction
from robot import Robot

ilan=Robot()
# # Port A - Right color sensor
# # Port B - Right wheel
# # Port C - Medium motor - front
# # Port D - Medium motor - back
# # Port E - Left color sensor
# # Port F - Left wheel

# hub = PrimeHub()
# left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
# right_motor = Motor(Port.B)
# motor_front = Motor(Port.C)
# motor_back = Motor(Port.D)
# drive_base = DriveBase(left_motor,right_motor,57,10) 


def drive():   
    ilan.drive_base.drive(150,0)


def reverse_drive():
    ilan.drive_base.drive(-100, 0)

def turn_left():
    ilan.drive_base.turn(-360,wait=False)

def turn_right():
    ilan.drive_base.turn(360,wait=False)

def front_motor():
    ilan.motor_front.dc(50)

def back_motor():
    ilan.motor_back.dc(50)

def front_motor_reverse():
    ilan.motor_front.dc(-50)
    
def back_motor_reverse():
    ilan.motor_back.dc(-50)

def stop_all():
    ilan.drive_base.stop()
    ilan.motor_back.stop()
    ilan.motor_front.stop()

def nigg():
    
    ilan.drive_base.straight(320.50)
    wait(1000)
    ilan.motor_back.dc(80)
    wait(1000)
    ilan.motor_back.dc(-10)
    ilan.drive_base.straight(20)
    wait(1000)  
    ilan.drive_base.straight(-350)

def test():

    ilan.drive_straight(10)
    wait(2000)
    ilan.drive_back(10)

def crabs():
    ilan.drive_base.curve(angle=-180, radius=0)

def test2():
    ilan.run_back_motor(250,720)



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
    ("6", test, Icon.FALSE),
    ("crabs", crabs, Icon.HAPPY),
    ("7",test2, Icon.FULL),
]
current_run = 0
print("current", ilan.hub.battery.current(), "voltage", ilan.hub.battery.voltage())

while True:
    try:
        if (Button.LEFT in ilan.hub.buttons.pressed()):
            current_run += 1
            if current_run >= len(runs):
                current_run = 0
            if len(runs[current_run]) ==2:
                ilan.hub.display.char(runs[current_run][0])
            else:
                ilan.hub.display.icon(runs[current_run][2])

        elif (Button.RIGHT in ilan.hub.buttons.pressed()):
            runs[current_run][1]()
        else:
            stop_all()
    except Exception as e:
         print(e)
         raise e
    finally:
        wait(100)


