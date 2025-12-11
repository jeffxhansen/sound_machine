import RPi.GPIO as GPIO
import time

GPIO_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)

pwm = GPIO.PWM(GPIO_PIN, 50)
pwm.start(0)

try:
    duty_cycle = 7.5 + (45 / 18.0)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    print(f"Moved servo to 45 degrees (duty cycle: {duty_cycle}%)")
    
finally:
    pwm.stop()
    GPIO.cleanup()
