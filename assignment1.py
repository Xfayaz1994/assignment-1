number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2

if number2 !=0:
    division = number1 / number2
else:
    division = 'cannot divide by 0'



print("\n--- Results ---")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")