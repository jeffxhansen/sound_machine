from gpiozero import Servo, Device
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep

# Use lgpio pin factory for better PWM control
Device.pin_factory = LGPIOFactory()

GPIO_PIN = 18

servo = Servo(GPIO_PIN)

try:
    print("Starting wave motion...")
    
    # Wave 5 times, fluctuating between -0.33 (30 degrees) and 0.33 (60 degrees)
    # Center is around 0 (0 degrees), so we move ±0.33 around center
    min_angle = -0.33  # ~30 degrees
    max_angle = 0.33   # ~60 degrees
    
    for wave in range(5):
        print(f"Wave {wave + 1}/5")
        
        # Swing to max
        servo.value = max_angle
        sleep(0.2)
        
        # Swing to min
        servo.value = min_angle
        sleep(0.2)
    
    # Return to center
    servo.value = 0
    print("Wave motion complete!")
    
finally:
    servo.close()
