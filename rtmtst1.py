from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Button
from pybricks.tools import wait

# Create a hub object
hub = PrimeHub()

# Create motors on Port A and Port F
motor_a = Motor(Port.A)
motor_f = Motor(Port.F)

# State variables to track each motor's status and direction
motor_a_running = False
motor_a_direction = 1  # 1 for forward, -1 for backward

motor_f_running = False
motor_f_direction = 1  # 1 for forward, -1 for backward

# Variables to track button press states
button_left_pressed = False
button_right_pressed = False

# Main loop
while True:
    try:
        # Handle Left Button for Motor A
        if Button.LEFT in hub.buttons.pressed() and not button_left_pressed:
            # Only register the press if the button hasn't been processed yet
            button_left_pressed = True
            
            if not motor_a_running:
                # Start motor A in the current direction
                motor_a.dc(2000* motor_a_direction)
                motor_a_running = True
            else:
                # Stop motor A if it's running
                motor_a.stop()
                motor_a_running = False
                # Toggle direction for next press
                motor_a_direction *= -1

        # Handle Right Button for Motor F
        if Button.RIGHT in hub.buttons.pressed() and not button_right_pressed:
            # Only register the press if the button hasn't been processed yet
            button_right_pressed = True
            
            if not motor_f_running:
                # Start motor F in the current direction
                motor_f.dc(2000* motor_f_direction)
                motor_f_running = True
            else:
                # Stop motor F if it's running
                motor_f.stop()
                motor_f_running = False
                # Toggle direction for next press
                motor_f_direction *= -1

        # If the button is no longer pressed, reset the button state
        if Button.LEFT not in hub.buttons.pressed():
            button_left_pressed = False
        if Button.RIGHT not in hub.buttons.pressed():
            button_right_pressed = False

        # Small delay to allow processing and debouncing
        wait(50)

    except Exception as e:
        print(f"Error: {e}")
