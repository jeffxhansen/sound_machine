from gpiozero import Servo, Device
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep
import threading

# Use lgpio pin factory for better PWM control
Device.pin_factory = LGPIOFactory()

GPIO_PIN = 18

servo = Servo(GPIO_PIN)

moving = True
servo_value = 0
direction = 1  # 1 for forward, -1 for backward

def move_servo():
    global servo_value, direction
    
    while moving:
        # Change direction when approaching max/min
        if servo_value >= 0.9:
            direction = -1
        elif servo_value <= -0.9:
            direction = 1
        
        # Move very slowly in small increments
        servo_value += direction * 0.005
        servo.value = servo_value
        sleep(0.2)

try:
    print("Starting continuous wave motion...")
    print("Press ENTER to stop")
    
    # Start servo movement in background thread
    servo_thread = threading.Thread(target=move_servo, daemon=True)
    servo_thread.start()
    
    # Wait for user to press enter
    input()
    
    print("Stopping servo...")
    moving = False
    servo_thread.join(timeout=1)
    
finally:
    servo.close()
