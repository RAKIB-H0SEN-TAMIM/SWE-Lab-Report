# main.py
from calculator import add, subtract, multiply, divide

if __name__ == "__main__":
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print(f"Result: {add(a, b)}")
    elif choice == '2':
        print(f"Result: {subtract(a, b)}")
    elif choice == '3':
        print(f"Result: {multiply(a, b)}")
    elif choice == '4':
        try:
            print(f"Result: {divide(a, b)}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid choice.")
