num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
operator = float(input("Enter the operator (+, -, *, /): "))
if operator == '+':
    result = num_1 + num_2
elif operator == '-':
    result = num_1 - num_2
elif operator == '*':
    result = num_1 * num_2
elif operator == '/':
    if num_2 != 0:
        result = num_1 / num_2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

    print(f"The result is: {result}")