"""
Restaurant Meal Calculator
Author: [Your Name]
Date: [Current Date]
Description: This program calculates the total amount of a meal purchased at a restaurant,
including 18% tip and 7% sales tax.
"""

def calculate_meal_total():
    """
    Calculate the total amount of a meal including tip and tax.
    """
    print("=" * 50)
    print("RESTAURANT MEAL CALCULATOR")
    print("=" * 50)
    
    try:
        # Get the food charge from user
        food_charge = float(input("Enter the charge for the food: $"))
        
        # Validate input
        if food_charge < 0:
            print("Error: Food charge cannot be negative!")
            return
        
        # Calculate tip (18%)
        tip_amount = food_charge * 0.18
        
        # Calculate sales tax (7%)
        sales_tax = food_charge * 0.07
        
        # Calculate total price
        total_price = food_charge + tip_amount + sales_tax
        
        # Display results
        print("\n" + "-" * 40)
        print("MEAL BREAKDOWN:")
        print("-" * 40)
        print(f"Food Charge:     ${food_charge:>10.2f}")
        print(f"Tip (18%):       ${tip_amount:>10.2f}")
        print(f"Sales Tax (7%):  ${sales_tax:>10.2f}")
        print("-" * 40)
        print(f"TOTAL PRICE:     ${total_price:>10.2f}")
        print("-" * 40)
        
    except ValueError:
        print("Error: Please enter a valid number for the food charge!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main function that runs the restaurant meal calculator.
    """
    print("WELCOME TO THE RESTAURANT MEAL CALCULATOR")
    print("This program calculates your meal total including tip and tax.")
    
    while True:
        calculate_meal_total()
        
        # Ask if user wants to calculate another meal
        try:
            another = input("\nCalculate another meal? (y/n): ").lower().strip()
            if another != 'y':
                print("\nThank you for using the Restaurant Meal Calculator!")
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