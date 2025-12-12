from gpiozero import Servo, Device
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep

# Use lgpio pin factory for better PWM control
Device.pin_factory = LGPIOFactory()

GPIO_PIN = 18

servo = Servo(GPIO_PIN)

try:
    
    max_up_position = -0.4
    end_position = 0.5
    
    servo.value = max_up_position
    sleep(0.5)
    servo.value = end_position
    sleep(0.5)
    servo.value = max_up_position
    sleep(0.5)
    
finally:
    servo.close()
