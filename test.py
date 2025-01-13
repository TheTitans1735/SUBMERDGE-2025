import keyboard

def my_function():
    print("Function triggered!")

# האזנה ללחיצה על מקש 'a'
keyboard.add_hotkey('a', my_function)

print("Press 'a' to trigger the function. Press 'esc' to exit.")
keyboard.wait('esc')  # התוכנית תסיים רק כשלוחצים על 'esc'
