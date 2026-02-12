
#       ADVANCED CLI CALCULATOR


import os
import math

# Utility Functions

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 45)
    print("        🧮  ADVANCED CLI CALCULATOR")
    print("=" * 45)


#Calculator Functions 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Error: Division by zero!"
    return a / b

def modulus(a, b):
    if b == 0:
        return "❌ Error: Modulus by zero!"
    return a % b

def power(a, b):
    return a ** b

def percentage(a, b):
    return (a / 100) * b


#  Main Program 

def main():
    while True:
        clear_screen()
        print_header()

        print("\nChoose an Operation:")
        print("1 ➤ Addition (+)")
        print("2 ➤ Subtraction (-)")
        print("3 ➤ Multiplication (*)")
        print("4 ➤ Division (/)")
        print("5 ➤ Modulus (%)")
        print("6 ➤ Power (a^b)")
        print("7 ➤ Percentage (a% of b)")
        print("8 ➤ Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == '8':
            print("\n👋 Thank you for using the calculator!")
            break

        if choice in ['1','2','3','4','5','6','7']:
            try:
                num1 = float(input("\nEnter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("\n❌ Invalid input! Please enter numeric values only.")
                input("\nPress Enter to continue...")
                continue

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = modulus(num1, num2)
            elif choice == '6':
                result = power(num1, num2)
            elif choice == '7':
                result = percentage(num1, num2)

            print("\n" + "-" * 45)
            print(f"✅ Result: {result}")
            print("-" * 45)

            input("\nPress Enter to continue...")

        else:
            print("\n❌ Invalid choice! Please select between 1-8.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()