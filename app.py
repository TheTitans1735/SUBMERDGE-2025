from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch, run_task, multitask
from pybricks.parameters import Icon, Color, Button, Direction
from robot import Robot
# from pynput import keyboard

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


async def drive():   
    ilan.drive_base.drive(100,0)


async def reverse_drive():
    ilan.drive_base.drive(-750, 0)

async def turn_left():
    await ilan.drive_base.turn(-360, wait=False)

async def turn_right():
    await ilan.drive_base.turn(360, wait=False)

async def front_motor():
    ilan.motor_front.dc(500)

async def back_motor():
    ilan.motor_back.dc(500)

async def front_motor_reverse():
    ilan.motor_front.dc(-50)
    
async def back_motor_reverse():
    ilan.motor_back.dc(-500)

async def stop_all():
    ilan.drive_base.stop()
    ilan.motor_back.stop()
    ilan.motor_front.stop()

async def nigg():
    await ilan.drive_base.straight(320.50)
    await wait(1000)
    ilan.motor_back.dc(80)
    await wait(1000)
    ilan.motor_back.dc(-10)
    await ilan.drive_base.straight(20)
    await wait(1000)
    await ilan.drive_base.straight(-350)

async def turn():
    await ilan.turn(90,150)
    await ilan.wait_for_button(True)
    await wait(1000)
    await ilan.turn(-90, 150)

async def prepare_whale_motor():
    await ilan.run_back_motor(100,100)
    # await wait(1000)
    await ilan.run_back_motor(200,-290)

async def whale():
    # await ilan.drive_straight(20)
    # await ilan.run_back_motor(100,100)
    # await ilan.run_back_motor(100,-290)
    # await ilan.wait_for_button()
    # await ilan.drive_straight(46)
    await multitask(ilan.drive_straight(70), prepare_whale_motor())
    await ilan.wait_for_button(debug=False)
    await ilan.turn(40)
    await ilan.wait_for_button(debug=False)
    await ilan.drive_straight(14,100)
    await ilan.drive_back(2,150)
    await ilan.drive_until_both_on_line()
    await ilan.drive_straight(2,150)

async def sonar():
    await ilan.drive_back_old(30,300)
    await ilan.turn(80,200)
    await ilan.drive_straight_old(13)
    await ilan.run_back_motor(150,-210)
    await ilan.drive_back_old(53,10)
    await ilan.run_back_motor(300,-90)

async def crabs():
    await ilan.drive_back(89,200)
    await ilan.drive_straight(-90,200)
    await ilan.arc_turn(20,200)
    await ilan.drive_straight(12,200)
    await ilan.arc_turn(-90,200)
    await ilan.drive_straight(39,200)
    await ilan.drive_back(18,200)
    await ilan.arc_turn(90,200)
    await ilan.drive_back(22,200)
    await ilan.drive_back(7,200)
    await ilan.motor_back.run_angle(250,200)
    await ilan.drive_straight(8,50)
    await ilan.drive_straight(60,200)
    await ilan.drive_straight(10,200)

async def massive():
    await ilan.drive_straight(40,200)
    await ilan.wait_for_button()
    await multitask(ilan.motor_back.run_angle(-2000,2000), await ilan.drive_straight(16.5,200))
    await ilan.wait_for_button()
    await ilan.motor_back.run_angle(70,2000)
    await ilan.wait_for_button()
    await ilan.drive_straight(1.5,200)
    await ilan.wait_for_button()
    await ilan.motor_front.run_angle(300,1000)
    await ilan.wait_for_button()
    await ilan.motor_front.run_angle(-400,1000)
    await ilan.wait_for_button()
    await ilan.motor_front.run_angle(200,1000)
    await ilan.wait_for_button()
    await ilan.drive_back(10,200)
    await ilan.wait_for_button()
    await ilan.turn(30,200)
    await ilan.wait_for_button()
    await ilan.drive_back(40,200)

async def test():
    await multitask(ilan.drive_straight(16,100), ilan.motor_back.run_angle(75,128))
    # await ilan.drive_straight(-20,200)
    await ilan.motor_back.run_angle(75,128)
    exit()

# this is the main program
async def main():
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
        ("1", massive, Icon.LEFT),
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
                await runs[current_run][1]()

            elif (Button.BLUETOOTH in ilan.hub.buttons.pressed()):
                await test()
            else:
                await stop_all()
        except Exception as e:
            print(e)
            raise e
        finally:
            await wait(100)


run_task(main())