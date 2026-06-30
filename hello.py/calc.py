# Function definitions for arithmetic
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    return x / y if y != 0 else "Error! Division by zero."

# Main loop to run the calculator
while True:
    print("\nSelect Operation: 1.Add 2.Sub 3.Mul 4.Div 5.Exit")
    choice = input("Enter choice (1-5): ")
    
    if choice == '5': break

    if choice in ('1', '2', '3', '4'):
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
            if choice == '1': print("Result:", add(n1, n2))
            elif choice == '2': print("Result:", subtract(n1, n2))
            elif choice == '3': print("Result:", multiply(n1, n2))
            elif choice == '4': print("Result:", divide(n1, n2))
        except ValueError: print("Invalid input.")
