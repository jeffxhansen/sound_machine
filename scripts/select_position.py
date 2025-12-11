import RPi.GPIO as GPIO
from time import sleep

GPIO_PIN = 18
PWM_FREQUENCY = 50  # 50 Hz for servo control
STEP_SIZE = 0.05  # Increment for each step

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)
pwm = GPIO.PWM(GPIO_PIN, PWM_FREQUENCY)

current_position = 0.0

def angle_to_duty_cycle(angle):
    """
    Convert servo angle (-1.0 to 1.0) to PWM duty cycle (2% to 12%)
    -1.0 = 2% (0ms), 0.0 = 7% (1.5ms), 1.0 = 12% (2.4ms)
    """
    return 7 + (angle * 5)

def print_menu():
    print("\n--- Servo Position Selector ---")
    print(f"Current position: {current_position:.2f}")
    print("Options:")
    print("  u - Move UP (increase position)")
    print("  d - Move DOWN (decrease position)")
    print("  q - Quit")
    print("-" * 35)

def move_up():
    global current_position
    current_position = min(current_position + STEP_SIZE, 1.0)
    pwm.ChangeDutyCycle(angle_to_duty_cycle(current_position))
    sleep(0.1)  # Brief delay for servo to move
    print(f"Moved UP - New position: {current_position:.2f}")

def move_down():
    global current_position
    current_position = max(current_position - STEP_SIZE, -1.0)
    pwm.ChangeDutyCycle(angle_to_duty_cycle(current_position))
    sleep(0.1)  # Brief delay for servo to move
    print(f"Moved DOWN - New position: {current_position:.2f}")

def main():
    global current_position
    
    print("Servo Position Selector")
    print(f"Starting at position: {current_position:.2f}")
    
    pwm.start(0)
    pwm.ChangeDutyCycle(angle_to_duty_cycle(current_position))
    
    while True:
        print_menu()
        choice = input("Enter command: ").strip().lower()
        
        if choice == 'u':
            move_up()
        elif choice == 'd':
            move_down()
        elif choice == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid command. Please enter 'u', 'd', or 'q'.")
    
    pwm.stop()
    GPIO.cleanup()
    print("Servo closed.")

if __name__ == "__main__":
    main()
