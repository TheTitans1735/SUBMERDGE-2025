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
    ilan.drive_base.drive(151,0)


def reverse_drive():
    ilan.drive_base.drive(-750, 0)

def turn_left():
    ilan.drive_base.turn(-360,wait=False)

def turn_right():
    ilan.drive_base.turn(360,wait=False)

def front_motor():
    ilan.motor_front.dc(500)

def back_motor():
    ilan.motor_back.dc(500)

def front_motor_reverse():
    ilan.motor_front.dc(-50)
    
def back_motor_reverse():
    ilan.motor_back.dc(-500)

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

def turn():
    # ilan.drive_base.curve(angle=-180, radius=0)
    ilan.turn(90,150)
    ilan.wait_for_button(True)
    wait(1000)
    ilan.turn(-90, 150)


def whale():
    ilan.drive_straight(20)
    ilan.motor_back.run_until_stalled(100, duty_limit=50)
    ilan.run_back_motor(400,-90, wait= False)
    ilan.wait_for_button()
    ilan.drive_straight(52)
    ilan.wait_for_button(debug= False)
    ilan.motor_back.run_until_stalled(30, duty_limit=40)
    ilan.motor_back.run_angle(100,-90, wait= False)
    ilan.turn(47)
    ilan.wait_for_button(debug= False)
    ilan.drive_straight(19,100)
    ilan.drive_back(2,150)
    ilan.drive_until_both_on_line()
    ilan.drive_straight(2,150)

def sonar():
    ilan.drive_back(30,300)
    ilan.turn(90)
    ilan.drive_straight(13)
    ilan.run_back_motor(50,-120)
    ilan.turn(-5)
    ilan.drive_back(49)
    ilan.run_back_motor(-90,300)
    # ilan.arc_tur

def crabs():
    ilan.drive_back(89,200)
    ilan.drive_straight(-90,200)
    ilan.arc_turn(20,200)
    ilan.drive_straight(12,200)
    ilan.arc_turn(-90,200)
    ilan.drive_straight(39,200)
    ilan.drive_back(18,200)
    ilan.arc_turn(90,200)
    ilan.drive_back(22,200)
    ilan.arc_turn(90,200)
    ilan.drive_back(7,200)
    ilan.motor_back.angle(250,200)
    ilan.drive_straight(8,50)
    ilan.arc_turn(180,200)
    ilan.drive_straight(60,200)
    ilan.arc_turn(10,200)
    ilan.drive_straight(10,200)
    
def test():
    # ilan.arc_turn(5, 180, 450)
    # ilan.drive_straight_pid(200,3000)
    # ilan.drive_until_both_on_line()
    ilan.drive_straight(20,250)
    # wait(1000)
    # ilan.drive_straight(-50,100)

    # ilan.turn(90,150)
    # ilan.drive_straight(115,550)
    # ilan.turn(90,150)
    # ilan.drive_straight(75,300)

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
    ("6", turn, Icon.CLOCKWISE),
    ("crabs", crabs, Icon.HAPPY),
    ("7",whale, Icon.FULL),
    ("T", test),
    ("8", sonar,Icon.HEART),
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

        elif (Button.BLUETOOTH in ilan.hub.buttons.pressed()):
            test()
        else:
            stop_all()
    except Exception as e:
         print(e)
         raise e
    finally:
        wait(100)


