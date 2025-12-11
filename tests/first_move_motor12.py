from gpiozero import Servo, Device
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep

# Use lgpio pin factory for better PWM control
Device.pin_factory = LGPIOFactory()

GPIO_PIN = 18

servo = Servo(GPIO_PIN)

try:
    # Move servo to max position (90 degrees)
    # gpiozero Servo uses -1 to 1 range where -1 is -90°, 0 is 0°, 1 is 90°
    # Max position = 1
    print(f"Setting servo to max position (90 degrees)...")
    servo.value = 1
    print(f"Servo value set to: {servo.value}")
    sleep(0.5)
    print("Moved servo to max position")
    
finally:
    servo.close()
