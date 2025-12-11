from gpiozero import Servo, Device
from gpiozero.pins.rpigpio import RPiGPIOFactory
from time import sleep

# Use RPiGPIOFactory for Pi 5 compatibility
Device.pin_factory = RPiGPIOFactory()

GPIO_PIN = 18
STEP_SIZE = 0.05  # Increment for each step

servo = Servo(GPIO_PIN)
current_position = 0.0

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
    servo.value = current_position
    sleep(0.1)  # Brief delay for servo to move
    print(f"Moved UP - New position: {current_position:.2f}")

def move_down():
    global current_position
    current_position = max(current_position - STEP_SIZE, -1.0)
    servo.value = current_position
    sleep(0.1)  # Brief delay for servo to move
    print(f"Moved DOWN - New position: {current_position:.2f}")

def main():
    global current_position
    
    print("Servo Position Selector")
    print(f"Starting at position: {current_position:.2f}")
    
    servo.value = current_position
    
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
    
    servo.close()
    print("Servo closed.")

if __name__ == "__main__":
    main()
