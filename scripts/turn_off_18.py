from gpiozero import Servo, Device
from gpiozero.pins.lgpio import LGPIOFactory

# Use lgpio pin factory for better PWM control
Device.pin_factory = LGPIOFactory()

GPIO_PIN = 18

servo = Servo(GPIO_PIN)

try:
    print("Removing power from GPIO18 servo...")
    
    # Disable PWM completely - removes all power
    servo.value = None
    print("Servo power removed. You can now move it by hand.")
    
finally:
    servo.close()
