"""
24-Hour Clock Alarm Calculator
Author: Amit Saxena
Date: 01-Aug-2025
Description: This program calculates what time an alarm will go off on a 24-hour clock.
It asks the user for the current time and hours to wait, then outputs the alarm time.
"""

def calculate_alarm_time():
    """
    Calculate what time the alarm will go off on a 24-hour clock.
    """
    print("=" * 50)
    print("24-HOUR CLOCK ALARM CALCULATOR")
    print("=" * 50)
    
    try:
        # Get current time from user
        current_time = int(input("Enter the current time (0-23 hours): "))
        
        # Validate current time input
        if current_time < 0 or current_time > 23:
            print("Error: Current time must be between 0 and 23!")
            return
        
        # Get hours to wait for alarm
        hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))
        
        # Validate hours to wait input
        if hours_to_wait < 0:
            print("Error: Hours to wait cannot be negative!")
            return
        
        # Calculate alarm time using modulo 24
        alarm_time = (current_time + hours_to_wait) % 24
        
        # Display results
        print("\n" + "-" * 40)
        print("ALARM CALCULATION:")
        print("-" * 40)
        print(f"Current time:    {current_time:>2} hours")
        print(f"Hours to wait:   {hours_to_wait:>2} hours")
        print("-" * 40)
        print(f"Alarm will go off at: {alarm_time:>2} hours")
        
        # Convert to 12-hour format for better understanding
        if alarm_time == 0:
            time_12hr = "12:00 AM (midnight)"
        elif alarm_time < 12:
            time_12hr = f"{alarm_time}:00 AM"
        elif alarm_time == 12:
            time_12hr = "12:00 PM (noon)"
        else:
            time_12hr = f"{alarm_time - 12}:00 PM"
        
        print(f"                ({time_12hr})")
        print("-" * 40)
        
    except ValueError:
        print("Error: Please enter valid integers for time values!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main function that runs the clock alarm calculator.
    """
    print("WELCOME TO THE 24-HOUR CLOCK ALARM CALCULATOR")
    print("This program calculates what time your alarm will go off.")
    print("Example: If it's currently 13 (1 PM) and you wait 50 hours,")
    print("         the alarm will go off at 15 (3 PM).")
    
    while True:
        calculate_alarm_time()
        
        # Ask if user wants to calculate another alarm
        try:
            another = input("\nCalculate another alarm? (y/n): ").lower().strip()
            if another != 'y':
                print("\nThank you for using the Clock Alarm Calculator!")
                print("Goodbye!")
                break
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            print("Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

# Run the program if this file is executed directly
if __name__ == "__main__":
    main() 
