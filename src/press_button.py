import RPi.GPIO as GPIO
from time import sleep
import math

GPIO_PIN = 18
PWM_FREQUENCY = 50  # 50 Hz for servo control

START_ANGLE = 1.0      # Starting position (resting angle)
END_ANGLE = 0.0        # Maximum extension to press button
STEP = 0.05            # Small increments for smooth motion
TIME_TO_PRESS = 2.0    # Total time in seconds to press the button

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)
pwm = GPIO.PWM(GPIO_PIN, PWM_FREQUENCY)

def angle_to_duty_cycle(angle):
    """
    Convert servo angle (-1.0 to 1.0) to PWM duty cycle (2% to 12%)
    -1.0 = 2% (0ms), 0.0 = 7% (1.5ms), 1.0 = 12% (2.4ms)
    """
    return 7 + (angle * 5)

def press_button():
    """
    Move servo from rest, go to max, return to rest,
    then slowly press the button over TIME_TO_PRESS seconds
    """
    try:
        pwm.start(0)
        
        # Step 1: Move all the way UP to max distance
        print("Moving servo UP to maximum distance...")
        pwm.ChangeDutyCycle(angle_to_duty_cycle(1.0))
        sleep(1.0)
        
        # Step 2: Go back down to START_ANGLE
        print(f"Returning to start angle: {START_ANGLE}")
        pwm.ChangeDutyCycle(angle_to_duty_cycle(START_ANGLE))
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
            pwm.ChangeDutyCycle(angle_to_duty_cycle(current_angle))
            sleep(sleep_interval)
        
        # Ensure we reach exactly END_ANGLE
        pwm.ChangeDutyCycle(angle_to_duty_cycle(END_ANGLE))
        
        print(f"Button pressed! Servo at angle: {END_ANGLE}")
        
    finally:
        pwm.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    press_button()