def add(*numbers):
    return sum(numbers)

def subtract(a, b):
    return a - b

def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def exponentiate(base, exponent):
    return base ** exponent

def main():
    print("Select operation:")
    print("'+' Add (multiple numbers)")
    print("'-' Subtract (a - b)")
    print("'*' Multiply (multiple numbers)")
    print("'/' Divide (a / b)")
    print("'e' Exponentiate (base ^ exponent)")

    while True:
        choice = input("Enter choice (+/-/*///e): ")

        if choice == '+':
            numbers = list(map(float, input("Enter numbers to add separated by space: ").split()))
            print(f"Result: {add(*numbers)}")

        elif choice == '-':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"Result: {subtract(num1, num2)}")

        elif choice == '*':
            numbers = list(map(float, input("Enter numbers to multiply separated by space: ").split()))
            print(f"Result: {multiply(*numbers)}")

        elif choice == '/':
            num1 = float(input("Enter the numerator: "))
            num2 = float(input("Enter the denominator: "))
            print(f"Result: {divide(num1, num2)}")

        elif choice == 'ee':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            print(f"Result: {exponentiate(base, exponent)}")

        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (y/n): ")
        if next_calculation.lower() != 'y':
            break

if __name__ == "__main__":
    main()
