print("===KWADWO'S SUPER CALCULATOR===")    
print("Type 'exit' to close")

while True:
    num1 = input("\"Enter first number (or 'exit'): ")
    if num1 == "exit":
        break
    num2 = input("Enter second number: ")

    num1 = int(num1)
    num2 = int(num2)
    
    print("Addition: ", num1 + num2)
    print("Subtraction: ", num1 - num2)
    print("Multiplication: ", num1 * num2)
    print("Division: ", num1 / num2)