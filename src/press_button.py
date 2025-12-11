from gpiozero import Servo, Device
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep
import math

# Use lgpio pin factory for better PWM control
Device.pin_factory = LGPIOFactory()

GPIO_PIN = 18

START_ANGLE = 1.0      # Starting position (resting angle)
END_ANGLE = 0.0        # Maximum extension to press button
STEP = 0.05            # Small increments for smooth motion
TIME_TO_PRESS = 2.0    # Total time in seconds to press the button

servo = Servo(GPIO_PIN)

def press_button():
    """
    Move servo from rest, go to max, return to rest,
    then slowly press the button over TIME_TO_PRESS seconds
    """
    try:
        # Step 1: Move all the way UP to max distance
        print("Moving servo UP to maximum distance...")
        servo.max()
        sleep(1.0)
        
        # Step 2: Go back down to START_ANGLE
        print(f"Returning to start angle: {START_ANGLE}")
        servo.value = START_ANGLE
        sleep(1.0)
        
        # Step 3: Slowly move from START_ANGLE to END_ANGLE
        print(f"Slowly pressing button over {TIME_TO_PRESS} seconds...")
        
        # Calculate number of steps and sleep interval
        angle_range = abs(END_ANGLE - START_ANGLE)
        num_steps = math.ceil(angle_range / STEP)
        sleep_interval = TIME_TO_PRESS / num_steps
        
        current_angle = START_ANGLE
        for i in range(num_steps):
            current_angle = START_ANGLE - (i + 1) * STEP
            current_angle = max(current_angle, END_ANGLE)
            servo.value = current_angle
            sleep(sleep_interval)
        
        # Ensure we reach exactly END_ANGLE
        servo.value = END_ANGLE
        
        print(f"Button pressed! Servo at angle: {servo.value}")
        
    finally:
        servo.close()

if __name__ == "__main__":
    press_button()